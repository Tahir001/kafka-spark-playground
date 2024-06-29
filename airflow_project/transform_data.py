# import libraries
import pandas as pd

# Read in the data
df = pd.read_csv("/Users/tahir/Desktop/Github/playground_dataeng/extracted-data.txt", delimiter='#')

# Keep only the two columns we care about 
df = df[['visitorid', 'timestamp']]

# Capitalize the first letter of each element in the 'visitorid' column
df['visitorid'] = df['visitorid'].apply(lambda x: x[0].upper() + x[1:])

# Save the DataFrame to a CSV file
df.to_csv('/Users/tahir/Desktop/Github/playground_dataeng/transformed_data_run.csv', index=False)
