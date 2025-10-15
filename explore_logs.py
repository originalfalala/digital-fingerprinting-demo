import pandas as pd

# Load the dataset we created earlier
df = pd.read_csv("user_logs.csv", parse_dates=["timestamp"])

# Show the first 10 rows
print("📋 Sample data:")
print(df.head(10), "\n")

# Get dataset info
print("🔍 Basic info:")
print(df.info(), "\n")

# Check how many records per user
print("👥 Number of events per user:")
print(df['user'].value_counts(), "\n")

# Count how many events of each type
print("🧠 Event type distribution:")
print(df['event_type'].value_counts(), "\n")

# Check if there are any unusual or missing values
print("❓ Missing values per column:")
print(df.isnull().sum(), "\n")

# Time range covered
print(f"🕓 Time range: {df['timestamp'].min()}  →  {df['timestamp'].max()}")
