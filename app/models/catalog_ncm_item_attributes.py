from sqlalchemy import Column, Integer, BigInteger, String, Boolean, DateTime, ForeignKey, Index, UUID
from sqlalchemy.orm import relationship
from ..database.config import Base
from .base_models import TimestampMixin
import uuid

class CatalogNcmItemAttributes(Base, TimestampMixin):
    __tablename__ = "catalog_ncm_item_attributes"

    id = Column(BigInteger, primary_key=True)
    key = Column(UUID, nullable=False, unique=True, default=uuid.uuid4)
    catalog_ncm_item_id = Column(BigInteger, ForeignKey("catalog_ncm_items.id"), nullable=False)
    ncm_attribute_id = Column(BigInteger, ForeignKey("ncm_attributes.id"), nullable=False)
    value = Column(String(255), nullable=True)
    
    # Relationships
    catalog_ncm_item = relationship("CatalogNcmItem", back_populates="catalog_ncm_items_attributes")
    ncm_attribute = relationship("NcmAttributes", back_populates="catalog_ncm_item_attributes")
    
    __table_args__ = (
        Index("catalog_ncm_item_attributes_catalog_ncm_item_id_idx", "catalog_ncm_item_id"),
        Index("catalog_ncm_item_attributes_deleted_at_idx", "deleted_at"),
        Index("catalog_ncm_item_attributes_key_index", "key"),
    ) 