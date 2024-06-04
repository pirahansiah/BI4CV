from flask import Flask, render_template_string, request, jsonify
import os
import subprocess

app = Flask(__name__)

# HTML template with buttons and descriptions
html_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BI Tools for Media Files</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f4f4f9;
        }
        h1 {
            color: #333;
        }
        .button-container {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
        }
        .button-container button {
            margin: 10px 0;
            padding: 15px 25px;
            font-size: 18px;
            font-weight: bold;
            color: #fff;
            background-color: #007BFF;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            position: relative;
        }
        .button-container button:hover {
            background-color: #0056b3;
        }
        .button-container button:hover::after {
            content: attr(data-description);
            display: block;
            background-color: #f9f9f9;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
            margin-top: 10px;
            font-size: 14px;
            color: #333;
            position: absolute;
            left: 105%;
            top: 50%;
            transform: translateY(-50%);
            white-space: nowrap;
        }
    </style>
</head>
<body>
    <h1>Business Intelligence Tools for Media Files (Images/Videos)</h1>
    <div class="button-container">
        <button data-description="Focus on Key Insights, Interactive Visualizations, Clear Labeling, and more" onclick="window.open('http://localhost:5003/', '_blank')">Dashboard</button>
        <button data-description="Identify and count specific objects (cars, people) within images/videos" onclick="runFunction('object_detection')">Object Detection and Recognition</button>
        <button data-description="Uncover movement patterns over time" onclick="runFunction('activity_tracking')">Activity Tracking</button>
        <button data-description="Classify scene types (indoor, outdoor, street scene, office)" onclick="runFunction('scene_understanding')">Scene Understanding</button>
        <button data-description="Count the number of people present" onclick="runFunction('people_counting')">People Counting and Analytics</button>
        <button data-description="Identify unusual objects, activities, or sudden movements" onclick="runFunction('anomalous_event_detection')">Anomalous Event Detection</button>
        <button data-description="Gauge the overall mood or feeling in an image based on facial expressions" onclick="runFunction('additional_insights')">Additional Insights</button>
        <button data-description="Object Detection Counts, Movement patterns, Event Detection, and more" onclick="runFunction('metrics_and_kpis')">Metrics and KPIs</button>
        <button data-description="Trends in object counts and events, Heatmaps, Pie Charts, and more" onclick="runFunction('visualizations')">Visualizations</button>
        <button data-description="Trend Analysis, Anomaly Detection, Predictive Analysis, and more" onclick="runFunction('insights_and_applications')">Insights and Applications</button>        
    </div>

    <script>
        function runFunction(button_id) {
            fetch('/run_function', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ button_id: button_id }),
            })
            .then(response => response.json())
            .then(data => alert(data.message))
            .catch(error => console.error('Error:', error));
        }
    </script>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(html_template)

@app.route('/run_function', methods=['POST'])
def run_function():
    data = request.get_json()
    button_id = data['button_id']
    
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        app_file_path = os.path.join(script_dir, 'bi2.py')
        result = subprocess.run(['python', app_file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            return jsonify(message=f'Running {button_id} Code...\n{result.stdout}')
        else:
            return jsonify(error=f'Error running {button_id} code: {result.stderr}')
    except subprocess.CalledProcessError as e:
        return jsonify(error=f'Error running {button_id} code: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
