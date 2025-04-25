import pandas as pd
import logging
import os
from collections import Counter

# --- Config ---
script_dir = os.path.dirname(__file__)
csv_file_path = os.path.join(script_dir, '..', '..', 'data', 'mssa_diss_blank_mfhd__202504241239.csv')
columns_to_analyze = ['PUBLISHER', 'PUB_PLACE']
log_file_path = os.path.join(script_dir, '..', '..', 'logs', 'publisher_place_analysis.log')
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

def analyze_column(df, column_name):
    logging.info(f"\n--- Analyzing Column: '{column_name}' ---")
    total_records = len(df)
    logging.info(f"Total Records: {total_records}")

    series = df[column_name].astype(str)
    blank_mask = series.str.strip() == ''
    blank_count = blank_mask.sum()
    blank_percentage = (blank_count / total_records) * 100 if total_records > 0 else 0
    logging.info(f"Blank Values: {blank_count} ({blank_percentage:.2f}%)")

    non_blank_series = series[~blank_mask].str.strip()
    non_blank_count = len(non_blank_series)
    logging.info(f"Non-Blank Values: {non_blank_count}")

    if non_blank_count > 0:
        value_counts = non_blank_series.value_counts()
        unique_count = len(value_counts)
        logging.info(f"Unique Non-Blank Values: {unique_count}")

        logging.info(f"All {unique_count} Unique Non-Blank Values and Counts:")
        for value, count in value_counts.items():
            percentage = (count / non_blank_count) * 100
            logging.info(f"  - '{value}': {count} ({percentage:.2f}%)")
    else:
        logging.info("No non-blank values to analyze.")

    logging.info(f"--- End Analysis for '{column_name}' ---")

try:
    logging.info(f"Reading input CSV: {csv_file_path}")
    df = pd.read_csv(csv_file_path, usecols=['MFHD_ID'] + columns_to_analyze, dtype=str)
    logging.info(f"Read {len(df)} records.")

    for col in columns_to_analyze:
        if col not in df.columns:
            logging.warning(f"Column '{col}' not found in CSV, skipping analysis.")
            continue
        analyze_column(df, col)

    logging.info("\n--- Analysis Complete ---")

except FileNotFoundError:
    logging.error(f"Error: Input CSV file not found at {csv_file_path}")
except Exception as e:
    logging.exception(f"An unexpected error occurred: {e}")
