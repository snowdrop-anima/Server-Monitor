from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import models, schemas
from database import SessionLocal, engine

# Create DB tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# API route for alert count
@app.get("/alerts/count", response_model=schemas.AlertCount)
def get_alert_count(db: Session = Depends(get_db)):
    critical = db.query(models.Alert).filter(models.Alert.severity.ilike('critical')).count()
    medium = db.query(models.Alert).filter(models.Alert.severity.ilike('medium')).count()
    low = db.query(models.Alert).filter(models.Alert.severity.ilike('low')).count()
    return {"critical": critical, "medium": medium, "low": low}

# Insert mock data ONCE at app startup
@app.on_event("startup")
def startup_event():
    from mock_data import insert_mock_data
    insert_mock_data()