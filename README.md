# cloud_lab_4

Laboratory work 4 for the **Cloud Technologies** course. Implements a minimal HTTP API server in Python, built without any external web framework, and packaged into a Docker container for cloud deployment.

The project was completed as a lab assignment for the Cloud Technologies course — a practical task on building a lightweight containerized HTTP service using only Python's standard library, demonstrating how an application can be packaged and run consistently across different environments via Docker.

## Technology Stack

- **Python** (standard library `http.server`)
- **Docker**

## Functionality

- `GET /?name=<name>` — returns a JSON greeting for the given name (defaults to `Anonymous` if not provided)
- `POST /` — accepts a JSON body with a `name` field and returns a JSON confirmation message; returns an error message if the body is not valid JSON

## Project Structure

```
api/
├── __init__.py       # marks the api directory as a Python package
└── index.py           # HTTP server implementation (GET and POST handlers)
Dockerfile             # container build definition
```

## How to Run

### Locally

```bash
python -m api.index
```

The server starts on `http://0.0.0.0:8000`.

### With Docker

Build the image:

```bash
docker build -t cloud-lab-4 .
```

Run the container:

```bash
docker run -p 8000:8000 cloud-lab-4
```

## Example Requests

```bash
curl "http://localhost:8000/?name=Misha"

curl -X POST http://localhost:8000/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Misha"}'
```
