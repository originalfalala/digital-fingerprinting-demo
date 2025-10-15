import pandas as pd
from sklearn.ensemble import IsolationForest

# Load the behavior features we created
df = pd.read_csv("user_behavior_features.csv")

# Keep a copy of identifying columns
meta_cols = ["user", "day"]
features = df.drop(columns=meta_cols)

# Train an Isolation Forest model
model = IsolationForest(
    contamination=0.05,  # expected proportion of anomalies
    random_state=42
)
model.fit(features)

# Get anomaly scores and predictions
df["anomaly_score"] = model.decision_function(features)
df["is_anomaly"] = model.predict(features)

# In IsolationForest, anomalies are marked as -1
df["is_anomaly"] = df["is_anomaly"].apply(lambda x: 1 if x == -1 else 0)

# Show potential anomalies
anomalies = df[df["is_anomaly"] == 1]

print("✅ Model trained and anomalies detected!")
print(f"🔎 Total days analyzed: {len(df)}")
print(f"⚠️ Potential anomalies detected: {len(anomalies)}\n")

print("📋 Example anomalies:")
print(anomalies.head(10))

# Save results
df.to_csv("anomaly_results.csv", index=False)
print("💾 Saved results to anomaly_results.csv")


