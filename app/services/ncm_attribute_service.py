from sqlalchemy.orm import Session
from typing import List, Dict, Any, Optional
from ..models import Ncm, NcmAttributes, Attribute
from sqlalchemy import or_, String
from ..repositories.ncm_attribute_repository import NcmAttributeRepository

class NcmAttributeService:
    """
    Service to handle operations related to NCM attributes
    """
    
    @staticmethod
    def get_attributes_by_ncm_code(db: Session, ncm_code: str) -> List[Dict[str, Any]]:
        """
        Get all attributes with their possible values for a specific NCM code
        
        Args:
            db: Database session
            ncm_code: The NCM code to search for
            
        Returns:
            List of attributes with their possible values
        """
        # Find the NCM by code
        ncm = NcmAttributeRepository.get_ncm_by_code(db, ncm_code)
        
        if not ncm:
            return []
            
        # Get all attributes for this NCM
        ncm_attributes = NcmAttributeRepository.get_attributes_by_ncm_id(db, ncm.id)
        
        # Format response
        result = []
        for attr in ncm_attributes:
            attribute_data = {
                "attr_code": attr['attr_code'],
                "presentation_name": attr['presentation_name'],
                "filling_form": attr['filling_form'],
                "is_required": attr['is_required'],
                "filling_guidance": attr['filling_guidance'],
                "max_length": attr['max_length'],
                "possible_values": []
            }
            
            # Add possible values based on filling form type
            if attr['filling_form'] == "STATIC_LIST" and attr['domain']:
                # If the attribute has a domain with possible values
                attribute_data["possible_values"] = attr['domain']
            elif attr['filling_form'] == "BOOLEAN":
                attribute_data["possible_values"] = [True, False]
            
            result.append(attribute_data)
            
        return result
    
    @staticmethod
    def search_ncm_by_code_or_description(db: Session, search_term: str, limit: int = 20) -> List[Dict[str, Any]]:
        """
        Search for NCM codes by code or description
        
        Args:
            db: Database session
            search_term: The search term to look for in code or description
            limit: Maximum number of results to return
            
        Returns:
            List of NCM codes with basic info
        """
        # Search for NCMs by code or description
        ncms = NcmAttributeRepository.search_ncm(db, search_term, limit)
        
        result = []
        for ncm in ncms:
            result.append({
                "id": ncm.id,
                "code": ncm.code,
                "description": ncm.description,
                "attributes_count": NcmAttributeRepository.count_ncm_attributes(db, ncm.id)
            })
            
        return result 

    @staticmethod
    def get_attributes_by_ncm_id(db: Session, ncm_id: int) -> List[Dict[str, Any]]:
        """
        Get all attributes for an NCM by ID, joined with Attribute model
        """
        # Use join to get Attribute data
        result = db.query(NcmAttribute, Attribute).join(
            Attribute, NcmAttribute.attribute_id == Attribute.id
        ).filter(
            NcmAttribute.ncm_id == ncm_id,
            Attribute.deleted_at.is_(None)  # Only keep deleted_at filter for Attribute
        ).order_by(NcmAttribute.order).all()
        
        # Transform the result into a list of dictionaries
        attributes = []
        for ncm_attr, attr in result:
            attribute_data = {
                # Data from NcmAttribute
                "id": ncm_attr.id,
                "attribute_id": ncm_attr.attribute_id,
                "is_required": ncm_attr.is_required,
                "validity_start_date": ncm_attr.validity_start_date,
                "validity_end_date": ncm_attr.validity_end_date,
                "have_conditional_attributes": ncm_attr.have_conditional_attributes,
                "condition_description": ncm_attr.condition_description,
                "condition": ncm_attr.condition,
                "is_multivalued": ncm_attr.is_multivalued,
                "sub_attributes": ncm_attr.sub_attributes,
                "order": ncm_attr.order,
                "modality": ncm_attr.modality,
                
                # Data from Attribute
                "attr_code": attr.attr_code,
                "presentation_name": attr.presentation_name,
                "filling_form": attr.filling_form,
                "max_length": attr.max_length,
                "filling_guidance": attr.filling_guidance,
                "attribute_modality": attr.modality,
                "domain": attr.domain,
                "goals": attr.goals,
                "organizations": attr.organizations,
                "decimal_places": attr.decimal_places
            }
            attributes.append(attribute_data)
            
        return attributes

    @staticmethod
    def count_ncm_attributes(db: Session, ncm_id: int) -> int:
        """
        Count attributes for an NCM
        """
        return db.query(NcmAttribute).filter(
            NcmAttribute.ncm_id == ncm_id
        ).count() 