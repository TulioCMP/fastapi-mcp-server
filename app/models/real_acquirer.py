from sqlalchemy import Column, Integer, BigInteger, String, Boolean, DateTime, ForeignKey, Index
from sqlalchemy.orm import relationship
from ..database.config import Base
from .base_models import TimestampMixin

class RealAcquirer(Base, TimestampMixin):
    __tablename__ = "real_acquirers"

    id = Column(BigInteger, primary_key=True)
    consignee_id = Column(BigInteger, ForeignKey("consignees.id"), nullable=False)
    name = Column(String(255), nullable=False, index=True)
    cnpj = Column(String(255), nullable=False, index=True)
    
    # Relationships
    consignee = relationship("Consignee", back_populates="real_acquirers")
    catalog_ncm_items = relationship("CatalogNcmItem", back_populates="real_acquirer")
    
    __table_args__ = (
        Index("real_acquirers_name_index", "name"),
        Index("real_acquirers_cnpj_index", "cnpj"),
    ) 