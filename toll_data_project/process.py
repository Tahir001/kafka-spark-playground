import pandas as pd
import numpy as np

# Extract data from different files

def extract_data():
    # File paths
    csv_file = 'data/raw/vehicle-data.csv'
    txt_file = 'data/raw/payment-data.txt'
    tsv_file = 'data/raw/tollplaza-data.tsv'


    # Define the column names
    vehicle_cols = ["Rowid", "Timestamp", "Anonymized Vehicle number", "Vehicle type", "Number of axles", "Vehicle code"]
    payment_cols = ["Rowid", "Timestamp", "Tollplaza id", "Tollplaza code", "Type of Payment code", "Vehicle Code"]
    tollplaza_cols = ["Rowid", "Timestamp", "Anonymized Vehicle number", "Vehicle type", "Number of axles", "Tollplaza id", "Tollplaza code"]

    # Read them in as DataFrames
    vehicle_df = pd.read_csv(csv_file, header=None, names=vehicle_cols)
    toll_df = pd.read_csv(tsv_file, delimiter='\t', names=tollplaza_cols)
    payment_df = pd.read_csv(txt_file, sep=" ", header=None, names=payment_cols, engine='python')  # Use engine='python' for fixed-width text file

    # Pre-process data 
    vehicle_df = vehicle_df[["Rowid", "Timestamp", "Anonymized Vehicle number", "Vehicle type"]]
    toll_df = toll_df[['Number of axles', 'Tollplaza id', 'Tollplaza code']]
    payment_df = payment_df[['Type of Payment code', 'Vehicle Code']]
    
    # Save these models in corresponding files 
    vehicle_df.to_csv("data/transformed/csv_data.csv")
    toll_df.to_csv("data/transformed/tsv_data.csv")
    payment_df.to_csv("data/transformed/fixed_width_data.csv")

    return vehicle_df, toll_df, payment_df

# Execute the function only when running the script directly
if __name__ == "__main__":
  vehicle_df, toll_df, payment_df = extract_data()

  print("Data extraction completed!")