# dummy-mission-system

A Flask API that implements a subset of the [PIC NEPA Data Standard](https://github.com/GSA-TTS/pic-standards/blob/main/src/openapi/openapi.json).

## Overview

This application serves hardcoded data for three entities from the NEPA Data Standard:
- **Project**: Information about projects requiring NEPA review
- **Process Instance**: Details about specific environmental review processes
- **Process Decision Payload**: Decision data and evaluation results

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Start the Flask development server:
```bash
python app.py
```

The server will run on `http://localhost:5000`

## API Endpoints

### GET /
Root endpoint that returns API information and available endpoints.

**Response:**
```json
{
  "message": "Dummy Mission System API",
  "endpoints": {
    "/project": "Get project data",
    "/process_instance": "Get process instance data",
    "/process_decision_payload": "Get process decision payload data"
  }
}
```

### GET /project
Returns project data. Accepts optional `id` query parameter but always returns the same hardcoded data.

**Query Parameters:**
- `id` (optional): Project ID (accepted but ignored)

**Response:** Array of project objects matching the NEPA Data Standard schema

**Example:**
```bash
curl http://localhost:5000/project
curl http://localhost:5000/project?id=1
```

### GET /process_instance
Returns process instance data. Accepts optional `id` query parameter but always returns the same hardcoded data.

**Query Parameters:**
- `id` (optional): Process ID (accepted but ignored)

**Response:** Array of process instance objects matching the NEPA Data Standard schema

**Example:**
```bash
curl http://localhost:5000/process_instance
curl http://localhost:5000/process_instance?id=1
```

### GET /process_decision_payload
Returns process decision payload data. Accepts optional `id` query parameter but always returns the same hardcoded data.

**Query Parameters:**
- `id` (optional): Payload ID (accepted but ignored)

**Response:** Array of process decision payload objects matching the NEPA Data Standard schema

**Example:**
```bash
curl http://localhost:5000/process_decision_payload
curl http://localhost:5000/process_decision_payload?id=1
```

## Data Format

All endpoints return data conforming to the schemas defined in the [PIC NEPA Data Standard OpenAPI specification](https://github.com/GSA-TTS/pic-standards/blob/main/src/openapi/openapi.json).

## Note

This is a dummy/mock system. All endpoints return the same hardcoded data regardless of input parameters. The application accepts project IDs and other parameters to simulate a real API, but the response is always identical.