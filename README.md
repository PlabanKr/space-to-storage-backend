# Space to Storage

## Overview
Space to Storage is a comprehensive web application built with Next.js for the frontend and FastAPI for the backend. The primary goal of this project is to provide farmers with tools and features to optimize ground elevation, manage water storage, and enhance overall agricultural efficiency.

## Features
- **Ground Elevation Analysis:** Gain insights into the topography of your agricultural land to make informed decisions about crop selection, irrigation planning, and drainage.

## Getting Started

### Prerequisites

- Python (https://www.python.org/)

### Installation

1. Clone the repository:
```bash
    git clone https://github.com/PlabanKr/space-to-storage-backend
    cd space-to-storage-backend
```
2. Install Dependencies
```bash
    pip install -r requirements.txt
```

### Configuration

### Running the Application (development)
1. Start the backend:
```bash
    uvicorn app.main:app --reload
```

2. Check the running status of the backend app by hitting the following route:
```bash
    http://127.0.0.1:8000/health
```

## License

This project is under the [MIT License](LICENSE).