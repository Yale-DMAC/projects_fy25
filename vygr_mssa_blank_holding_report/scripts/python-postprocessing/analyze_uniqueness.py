import pandas as pd
import logging
import os

# --- Config ---
script_dir = os.path.dirname(__file__)
csv_file_path = os.path.join(script_dir, '..', '..', 'data', 'mssa_diss_blank_mfhd__202504241239.csv')
columns_to_check = ['MFHD_ID', 'BIB_ID', 'TITLE', 'AUTHOR']
output_csv_path = os.path.join(script_dir, '..', '..', 'data', 'duplicate_records_analysis.csv')
log_file_path = os.path.join(script_dir, '..', '..', 'logs', 'uniqueness_analysis.log')
# --- End Config ---

# --- Logging Setup ---
log_full_path = log_file_path

if os.path.exists(log_full_path):
    os.remove(log_full_path)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_full_path),
        logging.StreamHandler() 
    ]
)
# --- End Logging Setup ---

try:
    logging.info(f"Reading CSV file: {csv_file_path}")
    df = pd.read_csv(csv_file_path, dtype=str)
    logging.info("CSV file read successfully.")
    logging.info(f"Analyzing uniqueness in columns: {', '.join(columns_to_check)}")

    total_records = len(df)
    logging.info(f"Total records: {total_records}\n")

    all_duplicates_list = []

    for col in columns_to_check:
        logging.info(f"\n--- Analyzing Column: '{col}' ---")
        series = df[col].astype(str)

        blank_mask = series.str.strip() == ''
        blank_count = blank_mask.sum()
        logging.info(f"Total blank values: {blank_count}")
        if blank_count > 0:
            blank_mfhd_ids = df.loc[blank_mask, 'MFHD_ID'].tolist()
            if len(blank_mfhd_ids) > 20:
                logging.info(f"  MFHD_IDs with blank '{col}': {blank_mfhd_ids[:20]} ... (and {len(blank_mfhd_ids) - 20} more)")
            else:
                logging.info(f"  MFHD_IDs with blank '{col}': {blank_mfhd_ids}")

        non_blank_series = series[~blank_mask].str.strip()
        total_non_blank = len(non_blank_series)
        unique_non_blank = non_blank_series.nunique()

        logging.info(f"Total non-blank values: {total_non_blank}")
        logging.info(f"Unique non-blank values: {unique_non_blank}")

        if total_non_blank == unique_non_blank:
            logging.info("Result: All non-blank values are unique.")
        else:
            logging.info("Result: Duplicate non-blank values found.")
            value_counts = non_blank_series.value_counts()
            duplicate_values = value_counts[value_counts > 1].index.tolist()
            num_duplicates = len(duplicate_values)
            logging.info(f"Number of unique values that appear more than once: {num_duplicates}")

            duplicate_mask = non_blank_series.isin(duplicate_values)
            num_rows_affected = duplicate_mask.sum()
            logging.info(f"Total rows containing non-unique {col} values: {num_rows_affected}")

            if num_duplicates > 0:
                top_n = 5
                logging.info(f"Top {min(top_n, num_duplicates)} duplicate values (value: count):")
                for value, count in value_counts[value_counts > 1].head(top_n).items():
                    logging.info(f'  - "{value}": {count}')
                if num_duplicates > top_n:
                    logging.info("  ...")

                duplicate_rows_df = df[df[col].isin(duplicate_values) & (~blank_mask)].copy()
                duplicate_rows_df['DuplicateInColumn'] = col
                all_duplicates_list.append(duplicate_rows_df)

        logging.info(f"----------------------------")

    if all_duplicates_list:
        all_duplicates_df = pd.concat(all_duplicates_list, ignore_index=True)
        output_dir = os.path.dirname(output_csv_path)
        os.makedirs(output_dir, exist_ok=True)
        all_duplicates_df.to_csv(output_csv_path, index=False)
        logging.info(f"Duplicate records analysis saved to: {output_csv_path}")
    else:
        logging.info("No duplicate records found to save to CSV.")

except FileNotFoundError:
    logging.error(f"Error: Input CSV file not found at {csv_file_path}")
except Exception as e:
    logging.exception(f"An unexpected error occurred: {e}")

logging.info("--- Analysis Complete ---")
