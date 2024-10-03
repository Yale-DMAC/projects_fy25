import requests
import pandas as pd
import json

# ArchivesSpace connection details
aspace_url = 'https://testarchivesspace.library.yale.edu/api'
username = ''
password = ''

# CSV file path
csv_file_path = 'C:/Users/tw722/Downloads/updated_filtered_agents_without_http.csv'  # Update this path as necessary

# Authenticate with ArchivesSpace API
def authenticate():
    auth_url = f"{aspace_url}/users/{username}/login"
    auth_params = {'username': username, 'password': password}
    
    response = requests.post(auth_url, data=auth_params)
    
    if response.status_code == 200:
        session = response.json()['session']
        print("Successfully authenticated.")
        return session
    else:
        print(f"Failed to authenticate: {response.status_code}, {response.text}")
        raise Exception("Failed to authenticate.")

# Load CSV data
def load_csv_data(csv_file):
    df = pd.read_csv(csv_file)
    return df

# Fetch agent record from ArchivesSpace by agent ID
def fetch_agent_record(agent_id, session):
    headers = {'X-ArchivesSpace-Session': session}
    
    # Construct the correct URL to fetch agent record
    agent_url = f"{aspace_url}{agent_id}"
    print(f"Fetching agent with URL: {agent_url}")  # Debugging URL
    
    response = requests.get(agent_url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching agent {agent_id}: {response.status_code}, {response.text}")
        return None

# Replace the primary record_identifier in the agent record within 'agent_record_identifiers' section
def replace_primary_record_identifier(agent_id, record, http_address, session):
    headers = {
        'X-ArchivesSpace-Session': session,
        'Content-Type': 'application/json'
    }
    
    # Check if 'agent_record_identifiers' section exists
    if 'agent_record_identifiers' not in record:
        print(f"No 'agent_record_identifiers' section found for agent {agent_id}")
        return
    
    # Replace the primary record_identifier
    primary_found = False
    for identifier in record['agent_record_identifiers']:
        # Check if this is the primary identifier
        if identifier.get('primary_identifier', False) is True:
            print(f"Replacing primary record_identifier for agent {agent_id} from '{identifier['record_identifier']}' to '{http_address}'")
            identifier['record_identifier'] = http_address
            primary_found = True
            break
    
    if not primary_found:
        print(f"No primary record_identifier found for agent {agent_id}")
        return
    
    # Verify the modified record structure before sending the request
    print(f"Modified record for agent {agent_id}: {json.dumps(record, indent=2)}")  # Print the modified record
    
    update_url = f"{aspace_url}{agent_id}"  # Use the correct URL format for updating the agent
    print(f"Updating agent with URL: {update_url}")  # Debugging URL
    
    # Use POST to update the agent record with the new identifier
    response = requests.post(update_url, headers=headers, json=record)
    
    if response.status_code == 200:
        print(f"Successfully updated agent {agent_id}")
    else:
        print(f"Error updating agent {agent_id}: {response.status_code}, {response.text}")
        print(f"Response content: {response.content}")  # Log the full response content for debugging

# Main process
def main():
    try:
        # Step 1: Authenticate with the ArchivesSpace API
        session = authenticate()

        # Step 2: Load CSV data
        agent_data = load_csv_data(csv_file_path)

        # Step 3: Loop through each agent record in the CSV
        for index, row in agent_data.iterrows():
            agent_id = row['agent_id']  # The unique ID for the agent, includes the full path
            http_address = row['http_address']  # The new HTTPS address from CSV
            
            # Step 4: Fetch the existing agent record from ArchivesSpace
            agent_record = fetch_agent_record(agent_id, session)
            
            if agent_record:
                # Step 5: Replace the primary record_identifier in agent_record_identifiers
                replace_primary_record_identifier(agent_id, agent_record, http_address, session)
                
                # Step 6: Verify the change by fetching the record again
                updated_record = fetch_agent_record(agent_id, session)
                print(f"Updated record verification for agent {agent_id}: {json.dumps(updated_record, indent=2)}")

    except Exception as e:
        print(f"Error in process: {e}")

if __name__ == "__main__":
    main()













 
