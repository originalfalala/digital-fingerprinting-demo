import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

# Load data
df = pd.read_csv("anomaly_results.csv")

# Create a scatter plot
fig = px.scatter(
    df,
    x="day",
    y="anomaly_score",
    color="user",
    symbol="is_anomaly",
    size="total_events",
    hover_data=["user", "total_events", "privileged_events"],
    title="User Anomaly Scores Over Time"
)

# Initialize Dash app
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Anomaly Detection Dashboard", style={"textAlign": "center"}),
    html.P("This dashboard shows user activity patterns and detected anomalies."),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)


