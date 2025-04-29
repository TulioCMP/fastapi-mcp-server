from sqlalchemy.orm import Session, joinedload
from typing import List, Dict, Any, Optional
from sqlalchemy import or_, String
from ..models import Ncm, NcmAttribute, Attribute

class NcmAttributeRepository:
    """
    Repository for NCM attributes
    """
    
    @staticmethod
    def get_ncm_by_code(db: Session, ncm_code: str) -> Optional[Ncm]:
        """
        Get an NCM by its code
        
        Args:
            db: Database session
            ncm_code: The NCM code to search for
            
        Returns:
            NCM object if found, None otherwise
        """
        return db.query(Ncm).filter(
            Ncm.code == ncm_code,
            Ncm.deleted_at.is_(None)
        ).first()
    
    @staticmethod
    def get_attributes_by_ncm_id(db: Session, ncm_id: int) -> List[Dict[str, Any]]:
        """
        Get all attributes for an NCM by ID, joined with Attribute model
        
        Args:
            db: Database session
            ncm_id: The NCM ID
            
        Returns:
            List of dictionaries with combined data
        """
        # Query with explicit column selection instead of selecting everything
        result = db.query(
            NcmAttribute.id,
            NcmAttribute.attribute_id,
            NcmAttribute.is_required,
            NcmAttribute.validity_start_date,
            NcmAttribute.validity_end_date,
            NcmAttribute.have_conditional_attributes,
            NcmAttribute.condition_description,
            NcmAttribute.condition,
            NcmAttribute.is_multivalued,
            NcmAttribute.sub_attributes,
            NcmAttribute.order,
            NcmAttribute.modality,
            Attribute.id.label('attr_id'),
            Attribute.attr_code,
            Attribute.presentation_name,
            Attribute.filling_form,
            Attribute.max_length,
            Attribute.filling_guidance,
            Attribute.modality.label('attr_modality'),
            Attribute.domain,
            Attribute.decimal_places
        ).join(
            Attribute, NcmAttribute.attribute_id == Attribute.id
        ).filter(
            NcmAttribute.ncm_id == ncm_id,
            Attribute.deleted_at.is_(None)
        ).order_by(NcmAttribute.order).all()
        
        # Transform the result
        attributes = []
        for row in result:
            # Convert row to dictionary
            attribute_data = {
                "id": row.id,
                "attribute_id": row.attribute_id,
                "is_required": row.is_required,
                "validity_start_date": row.validity_start_date,
                "validity_end_date": row.validity_end_date,
                "have_conditional_attributes": row.have_conditional_attributes,
                "condition_description": row.condition_description,
                "condition": row.condition,
                "is_multivalued": row.is_multivalued,
                "sub_attributes": row.sub_attributes,
                "order": row.order,
                "modality": row.modality,
                "attr_code": row.attr_code,
                "presentation_name": row.presentation_name,
                "filling_form": row.filling_form,
                "max_length": row.max_length,
                "filling_guidance": row.filling_guidance,
                "attribute_modality": row.attr_modality,
                "domain": row.domain,
                "decimal_places": row.decimal_places
            }
            attributes.append(attribute_data)
            
        return attributes
    
    @staticmethod
    def search_ncm(db: Session, search_term: str, limit: int = 20) -> List[Ncm]:
        """
        Search for NCMs by code or description
        
        Args:
            db: Database session
            search_term: The search term
            limit: Maximum number of results
            
        Returns:
            List of matching NCMs
        """
        search_pattern = f"%{search_term}%"
        
        return db.query(Ncm).filter(
            or_(
                Ncm.code.ilike(search_pattern),
                Ncm.description.cast(String).ilike(search_pattern)
            ),
            Ncm.deleted_at.is_(None)
        ).limit(limit).all()
    
    @staticmethod
    def count_ncm_attributes(db: Session, ncm_id: int) -> int:
        """
        Count attributes for an NCM
        
        Args:
            db: Database session
            ncm_id: The NCM ID
            
        Returns:
            Number of attributes
        """
        return db.query(NcmAttribute).filter(
            NcmAttribute.ncm_id == ncm_id
        ).count()

    @staticmethod
    def get_attributes_by_ncm_code(db: Session, ncm_code: str) -> List[Dict[str, Any]]:
        """
        Get all attributes with their possible values for a specific NCM code
        """
        # Find the NCM by code
        ncm = NcmAttributeRepository.get_ncm_by_code(db, ncm_code)
        
        if not ncm:
            return []
        
        # Get all attributes for this NCM (now with joined Attribute data)
        ncm_attributes = NcmAttributeRepository.get_attributes_by_ncm_id(db, ncm.id)
        
        # Format response with combined data
        result = []
        for attr in ncm_attributes:
            attribute_data = {
                "attr_code": attr["attr_code"],
                "presentation_name": attr["presentation_name"],
                "filling_form": attr["filling_form"],
                "is_required": attr["is_required"],
                "filling_guidance": attr["filling_guidance"],
                "max_length": attr["max_length"],
                "decimal_places": attr["decimal_places"],
                "modality": attr["modality"] or attr["attribute_modality"],
                "possible_values": []
            }
            
            # Add possible values based on filling form type
            if attr["filling_form"] == "STATIC_LIST" and attr["domain"]:
                # If the attribute has a domain with possible values
                attribute_data["possible_values"] = attr["domain"].get("values", [])
            elif attr["filling_form"] == "BOOLEAN":
                attribute_data["possible_values"] = [True, False]
            
            result.append(attribute_data)
        
        return result 