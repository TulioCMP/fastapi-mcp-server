from fastapi import FastAPI, HTTPException, Query, Depends
from typing import List
from sqlalchemy.orm import Session
import pandas as pd
from app.database.config import get_db
from pydantic import SkipValidation
import json
import re


# Import the NCM attribute service and schemas
from app.services.ncm_attribute_service import NcmAttributeService
from app.repositories.ncm_attribute_repository import NcmAttributeRepository
from app.schemas.ncm_attribute import NcmAttributeList, NcmSearchResults

from fastapi_mcp import add_mcp_server

app = FastAPI(
    title="NCM Attributes API",
    description="An API for retrieving NCM attributes and their possible values",
    version="0.1.0",
)

mcp_server = add_mcp_server(
    app,
    mount_path="/mcp",
    name="NCM Attributes MCP",
    description="MCP server for NCM attributes",
    base_url="http://172.18.0.1:8000",
    describe_all_responses=True,
    describe_full_response_schema=True,
)

# NCM Attribute Routes
@app.get("/ncm/{ncm_code}/attributes", response_model=NcmAttributeList)
async def get_ncm_attributes(
    ncm_code: str,
    db: Session = Depends(get_db)
):
    """
    Get all attributes with their possible values for a specific NCM code
    """
    # Get NCM from database
    ncm = NcmAttributeRepository.get_ncm_by_code(db, ncm_code)
    if not ncm:
        raise HTTPException(status_code=404, detail=f"NCM with code {ncm_code} not found")
    
    # Get attributes from service
    attributes = NcmAttributeService.get_attributes_by_ncm_code(db, ncm_code)
    
    # Format response
    return {
        "ncm_code": ncm.code,
        "ncm_description": ncm.description,
        "attributes": attributes
    }

@app.get("/ncm/search", response_model=NcmSearchResults)
async def search_ncm(
    query: str = Query(..., description="Search term for NCM code or description"),
    limit: int = Query(20, description="Maximum number of results to return"),
    db: Session = Depends(get_db)
):
    """
    Search for NCM codes by code or description
    """
    results = NcmAttributeService.search_ncm_by_code_or_description(db, query, limit)
    return {
        "results": results,
        "count": len(results)
    }

# MCP Tools
@mcp_server.tool()
async def print_name() -> str:
    """Print the name of the user."""
    return "Meu nome é Túlio"

@mcp_server.tool()
async def get_ncm_info(ncm: str) -> str:
    """Get the information of the NCM."""
    return f"NCM {ncm} info: Test NCM information"


@mcp_server.tool()
async def get_ncm_info_tool(ncm: str) -> dict:
    """
    Get the information of the NCM.
    """
    return {"ncm": ncm, "info": f"NCM {ncm} info: Test NCM information"}


@mcp_server.tool()
async def get_ncm_attributes_tool(ncm: SkipValidation[any]) -> str:
    """
    Get all attributes with their possible values for a specific NCM code
    
    Parameters:
        ncm: The NCM code to search for.
        
    Returns:
        String with the attributes of the NCM in Markdown format
    """
    # Get database session
    from app.database.config import SessionLocal
    db = SessionLocal()
    try:
        # Get NCM from database
        ncm_code = re.sub(r'[^0-9]', '', str(ncm))
        ncm_obj = NcmAttributeRepository.get_ncm_by_code(db, ncm_code)
        if not ncm_obj:
            return {"error": f"NCM with code {ncm_code} not found"}
        
        # Get attributes from service
        attributes = NcmAttributeService.get_attributes_by_ncm_code(db, ncm_code)
        
        # Format response
        
        return format_ncm_attributes({
            "ncm_code": ncm_obj.code,
            "ncm_description": ncm_obj.description,
            "attributes": attributes
        })
    except Exception as e:
        return {"error": str(e)}
    finally:
        db.close()



def format_ncm_attributes(data: dict) -> str:
    """
    Format the attributes of the NCM in Markdown format.

    Args:
        ncm_code: The NCM code to search for
        
    Returns:
        String with the attributes of the NCM in Markdown format
    """
    # Create a DataFrame from the attributes
    #data = json.dumps(data)
    df = pd.DataFrame.from_dict(data['attributes'])
    
    # Create a Markdown table
    markdown_table = df.to_html(index=False)
    
    return markdown_table
# Run the server if this file is executed directly
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)