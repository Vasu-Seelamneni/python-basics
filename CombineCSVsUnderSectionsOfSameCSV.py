import csv
import pandas as pd
import os

# Set the directory containing the CSV files
directory = 'C:/Users/vasu_seelamneni/OneDrive - Dell Technologies/Desktop/Vasu/Dell-Team/Sprints/FY24/0501/Mass Update Oppty/Vasu/Errors/Error'

# Get a list of CSV file names in the directory
csv_files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.csv')]

# Create a dictionary to store dataframes for each sheet
dfs = {}

# Loop through each CSV file and add its contents to the appropriate sheet
for file in csv_files:
    # Get the sheet name from the file name
    sheet_name = os.path.splitext(os.path.basename(file))[0]
    
    # Read the CSV file into a pandas dataframe
    df = pd.read_csv(file)
    
    # Add the dataframe to the dictionary
    dfs[sheet_name] = df

# Write the dataframes to a single CSV file with multiple sheets
with open('output_file.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for sheet_name, df in dfs.items():
        writer.writerow([sheet_name])
        writer.writerow([])
        df.to_csv(csvfile, index=False)
        writer.writerow([])