import pandas as pd
import numpy as np

csv_file_path = '../../data/mssa_diss_blank_mfhd__202504241239.csv'
id_column = 'MFHD_ID'

try:
    df = pd.read_csv(csv_file_path, keep_default_na=False, dtype=str) # Read all as string initially, careful about NAs

    print(f"Analyzing blanks in: {csv_file_path}\n")
    total_records = len(df)
    print(f"Total records found: {total_records}\n")


    # Check for blanks in each column
    for col in df.columns:
        # Define blanks as empty strings '', None/NaN (though keep_default_na=False helps), or strings with only whitespace
        # .astype(str) so that we can apply .str methods
        blanks = df[col].astype(str).str.strip() == ''

        blank_count = blanks.sum()

        if blank_count > 0:
            print(f"--- Column: '{col}' ---")
            print(f"Found {blank_count} blank value(s) ({blank_count/total_records:.2%}).")
            
            blank_ids = df.loc[blanks, id_column].tolist()
            
            # Print IDs (limit if too many for readability)
            if len(blank_ids) > 20:
                 print(f"IDs with blanks: {blank_ids[:10]} ... (showing first 10)")
            elif len(blank_ids) > 0 :
                 print(f"IDs with blanks: {blank_ids}")
            else:
                 print("No blanks found.") # Should not happen given blank_count > 0 check, but this is safe.
            print("-" * (len(col) + 14)) # Separator line matches title length
            print("\n")
        else:
            pass # Keep output cleaner by default; only show cols WITH blanks

except FileNotFoundError:
    print(f"Error: CSV file not found at {csv_file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
