from flask import Flask, jsonify, request

app = Flask(__name__)

# Hardcoded project data matching the OpenAPI schema
PROJECT_DATA = [
    {
        "id": 1,
        "created_at": "2024-01-01T00:00:00Z",
        "title": "Highway Expansion Project",
        "description": "Major highway expansion to reduce traffic congestion",
        "sector": "transportation",
        "lead_agency": "Department of Transportation",
        "participating_agencies": "Environmental Protection Agency, Federal Highway Administration",
        "location_lat": 38.9072,
        "location_lon": -77.0369,
        "location_text": "Washington, DC",
        "type": "highway",
        "funding": "Federal appropriated funds",
        "start_date": "2024-01-15",
        "current_status": "underway",
        "sponsor": "State DOT",
        "sponsor_contact": {
            "name": "John Smith",
            "email": "john.smith@state.gov",
            "phone": "555-0100"
        },
        "parent_project_id": None,
        "other": {},
        "record_owner_agency": "Department of Transportation",
        "data_source_agency": "Department of Transportation",
        "data_source_system": "NEPA System",
        "data_record_version": "1.0",
        "last_updated": "2024-01-15T10:00:00Z",
        "retrieved_timestamp": "2024-01-20T15:30:00Z"
    }
]

# Hardcoded process instance data
PROCESS_INSTANCE_DATA = [
    {
        "id": 1,
        "parent_project_id": 1,
        "created_at": "2024-01-01T00:00:00Z",
        "parent_process_id": None,
        "agency_id": "DOT-2024-001",
        "federal_id": "FED-NEPA-2024-001",
        "type": "Environmental Impact Statement",
        "status": "underway",
        "stage": "scoping",
        "start_date": "2024-01-15",
        "complete_date": None,
        "outcome": None,
        "comment_start": "2024-02-01",
        "comment_end": "2024-03-01",
        "lead_agency": "Department of Transportation",
        "joint_lead_agency": None,
        "cooperating_agencies": "EPA",
        "participating_agencies": "Federal Highway Administration",
        "notes": "Initial scoping phase underway",
        "process_model": None,
        "purpose_need": "Reduce traffic congestion and improve highway safety",
        "description": "Comprehensive environmental review for highway expansion",
        "other": {},
        "record_owner_agency": "Department of Transportation",
        "data_source_agency": "Department of Transportation",
        "data_source_system": "NEPA System",
        "data_record_version": "1.0",
        "last_updated": "2024-01-15T10:00:00Z",
        "retrieved_timestamp": "2024-01-20T15:30:00Z",
        "process_code": "EIS-001"
    }
]

# Hardcoded process decision payload data
PROCESS_DECISION_PAYLOAD_DATA = [
    {
        "id": 1,
        "created_at": "2024-01-01T00:00:00Z",
        "process_decision_element": 1,
        "process": 1,
        "project": 1,
        "data_description": "Traffic impact analysis completed",
        "evaluation_data": {
            "traffic_volume": 50000,
            "peak_hours": "7-9am, 4-7pm",
            "congestion_level": "high"
        },
        "response": "Approved for next phase",
        "result": "positive",
        "result_bool": True,
        "result_notes": "Traffic analysis shows significant need for expansion",
        "result_data": {
            "recommendation": "proceed",
            "conditions": ["additional environmental monitoring", "traffic management plan"]
        },
        "result_source": "Traffic Engineering Team",
        "parent_payload": None,
        "data_annotation": "Based on 2023 traffic data",
        "evaluation_data_annotation": {
            "methodology": "standard traffic impact assessment",
            "data_quality": "high"
        },
        "other": {},
        "record_owner_agency": "Department of Transportation",
        "data_source_agency": "Department of Transportation",
        "data_source_system": "NEPA System",
        "data_record_version": "1.0",
        "last_updated": "2024-01-15T10:00:00Z",
        "retrieved_timestamp": "2024-01-20T15:30:00Z"
    }
]


@app.route('/project', methods=['GET'])
def get_project():
    """Get project data. Accepts optional 'id' parameter but always returns the same hardcoded data."""
    project_id = request.args.get('id', type=int)
    # Note: We accept the project_id parameter but always return the same data as specified
    return jsonify(PROJECT_DATA), 200


@app.route('/process_instance', methods=['GET'])
def get_process_instance():
    """Get process instance data. Accepts optional 'id' parameter but always returns the same hardcoded data."""
    process_id = request.args.get('id', type=int)
    # Note: We accept the process_id parameter but always return the same data as specified
    return jsonify(PROCESS_INSTANCE_DATA), 200


@app.route('/process_decision_payload', methods=['GET'])
def get_process_decision_payload():
    """Get process decision payload data. Accepts optional 'id' parameter but always returns the same hardcoded data."""
    payload_id = request.args.get('id', type=int)
    # Note: We accept the payload_id parameter but always return the same data as specified
    return jsonify(PROCESS_DECISION_PAYLOAD_DATA), 200


@app.route('/', methods=['GET'])
def index():
    """Root endpoint with API information."""
    return jsonify({
        "message": "Dummy Mission System API",
        "endpoints": {
            "/project": "Get project data",
            "/process_instance": "Get process instance data",
            "/process_decision_payload": "Get process decision payload data"
        }
    }), 200


@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
