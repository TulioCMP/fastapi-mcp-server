from sqlalchemy import Column, Integer, BigInteger, String, Boolean, DateTime, ForeignKey, JSON, Index, Date, UniqueConstraint
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from ..database.config import Base
from .base_models import TimestampMixin

class NcmAttribute(Base, TimestampMixin):
    __tablename__ = "ncm_attribute"

    id = Column(BigInteger, primary_key=True)
    ncm_id = Column(BigInteger, ForeignKey("ncm.id"), nullable=False)
    attribute_id = Column(BigInteger, ForeignKey("attribute.id"), nullable=False)
    conditional_of_attr_id = Column(BigInteger, ForeignKey("attribute.id"), nullable=True)
    is_required = Column(Boolean, default=False, nullable=False)
    validity_start_date = Column(Date, nullable=True)
    validity_end_date = Column(Date, nullable=True)
    have_conditional_attributes = Column(Boolean, default=False, nullable=False)
    condition_description = Column(String(255), nullable=True)
    condition = Column(JSON, nullable=True)
    is_multivalued = Column(Boolean, default=False, nullable=False)
    sub_attributes = Column(JSONB, nullable=True)
    order = Column(Integer, default=0, nullable=False)
    compound_attribute_of_attr_id = Column(BigInteger, nullable=True)
    have_compound_attributes = Column(Boolean, default=False, nullable=False)
    modality = Column(String(255), nullable=True)
    
    # Relationships
    ncm = relationship("Ncm", back_populates="ncm_attributes")
    attribute = relationship("Attribute", foreign_keys=[attribute_id])
    conditional_of_attr = relationship("Attribute", foreign_keys=[conditional_of_attr_id])
    
    __table_args__ = (
        UniqueConstraint('ncm_id', 'attribute_id', name='ncm_attribute_ncm_id_attribute_id_unique'),
        Index("ncm_attribute_attribute_id_index", "attribute_id"),
        Index("ncm_attribute_ncm_id_attribute_id_index", "ncm_id", "attribute_id"),
    ) 