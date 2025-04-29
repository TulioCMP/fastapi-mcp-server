# FastAPI NCM Attributes Tool

This application provides a FastAPI-based API for retrieving information about NCM (Nomenclatura Comum do Mercosul) codes and their associated attributes.

## Features

- Search for NCM codes by code or description
- Retrieve all attributes for a specific NCM code with their possible values
- RESTful API endpoints with proper documentation
- MCP server integration for AI interaction

## Database Structure

The application uses a PostgreSQL database with the following main tables:

- `ncm`: Contains NCM codes and descriptions
- `ncm_attributes`: Contains attributes associated with NCM codes
- `attribute`: Contains attribute definitions

## API Endpoints

### NCM Attributes

- `GET /ncm/{ncm_code}/attributes`: Get all attributes for a specific NCM code
- `GET /ncm/search?query={search_term}`: Search for NCM codes by code or description

### MCP Tools

- `get_ncm_attributes_tool`: MCP tool to get attributes for an NCM code

## Example Usage

```python
import requests

# Search for NCM codes
response = requests.get("http://localhost:8000/ncm/search?query=1234")
results = response.json()

# Get attributes for a specific NCM code
response = requests.get("http://localhost:8000/ncm/1234.56.78/attributes")
attributes = response.json()
```

## Architecture

The application follows a clean architecture with:

- **Models**: SQLAlchemy models representing database tables
- **Repositories**: Handle database operations
- **Services**: Implement business logic
- **Schemas**: Pydantic models for request/response validation
- **API Routes**: FastAPI endpoints for HTTP interaction

## Running the Application

```bash
# Run the application
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Access the API documentation
# Open in browser: http://localhost:8000/docs
``` # fastapi-mcp-server
# fastapi-mcp-server
