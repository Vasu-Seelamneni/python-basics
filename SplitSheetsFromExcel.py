import pandas as pd

# Open Excel file
file_path = "C:\\Dell-Team\\Sprints\\FY24\\0402\\SFMC\\Lead\\Mass Update\\PROD\\SAR-26789-data.xlsx"
excel_file = pd.ExcelFile(file_path)

# Loop through each sheet and save as separate file
for sheet_name in excel_file.sheet_names:
    sheet_df = pd.read_excel(excel_file, sheet_name)
    sheet_file_name = f"{sheet_name}.xlsx"
    sheet_df.to_excel(sheet_file_name, index=False)
    print(f"{sheet_file_name} created successfully.")