import pandas as pd
import re
import logging
import os
from collections import defaultdict

# --- Config ---
script_dir = os.path.dirname(__file__)
csv_file_path = os.path.join(script_dir, '..', '..', 'data', 'mssa_diss_blank_mfhd__202504241239.csv')
column_name = 'BEGIN_PUB_DATE'
valid_year_range = (1500, 2025)
log_file_path = os.path.join(script_dir, '..', '..', 'logs', 'pub_date_analysis.log')
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
    df = pd.read_csv(csv_file_path, dtype=str)
    logging.info(f"Read {len(df)} records.")

    if column_name not in df.columns:
        logging.error(f"Error: Column '{column_name}' not found in the CSV file.")
        raise SystemExit # Exit if the crucial column is missing

    logging.info(f"--- Analyzing Column: '{column_name}' ---")

    series = df[column_name].astype(str)
    blank_mask = series.str.strip() == ''
    blank_count = blank_mask.sum()
    logging.info(f"Found {blank_count} blank value(s).")

    if blank_count > 0:
        blank_mfhd_ids = df.loc[blank_mask, 'MFHD_ID'].tolist()
        logging.info(f"  MFHD_ID(s) with blank '{column_name}': {blank_mfhd_ids}")

    non_blank_series = series[~blank_mask].str.strip()

    valid_years = []
    invalid_patterns = defaultdict(list)
    year_pattern = re.compile(r'^\d{4}$')

    for index, value in non_blank_series.items():
        mfhd_id = df.loc[index, 'MFHD_ID']
        if year_pattern.match(value):
            try:
                year = int(value)
                if valid_year_range[0] <= year <= valid_year_range[1]:
                    valid_years.append(year)
                else:
                    invalid_patterns[value].append(mfhd_id)
            except ValueError:
                invalid_patterns[value].append(mfhd_id) 
        else:
            invalid_patterns[value].append(mfhd_id)

    logging.info(f"Processed {len(non_blank_series)} non-blank entries.")
    logging.info(f"Found {len(valid_years)} valid YYYY-formatted years (between {valid_year_range[0]}-{valid_year_range[1]}).")

    if invalid_patterns:
        total_invalid_records = sum(len(ids) for ids in invalid_patterns.values())
        logging.warning(f"Found {len(invalid_patterns)} unique invalid/out-of-range patterns affecting {total_invalid_records} records:")
        for pattern, mfhd_ids in sorted(invalid_patterns.items()):
            reason = "out of plausible range {}-{}".format(*valid_year_range) if pattern.isdigit() else "does not match YYYY format"
            logging.warning(f"  - '{pattern}' ({reason}) - MFHD_IDs: {mfhd_ids}")

    if valid_years:
        logging.info(f"Earliest valid year found: {min(valid_years)}")
        logging.info(f"Latest valid year found: {max(valid_years)}")

        decades = defaultdict(int)
        for year in valid_years:
            decade_start = (year // 10) * 10
            decades[decade_start] += 1

        logging.info("\n--- Counts per Decade (based on valid years) ---")
        for decade in sorted(decades.keys()):
            logging.info(f"  {decade}s: {decades[decade]}")
        logging.info("--------------------------------------------")

    logging.info(f"--- Analysis Complete for '{column_name}' ---")

except FileNotFoundError:
    logging.error(f"Error: Input CSV file not found at {csv_file_path}")
except Exception as e:
    logging.exception(f"An unexpected error occurred during processing: {e}")
