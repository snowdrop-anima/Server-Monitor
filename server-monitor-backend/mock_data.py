from sqlalchemy.orm import Session
from database import SessionLocal
from models import Alert

def insert_mock_data():
    db: Session = SessionLocal()
    if db.query(Alert).count() == 0:  # Avoid duplicate inserts
        alerts = [
            Alert(severity="critical", message="CPU usage very high"),
            Alert(severity="medium", message="Disk nearing capacity"),
            Alert(severity="low", message="RAM usage slightly elevated"),
            Alert(severity="critical", message="Memory leak detected"),
            Alert(severity="medium", message="Network latency increased"),
        ]
        db.add_all(alerts)
        db.commit()
    db.close()