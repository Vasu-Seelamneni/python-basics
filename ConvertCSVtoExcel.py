import pandas as pd
import os

# Set the directory containing the CSV files
csv_directory = 'C:\\Dell-Team\\Sprints\\FY24\\Grax\\test'

# Set the directory for the output Excel files
excel_directory = 'C:\\Dell-Team\\Sprints\\FY24\\Grax\\test\\excel'

# Get a list of CSV file names in the directory
csv_files = [os.path.join(csv_directory, f) for f in os.listdir(csv_directory) if f.endswith('.csv')]

# Loop through each CSV file and convert it to an Excel file
for csv_file in csv_files:
    # Get the base file name without the extension
    base_name = os.path.splitext(os.path.basename(csv_file))[0]
    
    # Read the CSV file into a pandas dataframe
    df = pd.read_csv(csv_file)
    
    # Write the dataframe to an Excel file
    excel_file = os.path.join(excel_directory, f"{base_name}.xlsx")
    df.to_excel(excel_file, index=False)