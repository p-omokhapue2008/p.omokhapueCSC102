import pandas as pd


# Load the dataset
df1 = pd.read_csv('C:/Users/pecul/OneDrive/Documents/p.omokhapueCSC102/week-8/Datasetskaggle_data/dataset1.csv') 
df2 = pd.read_csv('C:/Users/pecul/OneDrive/Documents/p.omokhapueCSC102/week-8/Datasetskaggle_data/dataset2.csv') 
df3 = pd.read_csv('C:/Users/pecul/OneDrive/Documents/p.omokhapueCSC102/week-8/Datasetskaggle_data/dataset3.csv') 


print("Dataset 1 - First 7 rows: ")
print(df1.head(7))

print("\nDataset 2 - First 7 rows: ")
print(df2.head(7))

print("\nDataset 3 - First 7 rows: ")
print(df3.head(7))

print("\nDataset 1 - First 3 columns (1st row):")
print(df1.iloc[0, :3])

print("\nDataset 2 - First 3 columns(1st row):")
print(df2.iloc[0, :3])

print("\nDataset 3 - First 3 columns (1st row):")
print(df3.iloc[0, :3])

