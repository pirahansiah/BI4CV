"""Main service dashboard — landing page and service discovery."""

from __future__ import annotations

from flask import Flask, render_template_string

app = Flask(__name__)

_HOME_HTML = """\
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Main Service: Business Intelligence Tools for Media Files</title>
    <style>
        .button {
            font-size: 20px;
            font-weight: bold;
            color: white;
            background-color: #007BFF;
            border: none;
            padding: 15px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 12px;
        }
        .button:hover { background-color: #0056b3; }
    </style>
</head>
<body>
    <button class="button" onclick="window.open('http://localhost:5001/', '_blank')">
        List of BI Services
    </button>
    <h1>Business Intelligence Tools for Media Files</h1>
    <h2>Object Detection and Recognition</h2>
    <ul>
        <li>Identify and count specific objects (cars, people) within images/videos</li>
        <li>Analyze object attributes like color, size, and brand (if applicable)</li>
        <li>Track object frequency and distribution</li>
    </ul>
    <h2>Activity Tracking</h2>
    <ul>
        <li>Uncover movement patterns over time</li>
        <li>Generate heatmaps to visualize areas of high activity</li>
        <li>Identify and track specific activities (running, fighting, interacting)</li>
    </ul>
    <h2>Scene Understanding</h2>
    <ul>
        <li>Classify scene types (indoor, outdoor, street scene, office)</li>
        <li>Extract dominant colors and identify prevalent objects</li>
        <li>Analyze the overall composition of the scene</li>
    </ul>
    <h2>People Counting and Analytics</h2>
    <ul>
        <li>Count the number of people present</li>
        <li>Estimate demographics (age, gender - if applicable)</li>
        <li>Track people's location within the scene</li>
        <li>Calculate occupancy rates and peak traffic times</li>
    </ul>
    <h2>Anomalous Event Detection</h2>
    <ul>
        <li>Identify unusual objects, activities, or sudden movements</li>
        <li>Track the frequency and type of anomalies detected</li>
        <li>Enable timely responses to potential security incidents</li>
    </ul>
    <h2>Additional Insights</h2>
    <ul>
        <li>Sentiment Analysis: Gauge mood based on facial expressions</li>
        <li>Object Interactions: Identify how objects/people interact</li>
    </ul>
    <h2>Metrics and KPIs</h2>
    <ul>
        <li>Object Detection Counts</li>
        <li>Activity Tracking</li>
        <li>Event Detection</li>
        <li>Demographic Analysis</li>
        <li>Motion Analysis</li>
        <li>Text Recognition</li>
        <li>Sentiment Analysis</li>
    </ul>
    <h2>Visualizations</h2>
    <ul>
        <li>Bar and Line Charts</li>
        <li>Heatmaps</li>
        <li>Pie Charts</li>
        <li>Scatter Plots</li>
        <li>Dashboards</li>
        <li>Word Clouds</li>
        <li>Histograms</li>
        <li>Timelines</li>
        <li>Video Snippets</li>
    </ul>
</body>
</html>
"""


@app.route("/")
def home() -> str:
    """Render the main landing page."""
    return render_template_string(_HOME_HTML)


if __name__ == "__main__":
    app.run(port=5000)
