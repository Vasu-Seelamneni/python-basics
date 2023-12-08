import os
import pandas as pd

# Set the path to the original CSV file
file_path = "C:/Users/vasu_seelamneni/OneDrive - Dell Technologies/Desktop/Vasu/Dell-Team/Sprints/FY24/0501/Mass Update Oppty/Vasu/Errors/New folder/12-Sept-22.csv"

# Set the number of rows to include in each output file
rows_per_file = 10110

# Create a Pandas dataframe from the original CSV file
df = pd.read_csv(file_path)

# Split the dataframe into smaller dataframes with a specified number of rows
df_list = [df[i:i+rows_per_file] for i in range(0, df.shape[0], rows_per_file)]

# Create a directory to store the output files
output_dir = "C:/Users/vasu_seelamneni/OneDrive - Dell Technologies/Desktop/Vasu/Dell-Team/Sprints/FY24/0501/Mass Update Oppty/Vasu/Errors/New folder"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Export each dataframe to a separate CSV file
for i, df in enumerate(df_list):
    output_file_path = os.path.join(output_dir, f"result_{i+1}.csv")
    df.to_csv(output_file_path, index=False)
