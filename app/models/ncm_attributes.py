from sqlalchemy import Column, Integer, BigInteger, String, Boolean, DateTime, ForeignKey, JSON, Index, Date, UniqueConstraint, CheckConstraint
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from ..database.config import Base
from .base_models import TimestampMixin

class NcmAttributes(Base, TimestampMixin):
    __tablename__ = "ncm_attributes"

    id = Column(BigInteger, primary_key=True)
    ncm_id = Column(BigInteger, ForeignKey("ncm.id"), nullable=False)
    conditional_of_attr_id = Column(BigInteger, ForeignKey("ncm_attributes.id"), nullable=True)
    attr_code = Column(String(255), nullable=False, index=True)
    presentation_name = Column(String(255), nullable=False, index=True)
    filling_form = Column(String(255), nullable=False)
    max_length = Column(Integer, nullable=True)
    filling_guidance = Column(String(255), nullable=True)
    modality = Column(String(255), nullable=False)
    is_required = Column(Boolean, default=False, nullable=False)
    validity_start_date = Column(Date, nullable=True)
    validity_end_date = Column(Date, nullable=True)
    domain = Column(JSONB, nullable=True)
    goals = Column(JSONB, nullable=True)
    organizations = Column(JSONB, nullable=True)
    have_conditional_attributes = Column(Boolean, default=False, nullable=False)
    condition_description = Column(String(255), nullable=True)
    condition = Column(JSON, nullable=True)
    is_multivalued = Column(Boolean, default=False, nullable=False)
    sub_attributes = Column(JSONB, nullable=True)
    order = Column(Integer, default=0, nullable=False)
    
    # Relationships
    ncm = relationship("Ncm")
    conditional_of_attr = relationship("NcmAttributes", remote_side=[id], backref="conditional_attributes")
    catalog_ncm_item_attributes = relationship("CatalogNcmItemAttributes", back_populates="ncm_attribute")
    
    __table_args__ = (
        UniqueConstraint('ncm_id', 'attr_code', name='ncm_attributes_ncm_id_attr_code_unique'),
        CheckConstraint(
            "filling_form IN ('BOOLEAN', 'COMPOUND', 'STATIC_LIST', 'INTEGER', 'FLOAT', 'TEXT')",
            name="ncm_attributes_filling_form_check"
        ),
        Index("ncm_attributes_attr_code_index", "attr_code"),
        Index("ncm_attributes_presentation_name_index", "presentation_name"),
    ) 