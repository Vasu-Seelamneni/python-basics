import pandas as pd

# Open Excel file
file_path = "C:\\Dell-Team\\Sprints\\FY24\\0402\\SFMC\\Lead\\Mass Update\\PROD\\SAR-26789-data.xlsx"
excel_file = pd.ExcelFile(file_path)

# Loop through each sheet and count records
total_records = 0
for sheet_name in excel_file.sheet_names:
    sheet_df = pd.read_excel(excel_file, sheet_name)
    total_records += len(sheet_df)

# Print total number of records
print(f"Total number of records in all sheets: {total_records}")