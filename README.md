# Generative AI Business Intelligence Computer Vision (BI4CV)

Welcome to the BI4CV repository! This project is dedicated to revolutionizing the way businesses approach image and video dataset analysis. Our innovative Business Intelligence (BI) tools are designed to enhance storytelling and provide actionable insights for your media content.

Through advanced visualizations, interactive dashboards, and detailed reports, our system intelligently selects the optimal visual representations based on the diversity and complexity of your dataset. This approach simplifies the analytics process, making it accessible to users regardless of their technical expertise.

## What's New
I have updated the codebase to enhance the microservices architecture, allowing each service to run independently or all together. This approach facilitates better testing and flexibility. You can now run all services simply by executing the app.py file. The documentation has been expanded with more information about the tools, plans, and a to-do list. Each file is numbered for better sequence understanding.

- 1_main_service.py: Main Service Dashboard (Port 5000) - Enhanced with a new styled button for listing BI services, making it more visually appealing and user-friendly.
- 2_bi_tools.py: Business Intelligence Tools for Media Files (Port 5001) - Updated the HTML and CSS to improve the interface, added descriptions to buttons for better functionality, and made the layout more interactive and informative. It includes a list of buttons that navigate to respective services.
- 3_image_video_metadata_dashboard.py: Image/Video Metadata Dashboard (Port 5003) - Enhanced the dashboard with better visualizations using Plotly, improved layout and styling for better readability, and added interactive tabs for detailed insights into file metadata.
These updates streamline the development process and improve the user experience across all services.

## Use Cases 

### Move to AWS: Estimate Cost to Move Data into S3
- Analyze the total size of your media files (images/videos)
- Estimate the cost of transferring and storing the data in Amazon S3 based on AWS pricing
- Visualize the estimated costs over time, considering factors like data growth and retention policies

### Video Understanding on AWS: Estimate Cost of Running Docker Containers
- Determine the number of videos and their total size
- Estimate the processing time required based on video duration and complexity
- Calculate the cost of running Docker containers on Amazon Elastic Container Service (ECS) or Amazon Elastic Kubernetes Service (EKS) to process the videos
- Visualize the estimated costs based on different instance types and configurations

### Local Processing: Labeling, Querying Images/Videos
- Develop local tools or applications for manual or semi-automated labeling of media files
- Implement search and query capabilities to find specific images/videos based on labels, metadata, or content
- Track progress and productivity metrics for labeling and querying tasks

### Find Images/Videos Matching Specific Criteria
- Implement content-based image/video retrieval techniques to search for media files matching specific criteria (e.g., objects, scenes, activities)
- Visualize search results with thumbnails and relevant metadata
- Enable filtering and sorting options for efficient browsing and retrieval

### Anomaly Detection (e.g., Fire, Timing of Events)
- Develop anomaly detection models to identify unusual or potentially dangerous events in images/videos (e.g., fire, security incidents)
- Visualize detected anomalies on a timeline or heatmap, highlighting their location and severity
- Set up alerts and notifications for critical anomalies requiring immediate attention

### Comparison Data: Impact on Space, Processing Time, and Cost Estimation
- Compare the storage requirements, processing times, and costs associated with different media file formats and resolutions
- Visualize the trade-offs between file size, quality, and processing requirements
- Estimate the overall costs and resource requirements for various media processing scenarios

## Project Aim

Our aim is to develop a comprehensive suite of tools that leverage machine learning and local large language models (LLMs) to provide smart and intuitive BI dashboards for your image and video media content. These dashboards facilitate deeper insights into your datasets without requiring users to have technical experience in machine learning.

## Features

- **Advanced Visualization Tools**: Best-in-class tools for data visualization that make insights accessible and actionable.
- **Smart Dashboard Creation**: Utilize built-in ML-powered features to effortlessly create and customize BI dashboards.
- **Anomaly Detection**: Automatically detect and alert on anomalies, outliers, exceptions, and deviations in your data.
- **Local LLM Integration**: Leverage local LLMs for enhanced data storytelling and smarter BI dashboard creation.
- **User-Friendly Interface**: No prior technical knowledge of machine learning required to use the system.

## Getting Started

To get started with BI4CV, please follow the instructions below:

1. **Clone the Repository**:

`git clone https://github.com/yourusername/BI4CV.git`

2. **Navigate to the Project Directory**:

`cd BI4CV`

3. **Install Required Libraries** (if applicable):

`pip install -r requirements.txt`


## Usage

Here’s how you can start using BI4CV to create compelling data stories from your image and video datasets:
- Detail the step-by-step process for using the system.
- Include examples of commands or scripts to run.

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

- Email Gmail: pirahansiah
- [LinkedIn](https://www.linkedin.com/in/pirahansiah/)
- X: [@pirahansiah](https://x.com/pirahansiah)
- Project Link: [https://github.com/pirahansiah/BI4CV](https://github.com/pirahansiah/BI4CV)

## Community and Professional Networks
- [Google Scholar](https://scholar.google.com/citations?user=GvCEy4QAAAAJ&hl=en)
- [LinkedIn Group over 34K members](https://www.linkedin.com/groups/10320678/)
- [Facebook Group over 14K members](https://www.facebook.com/groups/computervisiondeeplearning)
- [Stack Overflow Profile](https://stackoverflow.com/users/3533188/farshid-pirahansiah)
- [Tiziran](https://www.tiziran.com/)
- [Website](https://pirahansiah.com/)

## Social Media and Content Sharing

- [Reddit](https://www.reddit.com/user/pirahansiah/)
- [Telegram](https://t.me/computer_vision_llm)
- [Mastodon](https://mastodon.social/@pirahansiah)
- [Instagram](https://www.instagram.com/computer_vision_deep_learning/)
- [WhatsApp Group](https://chat.whatsapp.com/COguUhOlNprFIjjaHTRppW)
- [TikTok](https://www.tiktok.com/@pirahansiah)
- [Medium Blog](https://medium.com/@pirahansiah)
- [YouTube Channel](https://www.youtube.com/@ComputerVisionDeepLearning)
- [GPT Store - Creator Profile](https://gptstore.ai/creators/user-bXM5WI8Cx4fppw1EEywZj2ZV)
- [Anaconda Cloud](https://anaconda.cloud/share/notebooks/b3402347-efbb-4a92-b754-fe8195b8ad63/overview)


![BI4CV](/BI4CV/BI4CV.png "BI4CV")
