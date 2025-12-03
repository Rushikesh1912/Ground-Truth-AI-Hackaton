# 🚀 Automated Insight Engine (H-001)  
### Ground Truth Hackathon – Data Engineering & Analytics Track  
Author: Rushikesh Kadam

---

## 📌 Overview  
This project automates the entire reporting workflow for large datasets.  
It ingests data, analyzes it, generates visual insights, optionally adds an AI-based summary, and exports **PDF & PPT** reports automatically.  
A full **FastAPI backend** enables external apps, dashboards, or pipelines to trigger report generation.

---

## ✅ Features  
- **CSV Upload & Ingestion**  
- **Automated Data Cleaning**  
- **Exploratory Data Analysis** (genres, directors, ratings, trends)  
- **Visualization Outputs** (PNG charts)  
- **AI Executive Summary** (optional OpenAI API key)  
- **PDF Report Generation**  
- **PPT Report Generation**  
- **REST API with Swagger UI**

---

## 📂 Project Structure  
GT Hackaton/
├── data/ # Raw + ingested dataset
├── reports/ # Generated reports + charts
├── scripts/
│ ├── generate_report.py
│ ├── api_server.py
├── uploads/ # Uploaded CSVs
├── venv/
└── README.md

yaml
Copy code

---

## ⚙️ Setup Instructions  
### 1. Create Virtual Environment  
```bash
python -m venv venv
2. Activate (Windows PowerShell)
powershell
Copy code
.\venv\Scripts\Activate.ps1
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. (Optional) Enable AI Summary
powershell
Copy code
$env:OPENAI_API_KEY="your-key-here"
▶ Run Without API (Standalone Report)
bash
Copy code
python scripts/generate_report.py
Outputs:

reports/netflix_report.pdf

reports/netflix_report.pptx

🌐 Run API Server (Recommended for Hackathon)
bash
Copy code
uvicorn scripts.api_server:app --reload
Open Swagger UI:

arduino
Copy code
http://127.0.0.1:8000/docs
📡 API Endpoints
Method	Endpoint	Description
GET	/	API health check
POST	/upload	Upload CSV
POST	/ingest	Load dataset from path
POST	/analyze	Run analysis (plots + summary)
POST	/generate-report	Create PDF + PPT
GET	/get-report/pdf	Download PDF
GET	/get-report/pptx	Download PPT

🧠 AI Summary Example
"Drama, comedy, and international genres dominate the catalog, showing Netflix's global content strategy. Rating patterns suggest content aimed at teens and adults. Director distribution reflects a diverse creator pool. Overall, the dataset shows strong variety and broad audience targeting."

🛠 Tech Stack
Python

FastAPI

Pandas

Matplotlib / Seaborn

FPDF

python-pptx

OpenAI API (optional)

🎉 Final Notes
This project completes the H-001 challenge by combining data engineering, analytics, automation, AI insights, and API-driven reporting.
It is production-ready and suitable for real-world enterprise reporting workflows.


🏗️ System Architecture
                   ┌─────────────────────────┐
                   │         Client          │
                   │  (Swagger UI / API)     │
                   └─────────────┬───────────┘
                                 │
                                 ▼
                    ┌────────────────────────┐
                    │       FastAPI API      │
                    │ api_server.py          │
                    └─────────────┬──────────┘
                                  │
              ┌───────────────────┼──────────────────┐
              ▼                   ▼                  ▼
   ┌─────────────────┐   ┌─────────────────┐  ┌──────────────────┐
   │ Data Ingestion   │   │ Data Analysis   │  │ AI Summary (LLM) │
   │ CSV / Upload     │   │ Charts/EDA      │  │ Optional         │
   └─────────────────┘   └─────────────────┘  └──────────────────┘
                                  │
                                  ▼
                      ┌──────────────────────┐
                      │   Report Generator   │
                      │  PDF + PPT (fpdf &   │
                      │  python-pptx)        │
                      └──────────────────────┘
                                  │
                                  ▼
                       /reports/netflix_report.*
