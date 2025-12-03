Automated Insight Engine (H-001) – Data Engineering & Analytics Track
1. Overview

This project is an end-to-end Automated Insight Engine built for the Ground Truth AI Hackathon (Track H-001).
It ingests data from multiple sources, performs analytics, generates AI-powered insights, and produces professional PDF and PowerPoint reports automatically.

The system is fully automated and requires no manual steps once triggered.

2. Features
2.1 Multi-Source Data Ingestion

CSV ingestion

JSON ingestion

SQL database support (MySQL, PostgreSQL, SQLite)

API JSON ingestion via POST request

2.2 Data Cleaning & Transformation

Handles missing values

Extracts duration values

Normalizes text columns

Splits multi-valued fields

Creates engineered features

Fully automated preprocessing pipeline

2.3 Analytics Layer

Automatically generates:

Top genres

Top directors

Ratings distribution

Titles per year

Average movie duration

Type distribution (Movie / TV Show)

Trend analysis

2.4 AI Insight Engine

Using OpenAI GPT-4o Mini for:

Executive-level summaries

Trend interpretation

Outlier detection

Content insights

Narrative generation for reports

2.5 Automated Report Generation

Produces two professional formats:

PDF Report

PowerPoint Report

Both include:

All generated charts

Textual insights

AI-generated summaries

Clean formatting

2.6 REST API Layer (FastAPI)

Endpoints:

/upload

/ingest

/analyze

/generate-report

/get-report/{type}

Interactive API docs available at:

http://127.0.0.1:8000/docs

3. Project Structure
GT-Hackaton/
│
├── data/
│   └── netflix_titles.csv
│
├── notebooks/
│   └── H001_notebook.ipynb
│
├── reports/
│   ├── netflix_report.pdf
│   ├── netflix_report.pptx
│   ├── top_genres.png
│   ├── top_directors.png
│   ├── rating_distribution.png
│   ├── titles_per_year.png
│   ├── type_count.png
│   ├── avg_movie_duration.png
│
├── scripts/
│   ├── generate_report.py
│   ├── load_data.py
│   ├── analyze.py
│   ├── api_server.py
│
├── venv/
│
├── requirements.txt
│
└── README.md

4. Installation
Step 1: Clone Repository
git clone <your-repository-url>
cd GT-Hackaton

Step 2: Create Virtual Environment

Windows

python -m venv venv
venv\Scripts\Activate.ps1


Mac/Linux

python3 -m venv venv
source venv/bin/activate

Step 3: Install Dependencies
pip install -r requirements.txt

5. Usage
Option A: Generate Complete Report

Run:

python scripts/generate_report.py


Outputs generated:

reports/netflix_report.pdf

reports/netflix_report.pptx

Option B: Run API Server
uvicorn scripts.api_server:app --reload


Open API documentation:

http://127.0.0.1:8000/docs

6. API Endpoints
Method	Endpoint	Description
POST	/upload	Upload CSV/JSON
POST	/ingest	Ingest and clean data
POST	/analyze	Run analytics and generate charts
POST	/generate-report	Produce PDF & PPT
GET	/get-report/{type}	Download final reports
7. Example AI Executive Insight

Automatically generated insight included in PDF and PPT:

Drama and International TV Shows are the most dominant content types, indicating strong global content diversity. Ratings are concentrated in TV-MA and TV-14 categories, showing a preference toward mature audience content. Content production increases significantly after 2015, reflecting Netflix’s investment in original programming. Directors are widely distributed, highlighting diverse creative partnerships.

8. Technologies Used
Backend

Python

Pandas

Matplotlib

Seaborn

FastAPI

Reporting

FPDF

python-pptx

AI

OpenAI GPT-4o Mini

9. Why This Project Meets H-001 Requirements
Hackathon Requirement	Implementation
Automated Ingestion	CSV, JSON, SQL ingest
Report Generation	PDF + PPT fully automated
AI Integration	GPT-4o insights
Data Engineering	Cleaning, transformation, analytics
API Pipeline	FastAPI endpoints
Scalability	Modular folder architecture
No Manual Work	One-click / one-API automation
10. Author

Rushikesh V. Kadam
B.Tech Artificial Intelligence & Data Science
GitHub: https://github.com/Rushikesh1912

Email: rushikadam1912@gmail.com