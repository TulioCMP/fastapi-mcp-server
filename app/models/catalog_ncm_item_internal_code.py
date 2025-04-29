from sqlalchemy import Column, Integer, BigInteger, String, Boolean, DateTime, ForeignKey, Index, UniqueConstraint
from sqlalchemy.orm import relationship
from ..database.config import Base
from .base_models import TimestampMixin

class CatalogNcmItemInternalCode(Base, TimestampMixin):
    __tablename__ = "catalog_ncm_item_internal_code"

    id = Column(BigInteger, primary_key=True)
    catalog_ncm_item_id = Column(BigInteger, ForeignKey("catalog_ncm_items.id"), nullable=False)
    internal_code = Column(String(100), nullable=False, index=True)
    
    # Relationships
    catalog_ncm_item = relationship("CatalogNcmItem", back_populates="internal_codes")
    
    __table_args__ = (
        UniqueConstraint('catalog_ncm_item_id', 'internal_code', name='catalog_ncm_item_internal_code_catalog_ncm_item_id_internal_cod'),
        Index("catalog_ncm_item_internal_code_internal_code_index", "internal_code"),
    ) 