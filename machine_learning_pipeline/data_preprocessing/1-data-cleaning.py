
# Step 0: Import necessary libraries
# os: Provides a way of using operating system dependent functionality, like interacting with the file system.
import pandas as pd
import os

# Get the directory where this script is located
# This ensures that the script can find the 'Titanic-Dataset.csv' file regardless of
# which directory you run the script from.
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'Titanic-Dataset.csv')


# Step 1: Load the dataset
# We use pandas' read_csv function to load the Titanic dataset into a DataFrame.
df = pd.read_csv(csv_path)
print("Dataset loaded successfully!")

# Display general information about the DataFrame.
# df.info() provides a concise summary of the DataFrame, including:
# - The index dtype and column dtypes
# - The number of non-null values in each column (useful for identifying missing data)
# - Memory usage
print("\nDataset Info:")
df.info()

# Display the first 5 rows of the DataFrame.
# df.head() is a pandas DataFrame method that returns the first n rows of the DataFrame.
# By default, n is 5, so df.head() will display the first 5 rows, which is useful for quickly
# inspecting the structure and content of the data after loading it.
print("\nFirst 5 rows:")
print(df.head())


# Step 2: Check for Duplicate Rows
# df.duplicated() returns a boolean Series indicating whether each row is a duplicate of a previous row.
# .sum() then counts the number of True values (i.e., duplicate rows).
print("\nChecking for duplicate rows:")
print(df.duplicated())

print("\nChecking the number of duplicate rows: ", df.duplicated().sum())
print("\n\n")


# Step 3: Identify Column Data Types
cat_col = [col for col in df.columns if df[col].dtype == 'object']
num_col = [col for col in df.columns if df[col].dtype != 'object']

print("\nCategorical Columns: ", cat_col)
print("Numerical Columns: ", num_col, "\n\n")


# Step 4: Analyze Categorical Columns
print(df[cat_col].nunique())
print("\nCategorical Columns Size: ", df[cat_col].size, "\n\n")


# Step 5: Calculate Missing Values as Percentage
print(df.isnull().sum(), "\n")
print(df.shape)
print(df.shape[0], "\n")
print(round(df.isnull().sum() / df.shape[0] * 100, 2), "\n\n")


# Step 6: Drop Irrelevant or Data-Heavy Missing Columns
"""
 Explain axis=1 and inplace=True:
    - axis=1: This parameter specifies that we want to drop columns. If we wanted to drop rows, we would use axis=0.
    - inplace=True: This parameter indicates that we want to modify the original DataFrame directly, 
      rather than creating a new DataFrame with the specified columns removed.
  Drop 'Cabin', 'Ticket', and 'Name' columns because they are either irrelevant for analysis or have too many missing values.
  Next, we handle missing values in the 'Embarked' and 'Age' columns:
    - For 'Embarked', we drop any rows where this value is missing, as it is a categorical variable and we cannot impute it easily.
    - For 'Age', we fill missing values with the mean age of the passengers, which is a common technique for handling missing numerical data.
"""
df1 = df.drop(['Cabin', 'Ticket', 'Name'], axis=1)
df1.dropna(subset=['Embarked'], inplace=True)
df1["Age"].fillna(df1["Age"].mean(), inplace=True)
print(df1)


# Step 7: Detect Outliers with Box Plot
import matplotlib.pyplot as plt

df3 = df1.copy()
"""
    📊 What this boxplot shows: 
    Box plot: https://www.geeksforgeeks.org/machine-learning/box-plot/
    Recall: https://www.geeksforgeeks.org/maths/interquartile-range/
"""
plt.boxplot(df3['Age'], vert=False)
plt.ylabel('Variable')
plt.xlabel('Age')
plt.title('Box Plot')
plt.show()

