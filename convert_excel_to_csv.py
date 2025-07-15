import pandas as pd
import os

excel_file = r"/path/to/your/file.xlsx" # Replace with your Excel file path

output_dir = os.path.dirname(excel_file)

xls = pd.read_excel(excel_file, sheet_name=None)

# Convert each sheet to CSV
for sheet_name, df in xls.items():
    clean_name = sheet_name.replace(" ", "_").replace("/", "_")
    csv_path = os.path.join(output_dir, f"{clean_name}.csv")
    df.to_csv(csv_path, index=False)
    print(f" Saved: {csv_path}")