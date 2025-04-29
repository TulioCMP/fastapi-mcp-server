from sqlalchemy import Column, Integer, BigInteger, String, Boolean, DateTime, ForeignKey, Index
from sqlalchemy.orm import relationship
from ..database.config import Base
from .base_models import TimestampMixin

class ForeignOperator(Base, TimestampMixin):
    __tablename__ = "foreign_operator"

    id = Column(BigInteger, primary_key=True)
    consignee_id = Column(Integer, ForeignKey("consignees.id"), nullable=False, index=True)
    operator_name = Column(String(255), nullable=False, index=True)
    email = Column(String(255), nullable=True)
    id_number = Column(String(255), nullable=True)
    internal_code = Column(String(255), nullable=True)
    zip_code = Column(String(255), nullable=True)
    address = Column(String(255), nullable=False)
    issuing_agency_id = Column(Integer, ForeignKey("issuing_agencies.id"), nullable=True)
    number = Column(String(255), nullable=True)
    portal_unico_code = Column(String(255), nullable=True)
    portal_unico_version = Column(String(255), nullable=True)
    portal_unico_created_at = Column(DateTime(timezone=True), nullable=True)
    portal_unico_updated_at = Column(DateTime(timezone=True), nullable=True)
    country_id = Column(BigInteger, ForeignKey("country.id"), nullable=True)
    state_id = Column(BigInteger, ForeignKey("state.id"), nullable=True)
    city = Column(String(255), nullable=True)
    portal_unico_situation = Column(String(255), nullable=True)
    is_exporter = Column(Boolean, nullable=True)
    is_manufacturer = Column(Boolean, nullable=True)
    
    # Relationships
    consignee = relationship("Consignee", back_populates="foreign_operators")
    issuing_agency = relationship("IssuingAgency", back_populates="foreign_operators")
    country = relationship("Country")
    state = relationship("State", back_populates="foreign_operators")
    catalog_ncm_items_foreign_operators = relationship("CatalogNcmItemsForeignOperator", back_populates="foreign_operator")
    
    __table_args__ = (
        Index("foreign_operator_consignee_id_index", "consignee_id"),
        Index("foreign_operator_operator_name_index", "operator_name"),
    ) 