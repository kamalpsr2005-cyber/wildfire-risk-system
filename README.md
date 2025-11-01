# Wildfire Risk Monitoring System

**Status:** Rebuilding after SSD crash — started 2025-11-01.

## Overview
Full-stack system to predict and display wildfire risk using weather inputs. Backend (Flask) exposes REST APIs; frontend built with React.

## Tech stack
- Python, Flask
- React, Tailwind CSS
- scikit-learn (RandomForest)
- MySQL / SQLite (demo)

## How to run (local)
1. `python3 -m venv venv`  
2. `pip install -r requirements.txt`  
3. `python app.py`

## Next steps
- Implement model placeholder and API for predictions
- Add frontend form and connect to `/predict` endpoint
- Add unit tests and CI
