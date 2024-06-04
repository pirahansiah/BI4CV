from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
        <html>
        <head>
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
        .button:hover {
            background-color: #0056b3;
        }
    </style>
        </head>
        <body>            
            <button class="button" onclick="window.open('http://localhost:5001/', '_blank')">List of BI Services</button>
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
        <li>Sentiment Analysis: Gauge the overall mood or feeling in an image based on facial expressions (positive, negative, neutral)</li>
        <li>Object Interactions: Identify how objects or people interact with each other in videos (e.g., person using a tool, car passing a pedestrian)</li>
    </ul>
    <h2>Metrics and KPIs</h2>
    <h3>Metrics</h3>
    <ul>
        <li>Object Detection Counts</li>
        <li>Activity Tracking</li>
        <li>Event Detection</li>
        <li>Demographic Analysis</li>
        <li>Motion Analysis</li>
        <li>Text Recognition</li>
        <li>Sentiment Analysis</li>
    </ul>
    <h3>Key Performance Indicators (KPIs)</h3>
    <ul>
        <li>Operational Efficiency</li>
        <li>Customer Engagement</li>
        <li>Safety and Security</li>
        <li>Sales and Marketing</li>
        <li>Brand Sentiment Analysis</li>
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
    <h2>Insights and Applications</h2>
    <ul>
        <li>Trend Analysis</li>
        <li>Anomaly Detection</li>
        <li>Predictive Analysis</li>
        <li>Optimization Suggestions</li>
        <li>Customer Behavior</li>
        <li>Competitor Analysis</li>
        <li>Marketing Effectiveness</li>
        <li>Operational Efficiency</li>
    </ul>
    <h2>Best Practices for BI Dashboard Display</h2>
    <ul>
        <li>Focus on Key Insights</li>
        <li>Interactive Visualizations</li>
        <li>Clear Labeling</li>
        <li>Filters and Sliders</li>
        <li>Storytelling Context</li>
        <li>Responsive Design</li>
        <li>Regular Updates</li>
    </ul>
    <h2>Enhance Dataset of Images/Videos</h2>
    <h3>Shadow and Overexposure Removal / Lighting Correction</h3>
    <ul>
        <li>Histogram Equalization</li>
        <li>Deep Learning Models</li>
        <li>Conditional GANs</li>
        <li>Lighting Transfer</li>
    </ul>
    <h3>Detecting Issues with Lighting</h3>
    <ul>
        <li>Image Quality Assessment</li>
        <li>Deep Learning</li>
        <li>Pre-trained Models</li>
    </ul>
    <h3>Keeping Biometric Integrity</h3>
    <ul>
        <li>Face Landmark Detection</li>
        <li>GANs with Biometric Constraints</li>
    </ul>
        </body>
        </html>
    ''')

if __name__ == '__main__':
    app.run(port=5000)
