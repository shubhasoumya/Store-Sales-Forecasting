import pandas as pd

# Load the dataset
file_path = 'data/stores_sales_forecasting.csv'
df = pd.read_csv(file_path, encoding='ISO-8859-1')

# Check the data structure
print(df.info())
print(df.head())

# 1. Check for missing values and handle them
print(df.isnull().sum())  # Identify missing values
df.fillna(0, inplace=True)  # Replace missing values with 0 (or use other imputation methods)

# 2. Ensure date column is in proper datetime format
df['Order Date'] = pd.to_datetime(df['Order Date'])

# 3. Add new features for time-series analysis
df['year'] = df['Order Date'].dt.year
df['month'] = df['Order Date'].dt.month
df['week'] = df['Order Date'].dt.isocalendar().week
df['day'] = df['Order Date'].dt.day
df['weekday'] = df['Order Date'].dt.weekday  # 0 = Monday, 6 = Sunday

# 4. Ensure all relevant columns are numeric (e.g., sales amount)
df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')
df['Sales'].fillna(0, inplace=True)  # Handle invalid values

# 5. Add calculated columns (e.g., sales by store or category)
df['sales_per_region'] = df.groupby('Region')['Sales'].transform('sum')

# Save the cleaned dataset
df.to_csv('data/cleaned_dataset.csv', index=False)
print("Dataset cleaned and saved!")
