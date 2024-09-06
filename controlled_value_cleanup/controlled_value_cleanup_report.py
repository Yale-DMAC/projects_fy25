import connections.SQL as sql
import pandas as pd
import time

#Query1 checks for the enum values, ids, table position, and numbr of associated records for Container Types in both archival objects and Top Containers
QUERY1 = """
WITH Type2Counts AS (
	SELECT
		ev.id,
		ev.value,
		ev.position,
		COUNT(sc2.instance_id) AS counter
	FROM sub_container sc2
	RIGHT JOIN enumeration_value ev ON sc2.type_2_id = ev.id
	WHERE ev.enumeration_id = 16
	GROUP BY ev.id, ev.value, ev.position
),
TopContainerCounts AS (
	SELECT
		ev2.id,
		ev2.value,
		ev2.position,
		COUNT(tc.id) AS counter
	FROM top_container tc
	RIGHT JOIN enumeration_value ev2 ON tc.type_id = ev2.id
	WHERE ev2.enumeration_id = 16
	GROUP BY ev2.id, ev2.value, ev2.position
),
CombinedCounts AS (
	SELECT id, value, position, counter
	FROM Type2Counts
	UNION ALL
	SELECT id, value, position, counter
	FROM TopContainerCounts
)
SELECT
	SUM(counter) AS total_counter,
	id,
	value,
	position
FROM CombinedCounts
GROUP BY id, value, position
"""
#Query2 is specifically creating a report of individual records and who created them for container types in our controlled values tables who exist in specific positions i.e. our error values.
#This query will need to have its where conditions updated to the user's needs.
QUERY2 = """
WITH Type2report AS (
	SELECT
	CONCAT('/repositories/', ao.repo_id, '/archival_objects/', ao.id) as URI,
	ao.root_record_id as resource_id,
    ao.parent_id as parent,
    ao.id as object_id,
	sc2.created_by as creator,
    ao.repo_id,
	ev.id,
		ev.value,
		ev.position
	FROM enumeration_value ev
	LEFT JOIN sub_container sc2 ON sc2.type_2_id = ev.id
	LEFT JOIN instance i ON i.id = sc2.instance_id
	LEFT JOIN archival_object ao ON ao.id = i.archival_object_id
	WHERE ev.enumeration_id = 16 and (ev.position = "10" OR ev.position >= "15")
),
TopContainerreport AS (
	SELECT
	CONCAT('/repositories/', tc.repo_id, '/top_containers/', tc.id) as URI,
	tc.created_by as creator,
    tc.repo_id,
    tc.id as object_id,
		ev2.id,
		ev2.value,
		ev2.position
	FROM enumeration_value ev2
	LEFT JOIN top_container tc ON tc.type_id = ev2.id
	WHERE ev2.enumeration_id = 16 and (ev2.position = "10" OR ev2.position >= "15")
),
Combinedreport AS (
	SELECT URI, repo_id, resource_id, parent, object_id, creator, value
	FROM Type2report
	UNION ALL
	SELECT URI, repo_id, NULL as resource_id, NULL as parent, object_id, creator, value
	FROM TopContainerreport
)
SELECT
    r.repo_code,
    cr.resource_id as resource,
	cr.parent,
    cr.object_id,
    ao.title,
    u.name as creator,
	cr.value
FROM Combinedreport cr
JOIN archival_object ao ON cr.object_id = ao.id
JOIN user u ON u.username = cr.creator
JOIN repository r ON r.id = cr.repo_id
WHERE position = "10" OR position >= "15"
"""
#Query3 creates a report of enum ids, values, table positions, and a count of associated records for Extent Types.
QUERY3 = """
SELECT count(ex.id), ev.id, ev.value, ev.position 
FROM extent ex
RIGHT JOIN enumeration_value ev ON ev.id = ex.extent_type_id
WHERE ev.enumeration_id = 14
GROUP by ev.id, ev.value, ev.position
"""

#Checks if the connection to the SQL database succeeded, otherwise returns and error.
if sql.conn():
    date_str = time.strftime("%y%m%d")
    print("Connected to SQL.")
    cursor = sql.connection.cursor()

  #Executes Query1 and 2 then saves them as dataframes
    print("Executing Query...")
    cursor.execute(QUERY1)
    combinedcounts = cursor.fetchall()
    dfc = pd.DataFrame(data=combinedcounts, columns=["Related Records", "Enumeration ID", "Value Name", "Enumeration Position"])
    print("Query 1 Completed.")

    print("Executing Query...")
    cursor.execute(QUERY2)
    combinedreport = cursor.fetchall()
    dfr = pd.DataFrame(data=combinedreport, columns=["Repository", "Resource ID", "Parent ID", "Object ID", "Tile", "Creator", "Value Name"])
    print("Query 2 Completed.")

  #Saves the two Container Type Queries into a single Excel workbook
    with pd.ExcelWriter(f"files/{date_str}_container_type_report.xlsx", engine='xlsxwriter', mode='w') as writer:
        dfr.to_excel(writer, sheet_name="Enumeration URI", index=False)
        dfc.to_excel(writer, sheet_name="Enumeration Counts", index=False)

  #Executes Query3 then saves it as a dataframe
    print("Executing Query...")
    cursor.execute(QUERY3)
    data = cursor.fetchall()
    df = pd.DataFrame(data=data, columns=["Related Records", "Enumeration ID", "Value Name", "Enumeration Position"])
    print("Query 3 Completed")

  #Saves the Extent Type query into an excel workbook
    df.to_excel(f"files/{date_str}_extent_type_report.xlsx",engine='xlsxwriter', index=False)
else:
    print("Connection failed. Are you connected to the VPN?")
