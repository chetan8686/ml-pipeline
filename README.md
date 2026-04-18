#### ML Model Pipeline with Atomic Promotion & FastAPI Serving
##### Overview

This project implements a small, reproducible end-to-end machine learning service that:

Trains a tabular ML model from CSV data

Validates incoming data

Evaluates new models against the current production model

Promotes a better model atomically

Serves predictions via a single FastAPI service

The service always serves the latest promoted production.

High-Level Architecture
CSV → Validate → Train → Evaluate → Promote → Serve

Key Design Principles

Simple and reproducible pipeline

Atomic model promotion (no partial updates)

Clear separation of pipeline and service layers

Production-style API contracts

Project Structure
ml-model-pipeline/
│
├── data/
│   └── sample.csv              # Input CSV data
│
├── models/
│   ├── candidate/              # Newly trained models
│   └── production/             # Currently promoted model
│       └── model.pkl
│
├── pipeline/
│   ├── ingest.py               # Load CSV data
│   ├── validate.py             # Data validation
│   ├── train.py                # Model training
│   ├── evaluate.py             # Model evaluation
│   └── promote.py              # Atomic promotion logic
│
├── service/
│   ├── app.py                  # FastAPI application
│   ├── model_loader.py         # Load production model
│   └── schemas.py              # API request/response schemas
│
├── run_pipeline.py             # Orchestrates full pipeline
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
└── .gitignore
