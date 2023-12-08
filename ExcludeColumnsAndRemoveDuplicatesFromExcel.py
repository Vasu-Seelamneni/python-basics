import pandas as pd

# Read the CSV file into a pandas dataframe
df = pd.read_csv('C:\\Dell-Team\\Sprints\\FY24\\Grax\\19-Mar-2023\\FY24 Q1 DirectLead 2019_Nov04-Nov10\\Lead.csv')

# Drop all columns except the first column
df.drop(df.columns[1:], axis=1, inplace=True)

# Drop duplicates based on all columns
df.drop_duplicates(inplace=True)

# Save the modified dataframe to a new CSV file
df.to_csv('file_modified.csv', index=False)