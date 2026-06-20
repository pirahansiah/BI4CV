"""BI Tools service — interactive tool buttons and function runner."""

from __future__ import annotations

import logging
import subprocess
import sys
from pathlib import Path

from flask import Flask, jsonify, render_template_string, request

app = Flask(__name__)
logger = logging.getLogger(__name__)

_BI_TOOLS_HTML = """\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BI Tools for Media Files</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 20px; background-color: #f4f4f9; }
        h1 { color: #333; }
        .button-container { display: flex; flex-direction: column; align-items: flex-start; }
        .button-container button {
            margin: 10px 0; padding: 15px 25px; font-size: 18px; font-weight: bold;
            color: #fff; background-color: #007BFF; border: none; border-radius: 8px;
            cursor: pointer; position: relative;
        }
        .button-container button:hover { background-color: #0056b3; }
        .button-container button:hover::after {
            content: attr(data-description); display: block; background-color: #f9f9f9;
            padding: 10px; border: 1px solid #ccc; border-radius: 5px; margin-top: 10px;
            font-size: 14px; color: #333; position: absolute; left: 105%; top: 50%;
            transform: translateY(-50%); white-space: nowrap;
        }
    </style>
</head>
<body>
    <h1>Business Intelligence Tools for Media Files (Images/Videos)</h1>
    <div class="button-container">
        <button data-description="Interactive Plotly visualizations and drill-down" onclick="window.open('http://localhost:5003/', '_blank')">Dashboard</button>
        <button data-description="Identify and count objects (cars, people)" onclick="runFunction('object_detection')">Object Detection and Recognition</button>
        <button data-description="Uncover movement patterns over time" onclick="runFunction('activity_tracking')">Activity Tracking</button>
        <button data-description="Classify scene types" onclick="runFunction('scene_understanding')">Scene Understanding</button>
        <button data-description="Count people present" onclick="runFunction('people_counting')">People Counting and Analytics</button>
        <button data-description="Identify unusual objects or activities" onclick="runFunction('anomalous_event_detection')">Anomalous Event Detection</button>
        <button data-description="Mood and sentiment from facial expressions" onclick="runFunction('additional_insights')">Additional Insights</button>
        <button data-description="Object counts, movement patterns, events" onclick="runFunction('metrics_and_kpis')">Metrics and KPIs</button>
        <button data-description="Trends, heatmaps, pie charts" onclick="runFunction('visualizations')">Visualizations</button>
        <button data-description="Trend analysis, anomaly detection, predictions" onclick="runFunction('insights_and_applications')">Insights and Applications</button>
    </div>
    <script>
        function runFunction(button_id) {
            fetch('/run_function', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({button_id: button_id}),
            })
            .then(r => r.json())
            .then(data => alert(data.message || data.error))
            .catch(err => console.error('Error:', err));
        }
    </script>
</body>
</html>
"""


@app.route("/")
def index() -> str:
    """Render the BI tools landing page."""
    return render_template_string(_BI_TOOLS_HTML)


@app.route("/run_function", methods=["POST"])
def run_function() -> tuple[dict[str, str], int]:
    """Execute a BI tool function by name."""
    data = request.get_json(silent=True)
    if data is None or "button_id" not in data:
        return jsonify(error="Missing button_id"), 400

    button_id: str = data["button_id"]
    script_dir = Path(__file__).resolve().parent
    app_file = script_dir / "bi2.py"

    if not app_file.exists():
        return jsonify(error=f"Script not found: {app_file.name}"), 404

    try:
        result = subprocess.run(
            [sys.executable, str(app_file)],
            capture_output=True,
            text=True,
            timeout=60,
        )
        if result.returncode == 0:
            return jsonify(message=f"Running {button_id}...\n{result.stdout}")
        return jsonify(error=f"Error running {button_id}: {result.stderr}"), 500
    except subprocess.TimeoutExpired:
        return jsonify(error=f"Timeout running {button_id}"), 504
    except Exception as exc:
        logger.exception("Unexpected error running %s", button_id)
        return jsonify(error=str(exc)), 500


if __name__ == "__main__":
    app.run(debug=True, port=5001)
