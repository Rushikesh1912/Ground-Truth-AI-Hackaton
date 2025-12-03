# scripts/api_server.py

import os
import shutil
from pathlib import Path
from typing import Optional, Literal

from fastapi import FastAPI, UploadFile, File, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse

from scripts.generate_report import run_report, DATA_DIR, REPORTS_DIR

BASE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = BASE_DIR.parent
UPLOADS_DIR = PROJECT_DIR / "uploads"

UPLOADS_DIR.mkdir(parents=True, exist_ok=True)

app = FastAPI(
    title="Automated Insight Engine API",
    version="1.0.0",
    description="Ground Truth Hackathon - H-001 Automated Insight Engine",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Automated Insight Engine API is running."}


# ---------------------------
# /upload  → upload CSV file
# ---------------------------
@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    ext = os.path.splitext(file.filename)[1].lower()
    if ext != ".csv":
        raise HTTPException(status_code=400, detail="Only CSV files are supported for now.")

    dest_path = UPLOADS_DIR / file.filename
    with dest_path.open("wb") as f:
        shutil.copyfileobj(file.file, f)

    # Also store as current_dataset.csv in data/ to be used by run_report()
    current_dataset_path = Path(DATA_DIR) / "current_dataset.csv"
    shutil.copy(dest_path, current_dataset_path)

    return {
        "message": "File uploaded successfully.",
        "uploaded_path": str(dest_path),
        "current_dataset": str(current_dataset_path),
    }


# ---------------------------
# /ingest → ingest from server path (CSV)
# ---------------------------
@app.post("/ingest")
async def ingest(
    path: str = Query(..., description="Server-side path to CSV to ingest"),
):
    csv_path = Path(path)
    if not csv_path.exists():
        raise HTTPException(status_code=404, detail=f"File not found: {csv_path}")

    # Copy into data/current_dataset.csv
    current_dataset_path = Path(DATA_DIR) / "current_dataset.csv"
    shutil.copy(csv_path, current_dataset_path)

    # Optionally, we can load it to count rows
    import pandas as pd
    df = pd.read_csv(current_dataset_path)

    return {
        "message": "Ingestion successful.",
        "rows": len(df),
        "current_dataset": str(current_dataset_path),
    }


# ---------------------------
# /analyze → run analysis only
# ---------------------------
@app.post("/analyze")
async def analyze(
    source: Optional[str] = Query(
        None,
        description="Optional CSV path; if not provided, uses data/current_dataset.csv or data/netflix_titles.csv",
    )
):
    try:
        result = run_report(csv_path=source, generate_files=False)
        return {
            "message": "Analysis completed.",
            "csv_path": result["csv_path"],
            "plots": result["plots"],
            "ai_summary": result["ai_summary"],
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ---------------------------
# /generate-report → full pipeline (PDF + PPT)
# ---------------------------
@app.post("/generate-report")
async def generate_report(
    source: Optional[str] = Query(
        None,
        description="Optional CSV path; if not provided, uses data/current_dataset.csv or data/netflix_titles.csv",
    )
):
    try:
        result = run_report(csv_path=source, generate_files=True)
        return {
            "message": "Report generated successfully.",
            "csv_path": result["csv_path"],
            "pdf_file": result["pdf_file"],
            "ppt_file": result["ppt_file"],
            "ai_summary": result["ai_summary"],
            "plots": result["plots"],
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ---------------------------
# /get-report/{report_type} → download PDF/PPT
# ---------------------------
@app.get("/get-report/{report_type}")
async def get_report(report_type: Literal["pdf", "pptx"]):
    if report_type == "pdf":
        path = Path(REPORTS_DIR) / "netflix_report.pdf"
        media_type = "application/pdf"
    else:
        path = Path(REPORTS_DIR) / "netflix_report.pptx"
        media_type = "application/vnd.openxmlformats-officedocument.presentationml.presentation"

    if not path.exists():
        raise HTTPException(status_code=404, detail=f"{report_type.upper()} report not found. Generate it first.")

    return FileResponse(str(path), filename=path.name, media_type=media_type)
