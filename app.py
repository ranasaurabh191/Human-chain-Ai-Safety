# The Flask application with all required API endpoints, configured for MySQL.
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from models import db, Incident
import os

app = Flask(__name__)

# Configure MySQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3306/humanchain'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db.init_app(app)

# Allowed severity levels
ALLOWED_SEVERITIES = ['Low', 'Medium', 'High']

@app.route('/')
def index():
    return jsonify({"message": "Welcome to the HumanChain AI Safety Incident Reporting API!"}), 200

@app.route('/incidents', methods=['GET'])
def get_all_incidents():
    incidents = Incident.query.all()
    return jsonify([
        {
            'id': incident.id,
            'title': incident.title,
            'description': incident.description,
            'severity': incident.severity,
            'reported_at': incident.reported_at.isoformat()
        } for incident in incidents
    ]), 200

@app.route('/incidents', methods=['POST'])
def create_incident():
    data = request.get_json()
    
    # Validate required fields
    if not data:
        return jsonify({'error': 'Request body must be JSON'}), 400
    if not all(key in data for key in ['title', 'description', 'severity']):
        return jsonify({'error': 'Missing required fields: title, description, severity'}), 400
    if not isinstance(data['title'], str) or not data['title'].strip():
        return jsonify({'error': 'Title must be a non-empty string'}), 400
    if not isinstance(data['description'], str) or not data['description'].strip():
        return jsonify({'error': 'Description must be a non-empty string'}), 400
    if data['severity'] not in ALLOWED_SEVERITIES:
        return jsonify({'error': f'Severity must be one of {ALLOWED_SEVERITIES}'}), 400

    # Create new incident
    incident = Incident(
        title=data['title'],
        description=data['description'],
        severity=data['severity'],
        reported_at=datetime.utcnow()
    )
    db.session.add(incident)
    db.session.commit()

    return jsonify({
        'id': incident.id,
        'title': incident.title,
        'description': incident.description,
        'severity': incident.severity,
        'reported_at': incident.reported_at.isoformat()
    }), 201

@app.route('/incidents/<int:id>', methods=['GET'])
def get_incident(id):
    incident = Incident.query.get(id)
    if not incident:
        return jsonify({'error': 'Incident not found'}), 404
    return jsonify({
        'id': incident.id,
        'title': incident.title,
        'description': incident.description,
        'severity': incident.severity,
        'reported_at': incident.reported_at.isoformat()
    }), 200

@app.route('/incidents/<int:id>', methods=['DELETE'])
def delete_incident(id):
    incident = Incident.query.get(id)
    if not incident:
        return jsonify({'error': 'Incident not found'}), 404
    db.session.delete(incident)
    db.session.commit()
    return jsonify({'message': 'Deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)