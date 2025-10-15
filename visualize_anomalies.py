import pandas as pd
import matplotlib.pyplot as plt

# Load the anomaly detection output
df = pd.read_csv("anomaly_results.csv")

# Plot
plt.figure(figsize=(10, 5))
for user in df["user"].unique():
    user_data = df[df["user"] == user]
    plt.scatter(user_data["day"], user_data["anomaly_score"], label=user)

# Highlight anomalies
anomalies = df[df["is_anomaly"] == 1]
plt.scatter(anomalies["day"], anomalies["anomaly_score"], color="red", marker="x", s=100, label="Anomalies")

plt.title("Anomaly Scores per User Over Time")
plt.xlabel("Day")
plt.ylabel("Anomaly Score")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
