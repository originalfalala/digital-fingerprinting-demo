# digital-fingerprinting-demo
Digital Fingerprinting for Anomaly Detection

This project demonstrates how to simulate and detect user behavior anomalies using digital fingerprinting techniques. It analyzes daily event logs to identify suspicious or irregular activities — such as unusual login counts, abnormal event types, or privilege escalations — which could indicate potential insider threats or system misuse.

🔍 Features

Event Log Simulation — Generates realistic user activity data (logins, logouts, privileged actions, etc.)

Machine Learning Model — Uses Isolation Forest to identify unusual user behavior patterns

Anomaly Detection — Flags users and dates with high anomaly scores

Interactive Dashboard — Built with Plotly Dash for exploring anomalies visually

Lightweight & Local — Runs entirely on your machine without GPU or cloud dependencies

⚙️ Tech Stack

Python 3.13

scikit-learn — for anomaly detection

pandas / numpy — for data processing

plotly-dash — for interactive visualization

Jupyter / VSCode — for analysis and testing

🚀 Usage

Clone the repository:

git clone https://github.com/originalfalala/digital-fingerprinting-demo.git
cd digital-fingerprinting-demo


Install dependencies:

pip install -r requirements.txt


Generate sample data:

python generate_logs.py

quick inspection of user_logs.csv:

python explore_logs.py

convert logs:

python create_features.py

Train model & detect anomalies:

python detect_anomalies.py

simple matplotlib scatter plot of anomaly scores (static):

python visualize_anomalies.py

Launch dashboard:

python dashboard.py


Open your browser at http://127.0.0.1:8050 to explore.

📊 Example Output
✅ Model trained and anomalies detected!
🔎 Total days analyzed: 10
⚠️ Potential anomalies detected: 1

🧩 Future Improvements

Add user authentication for secure dashboard access

Incorporate real-time log streaming (e.g., from syslog or API feeds)

Experiment with deep learning-based anomaly models (autoencoders, LSTM)

Extend the dashboard to show trend graphs and correlations

📘 Author

Arthur Lobowicz
Computer Science & Cybersecurity Student
Grambling State University