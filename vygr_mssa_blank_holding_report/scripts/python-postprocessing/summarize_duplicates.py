import pandas as pd
import os
import logging

# --- Config ---
script_dir = os.path.dirname(__file__)
csv_file_path = os.path.join(script_dir, '..', '..', 'data', 'mssa_diss_blank_mfhd__202504241239.csv')
columns_to_summarize = ['BIB_ID', 'TITLE', 'AUTHOR']
output_csv_path = os.path.join(script_dir, '..', '..', 'data', 'duplicate_summary_by_value.csv')
log_file_path = os.path.join(script_dir, '..', '..', 'logs', 'summarize_duplicates.log')
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
    logging.info(f"Reading input CSV: {csv_file_path}")
    df = pd.read_csv(csv_file_path, usecols=['MFHD_ID'] + columns_to_summarize, dtype=str)
    logging.info(f"Read {len(df)} records.")

    summary_data = []

    for col in columns_to_summarize:
        logging.info(f"\n--- Summarizing Duplicates for Column: '{col}' ---")

        if col not in df.columns:
            logging.warning(f"Column '{col}' not found, skipping.")
            continue

        series = df[col].astype(str).str.strip()
        non_blank_series = series[series != '']

        if non_blank_series.empty:
            logging.info("No non-blank values to analyze for duplicates.")
            continue

        value_counts = non_blank_series.value_counts()
        duplicate_values = value_counts[value_counts > 1].index

        num_duplicate_values = len(duplicate_values)
        logging.info(f"Found {num_duplicate_values} unique non-blank values appearing more than once.")

        if num_duplicate_values > 0:
            df_filtered = df[df[col].isin(duplicate_values)].copy()
            df_filtered['value_group'] = df_filtered[col].astype(str).str.strip()

            grouped = df_filtered.groupby('value_group')['MFHD_ID'].agg(['count', lambda x: ', '.join(x.astype(str).unique())])
            grouped.rename(columns={'count': 'OccurrenceCount', '<lambda_0>': 'AssociatedMFHD_IDs'}, inplace=True)

            for value, row in grouped.iterrows():
                summary_data.append({
                    'ColumnAnalyzed': col,
                    'DuplicateValue': value,
                    'OccurrenceCount': row['OccurrenceCount'],
                    'AssociatedMFHD_IDs': row['AssociatedMFHD_IDs']
                })

        else:
            logging.info("No duplicate non-blank values found in this column.")

        logging.info(f"--- Finished Summarizing for '{col}' ---")

    # --- Write Summary CSV ---
    if summary_data:
        summary_df = pd.DataFrame(summary_data)
        output_dir = os.path.dirname(output_csv_path)
        os.makedirs(output_dir, exist_ok=True)
        summary_df.to_csv(output_csv_path, index=False)
        logging.info(f"Duplicate summary saved to: {output_csv_path}")
    else:
        logging.info("No duplicate values found across analyzed columns to generate summary CSV.")
    # --- End Write Summary CSV ---

except FileNotFoundError:
    logging.error(f"Error: Input CSV file not found at {csv_file_path}")
except Exception as e:
    logging.exception(f"An unexpected error occurred: {e}")

logging.info("--- Duplicate Summary Analysis Complete ---")
