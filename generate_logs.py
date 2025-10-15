import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Parameters
users = ["alice", "bob", "charlie"]
event_types = ["login", "logout", "file_access", "config_change", "download"]
locations = ["US", "EU", "ASIA"]

# Generate 500 fake log records
rows = []
start_time = datetime.now() - timedelta(days=3)

for i in range(500):
    user = random.choice(users)
    event = random.choices(
        event_types, weights=[0.4, 0.3, 0.2, 0.05, 0.05]
    )[0]  # login more frequent
    location = random.choices(locations, weights=[0.6, 0.3, 0.1])[0]
    timestamp = start_time + timedelta(minutes=random.randint(0, 3 * 24 * 60))
    rows.append([timestamp, user, event, location])

# Convert to DataFrame
df = pd.DataFrame(rows, columns=["timestamp", "user", "event_type", "location"])

# Inject anomalies (weird behavior)
anomalies = []
for i in range(10):
    user = random.choice(users)
    timestamp = start_time + timedelta(minutes=random.randint(0, 3 * 24 * 60))
    # Unusual location or rare event
    event = random.choice(["privileged_access", "unauthorized_file"])
    location = random.choice(["RU", "CN"])
    anomalies.append([timestamp, user, event, location])

df = pd.concat([df, pd.DataFrame(anomalies, columns=df.columns)], ignore_index=True)

# Sort by timestamp and save
df = df.sort_values(by="timestamp")
df.to_csv("user_logs.csv", index=False)

print("✅ Generated dataset saved as user_logs.csv")
print(df.head(10))
