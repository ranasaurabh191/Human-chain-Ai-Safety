# A script to populate the database with sample incidents.
from app import app, db, Incident
from datetime import datetime

def init_db():
    with app.app_context():
        # Create tables
        db.create_all()

        # Check if incidents already exist
        if Incident.query.count() == 0:
            # Add sample incidents
            sample_incidents = [
                Incident(
                    title="Unexpected AI Behavior",
                    description="AI model generated inappropriate content during testing.",
                    severity="Medium",
                    reported_at=datetime.utcnow()
                ),
                Incident(
                    title="Data Leakage",
                    description="Sensitive user data was exposed due to misconfiguration.",
                    severity="High",
                    reported_at=datetime.utcnow()
                ),
                Incident(
                    title="Minor Processing Delay",
                    description="AI inference took longer than expected under heavy load.",
                    severity="Low",
                    reported_at=datetime.utcnow()
                )
            ]
            db.session.bulk_save_objects(sample_incidents)
            db.session.commit()
            print("Database initialized with sample incidents.")
        else:
            print("Database already contains incidents.")

if __name__ == '__main__':
    init_db()