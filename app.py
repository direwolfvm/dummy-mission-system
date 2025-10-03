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
        "evaluation_data": {    {
        "top_level_key": "Test-2",
        "secondary_key": "BLM-MOAB-CE",
        "value": [
            {
                "name": "projectApprovedBy",
                "value": {
                    "value": "Sally Supervisor",
                    "comment": {
                        "comment": "",
                        "saved": false
                    }
                }
            },
            {
                "name": "projectLead",
                "value": {
                    "value": "Analyst Arthur",
                    "comment": {
                        "comment": "",
                        "saved": false
                    }
                }
            },
            {
                "name": "applicant",
                "value": {
                    "value": "Various, see attachment 3",
                    "comment": {
                        "comment": "",
                        "saved": false
                    }
                }
            },
            {
                "name": "accessNeeded",
                "value": {
                    "value": "None",
                    "comment": {
                        "comment": "",
                        "saved": false
                    }
                }
            },
            {
                "name": "typeOfAuthorization",
                "value": {
                    "value": "ROW",
                    "comment": {
                        "comment": "",
                        "saved": false
                    }
                }
            },
            {
                "name": "acresOfDisturbance",
                "value": {
                    "value": 0,
                    "comment": {
                        "comment": "",
                        "saved": false
                    }
                }
            },
            {
                "name": "specialManagementArea",
                "value": {
                    "value": "No",
                    "comment": {
                        "comment": "",
                        "saved": false
                    }
                }
            },
            {
                "name": "knownIssues",
                "value": {
                    "value": "None",
                    "comment": {
                        "comment": "",
                        "saved": false
                    }
                }
            },
            {
                "name": "surveyNeeds",
                "value": {
                    "value": "None",
                    "comment": {
                        "comment": "",
                        "saved": false
                    }
                }
            },
            {
                "name": "timelines_lengthOfProject",
                "value": {
                    "value": "2 months",
                    "comment": {
                        "comment": "",
                        "saved": false
                    }
                }
            },
            {
                "name": "projectName",
                "value": {
                    "value": "2025 Rights of Way Renewals and Assignments",
                    "comment": {
                        "comment": "",
                        "saved": false
                    }
                }
            },
            {
                "name": "description",
                "value": {
                    "value": "The Bureau of Land Management (BLM) Moab Field Office (MFO) has thirteen Rights of way  (ROWs) and one Land Use Permit (LUP) expiring between January 1, 2025 and December 31,  2025...",
                    "comment": {
                        "comment": "",
                        "saved": false
                    }
                }
            },
            {
                "name": "fieldOfficeName",
                "value": {
                    "value": "Moab Field Office",
                    "comment": {
                        "comment": "",
                        "saved": false
                    }
                }
            },
            {
                "name": "streetAddress",
                "value": {
                    "value": "82 East Dogwood Avenue",
                    "comment": {
                        "comment": "",
                        "saved": false
                    }
                }
            },
            {
                "name": "city",
                "value": {
                    "value": "Moab",
                    "comment": {
                        "comment": "",
                        "saved": false
                    }
                }
            },
            {
                "name": "state",
                "value": {
                    "value": "UT",
                    "comment": {
                        "comment": "",
                        "saved": false
                    }
                }
            },
            {
                "name": "zipCode",
                "value": {
                    "value": "84532",
                    "comment": {
                        "comment": "",
                        "saved": false
                    }
                }
            },
            {
                "name": "categoricalExclusionID",
                "value": {
                    "value": "DOI-BLM-UT-Y010-2025-0018-CX",
                    "comment": {
                        "comment": "",
                        "saved": false
                    }
                }
            },
            {
                "name": "locationOfProposedAction",
                "value": {
                    "value": "Moab Field Office",
                    "comment": {
                        "comment": "",
                        "saved": false
                    }
                }
            },
            {
                "name": "leaseSerialCaseFileNumber",
                "value": {
                    "value": "UTUT106105849, UTUT106264058, UTUT106250106, UTUT106133787, UTUT106102434, UTUT106251062, UTUT105866534, UTUT106247230, UTUT105864144, UTUT105864146, UTUT106247656, UTUT106156132 UTUT106180673, UTUT106094622",
                    "comment": {
                        "comment": "",
                        "saved": false
                    }
                }
            },
            {
                "name": "contactPerson",
                "value": {
                    "value": "Read Kennard",
                    "comment": {
                        "comment": "",
                        "saved": false
                    }
                }
            },
            {
                "name": "contactTitle",
                "value": {
                    "value": "Realty Specialist",
                    "comment": {
                        "comment": "",
                        "saved": false
                    }
                }
            },
            {
                "name": "officeName",
                "value": {
                    "value": "Moab Field Officer",
                    "comment": {
                        "comment": "",
                        "saved": false
                    }
                }
            },
            {
                "name": "mailingAddress",
                "value": {
                    "value": "82 E. Dogwood, Moab, Utah 84532",
                    "comment": {
                        "comment": "",
                        "saved": false
                    }
                }
            },
            {
                "name": "telephoneNumber",
                "value": {
                    "value": "435-259-2133",
                    "comment": {
                        "comment": "",
                        "saved": false
                    }
                }
            },
            {
                "name": "exclusion",
                "value": {
                    "value": "Renewals and assignments of leases, permits, or rights-of-way where no additional rights are conveyed beyond those granted by the original authorizations.",
                    "comment": {
                        "comment": "",
                        "saved": false
                    }
                }
            },
            {
                "name": "landUsePlanName",
                "value": {
                    "value": "Land Use Plan Name: Moab Field Office Record of Decision and Approved Resource Management Plan, as amended",
                    "comment": {
                        "comment": "",
                        "saved": false
                    }
                }
            },
            {
                "name": "dateApproved",
                "value": {
                    "value": "2016-12-15",
                    "comment": {
                        "comment": "",
                        "saved": false
                    }
                }
            },
            {
                "name": "conformanceOption",
                "value": {
                    "value": "specificallyProvided",
                    "comment": {
                        "comment": "",
                        "saved": false
                    }
                }
            },
            {
                "name": "lupDecisions",
                "value": {
                    "value": {
                        "value": {
                            "value": {
                                "value": {
                                    "value": {
                                        "value": "Goals and Objectives: Meet public needs for use authorization such as rights of way (ROWs)...",
                                        "comment": {
                                            "comment": "",
                                            "saved": false
                                        }
                                    },
                                    "comment": {
                                        "comment": "",
                                        "saved": false
                                    }
                                },
                                "comment": {
                                    "comment": "",
                                    "saved": false
                                }
                            },
                            "comment": {
                                "comment": "",
                                "saved": false
                            }
                        },
                        "comment": {
                            "comment": "",
                            "saved": false
                        }
                    },
                    "comment": {
                        "comment": "",
                        "saved": false
                    }
                }
            },
            {
                "name": "responsibleOfficial",
                "value": "David Pals"
            },
            {
                "name": "date",
                "value": "2025-02-24"
            },
            {
                "name": "moveonval",
                "value": "yes"
            },
            {
                "name": "publicHealthImpacts",
                "value": {
                    "value": "This category of action is not known to have impacts on public health and safety because it does not involve on-the-ground activities.",
                    "comment": {}
                }
            },
            {
                "name": "naturalResourcesImpacts",
                "value": {
                    "value": "The type of activity, as described in the Proposed Action, has no potential (i.e. no surface disturbance) to cause effects on cultural resources.\nThis category of action is not known to have impacts on park, recreation or refuge lands.\nThe this category of proposed action is not known to have impacts on Wilderness Areas.\nThis category of action is not known to have impacts on Wild or Scenic Rivers.\nThis category of action is not known to have impacts on National Natural Landmarks.\nThere are no aspects of the proposed action that will impact sole or principal drinking water aquifers.\nThis category of action is not known to have impacts on prime farmlands.\nThis category of action is not known to have impacts on wetlands.\nThis category of action is not known to have impacts on floodplains.\nThis category of action is not known to have impacts on national monuments.\nThis category of action is not known to have impacts on migratory birds.\nThis category of action is not known to have impacts on other unique resources.\nThe action does not have significant impacts on properties listed or eligible for listing on the National Register of Historic Places.",
                    "comment": {}
                }
            },
            {
                "name": "controversialEffects",
                "value": {
                    "value": "The impacts of the action are not highly uncertain and do not involve unique or unknown risks.",
                    "comment": {}
                }
            },
            {
                "name": "precedentForFutureAction",
                "value": {
                    "value": "The action does not establish a precedent for future action or represent a decision in principle about future actions with potentially significant environmental effects.",
                    "comment": {}
                }
            },
            {
                "name": "cumulativeImpacts",
                "value": {
                    "value": "The action does not have a direct relationship to other actions with individually insignificant but cumulatively significant environmental effects.",
                    "comment": {}
                }
            },
            {
                "name": "endangeredSpeciesImpacts",
                "value": null
            },
            {
                "name": "limitAccessToSacredSites",
                "value": {
                    "value": "The action will not limit access to or ceremonial use of Indian sacred sites.",
                    "comment": {}
                }
            },
            {
                "name": "promoteNoxiousWeeds",
                "value": {
                    "value": "The action will not contribute to the introduction, continued existence, or spread of noxious weeds or non-native invasive species.",
                    "comment": {}
                }
            },
            {
                "name": "categoricalExclusionJustification",
                "value": {
                    "value": "This categorical exclusion is appropriate in this situation because there are no extraordinary  circumstances potentially having effects that may significantly affect the environment. The  Proposed Action has been reviewed, and none of the extraordinary circumstances described in 43  CFR Part 46.215 apply.",
                    "comment": {}
                }
            }
        ]
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
