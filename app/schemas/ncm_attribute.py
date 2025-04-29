from typing import List, Dict, Any, Optional, Union
from pydantic import BaseModel, Field

class AttributeValue(BaseModel):
    """Schema for a possible attribute value from domain"""
    code: str = Field(..., description="Value code")
    description: str = Field(..., description="Value description")

class NcmAttribute(BaseModel):
    """Schema for an NCM attribute with possible values"""
    attr_code: str = Field(..., description="Attribute code")
    presentation_name: str = Field(..., description="Presentation name for the attribute")
    filling_form: str = Field(..., description="Type of form field (BOOLEAN, COMPOUND, STATIC_LIST, INTEGER, FLOAT, TEXT)")
    is_required: bool = Field(..., description="Whether the attribute is required")
    filling_guidance: Optional[str] = Field(None, description="Guidance on how to fill the attribute")
    max_length: Optional[int] = Field(None, description="Maximum length for text fields")
    possible_values: List[Union[AttributeValue, bool, str, int, float]] = Field(default=[], description="Possible values for the attribute")

class NcmAttributeList(BaseModel):
    """Schema for a list of NCM attributes"""
    ncm_code: str = Field(..., description="NCM code")
    ncm_description: Dict[str, str] = Field(..., description="NCM description in multiple languages")
    attributes: List[NcmAttribute] = Field(..., description="List of attributes for the NCM")

class NcmSearchResult(BaseModel):
    """Schema for an NCM search result"""
    id: int = Field(..., description="NCM ID")
    code: str = Field(..., description="NCM code")
    description: Dict[str, str] = Field(..., description="NCM description in multiple languages")
    attributes_count: int = Field(..., description="Number of attributes for this NCM")

class NcmSearchResults(BaseModel):
    """Schema for a list of NCM search results"""
    results: List[NcmSearchResult] = Field(..., description="List of NCM search results")
    count: int = Field(..., description="Total number of results") 