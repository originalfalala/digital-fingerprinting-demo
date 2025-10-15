import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("user_logs.csv", parse_dates=["timestamp"])

# Extract time features
df["hour"] = df["timestamp"].dt.hour
df["day"] = df["timestamp"].dt.date

# Define "night hours" roughly 0–6
df["is_night"] = df["hour"].apply(lambda h: 1 if 0 <= h < 6 else 0)

# Group by user and day — aggregate their behavior
features = df.groupby(["user", "day"]).agg(
    total_events=("event_type", "count"),
    unique_event_types=("event_type", "nunique"),
    unique_locations=("location", "nunique"),
    night_activity_ratio=("is_night", "mean"),
    logins=("event_type", lambda x: (x == "login").sum()),
    file_accesses=("event_type", lambda x: (x == "file_access").sum()),
    privileged_events=("event_type", lambda x: (x.isin(["privileged_access", "unauthorized_file"]).sum()))
).reset_index()

# Fill any NaN values with 0
features = features.fillna(0)

# Save features
features.to_csv("user_behavior_features.csv", index=False)

print("✅ Created behavior feature dataset:")
print(features.head(10))
