# Generative AI Business Intelligence Computer Vision (BI4CV)

![Python 3.10+](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.9+-5C3EE8?style=flat&logo=opencv&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-5.18+-3F4F75?style=flat&logo=plotly&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=flat&logo=docker&logoColor=white)

Welcome to the BI4CV repository — a comprehensive Business Intelligence platform for image and video dataset analysis using generative AI, local LLMs, and advanced ML-powered dashboards.

## Overview

BI4CV intelligently selects optimal visual representations based on dataset diversity and complexity, providing actionable insights through interactive dashboards, automated anomaly detection, and LLM-powered data storytelling.

## What's New (2025-2026)

- **Ollama Integration**: Local LLM inference via Ollama for privacy-first data storytelling (Llama 3.2, Phi-3, Mistral)
- **RAG-Enhanced Analytics**: Retrieval-Augmented Generation for contextual dataset insights
- **ONNX Runtime**: Model inference accelerated with ONNX Runtime 1.18+ for edge and CPU deployment
- **Multimodal LLM Support**: Vision-language models (GPT-4V, LLaVA, Florence-2) for automated image/video captioning and analysis
- **Semantic Search**: CLIP-based zero-shot image retrieval and content-based search
- **Async Microservices**: FastAPI-based async endpoints replacing Flask for higher throughput
- **Cloud-Native CI/CD**: GitHub Actions with automated Docker builds and multi-arch support
- **Quantized Models**: INT8/INT4 quantization via bitsandbytes and GGUF for local deployment

## Microservices Architecture

| Service | Port | Description |
|---------|------|-------------|
| `1_main_service.py` | 5000 | Main Service Dashboard — service discovery and routing |
| `2_bi_tools.py` | 5001 | BI Tools — dataset profiling, cost estimation, insights |
| `3_image_video_metadata_dashboard.py` | 5003 | Metadata Dashboard — Plotly visualizations, interactive tabs |

## Use Cases

### Move to AWS: Estimate Cost to Move Data into S3
- Analyze total size of media files (images/videos)
- Estimate cost of transferring and storing data in Amazon S3
- Visualize estimated costs over time with data growth projections

### Video Understanding on AWS: Estimate Docker Container Costs
- Determine video count and total size
- Estimate processing time based on duration and complexity
- Calculate costs for ECS/EKS container processing
- Visualize costs across instance types and configurations

### Local Processing: Labeling, Querying Images/Videos
- Semi-automated labeling with SAM-2 (Segment Anything Model 2) integration
- CLIP-based semantic search for content-based retrieval
- Track progress and productivity metrics

### Anomaly Detection
- YOLOv9/YOLO11-based real-time anomaly detection
- Temporal anomaly patterns with heatmap visualization
- Alert system for critical events (fire, security incidents)

### Comparison Data: Space, Processing Time, Cost
- Compare storage requirements across formats and resolutions
- Visualize trade-offs between file size, quality, and processing needs

## Tech Stack

| Category | Tools |
|----------|-------|
| **ML/DL** | PyTorch 2.x, Ultralytics YOLO11, ONNX Runtime, SAM-2 |
| **LLM** | Ollama (Llama 3.2, Phi-3), OpenAI API, LangChain |
| **Vision** | OpenCV 4.9+, CLIP, Florence-2, LLaVA |
| **Dashboard** | Plotly 5.x, Dash, Streamlit |
| **Backend** | FastAPI, Flask, Python 3.10+ |
| **Infrastructure** | Docker, GitHub Actions, AWS (S3, ECS, EKS) |
| **Data** | Pandas, NumPy, ChromaDB (vector store) |

## Getting Started

```bash
git clone https://github.com/pirahansiah/BI4CV.git
cd BI4CV
pip install -r requirements.txt

# Start all services
python app.py

# Or start individual services
python 1_main_service.py    # Port 5000
python 2_bi_tools.py        # Port 5001
python 3_image_video_metadata_dashboard.py  # Port 5003
```

### Quick Start with Docker

```bash
docker-compose up --build
```

## Key Features

- **Advanced Visualization**: Plotly/Dash interactive dashboards with drill-down capabilities
- **Smart Dashboard Creation**: ML-powered auto-layout and chart selection
- **Anomaly Detection**: Automated detection of outliers and deviations
- **Local LLM Integration**: Ollama-powered data storytelling without cloud dependency
- **RAG Pipeline**: ChromaDB + embeddings for contextual dataset Q&A
- **Zero-Shot Classification**: CLIP-based content categorization without labeled data
- **Quantized Inference**: GGUF/INT8 models for CPU and edge deployment

## Research References

- **SAM-2** (2024): Segment Anything Model 2 for video segmentation — [Meta AI](https://github.com/facebookresearch/segment-anything-2)
- **YOLO11** (2025): Ultralytics latest real-time object detection — [Ultralytics](https://github.com/ultralytics/ultralytics)
- **Florence-2** (2024): Microsoft's unified vision foundation model — [Microsoft Research](https://arxiv.org/abs/2311.06783)
- **CLIP** (2024): Contrastive Language-Image Pre-training for zero-shot retrieval — [OpenAI](https://github.com/openai/CLIP)
- **Ollama** (2025): Local LLM inference engine — [Ollama](https://ollama.com)
- **LLaVA** (2024): Visual Instruction Tuning — [Microsoft/University of Wisconsin](https://llava-vl.github.io)
- **RAG** (2024): Retrieval-Augmented Generation survey — [Lewis et al.](https://arxiv.org/abs/2005.11401)

## Contributing

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

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

## Social Media

- [Reddit](https://www.reddit.com/user/pirahansiah/)
- [Telegram](https://t.me/computer_vision_llm)
- [YouTube Channel](https://www.youtube.com/@ComputerVisionDeepLearning)
- [Medium Blog](https://medium.com/@pirahansiah)

![BI4CV](/BI4CV/BI4CV.png "BI4CV")
