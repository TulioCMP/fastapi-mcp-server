from sqlalchemy import Column, Integer, BigInteger, String, Boolean, DateTime, ForeignKey, Index, UUID, UniqueConstraint
from sqlalchemy.orm import relationship
from ..database.config import Base
from .base_models import TimestampMixin
import uuid

class CatalogNcmItemAttribute(Base, TimestampMixin):
    __tablename__ = "catalog_ncm_item_attribute"

    id = Column(BigInteger, primary_key=True)
    key = Column(UUID, nullable=False, unique=True, default=uuid.uuid4)
    catalog_ncm_item_id = Column(BigInteger, ForeignKey("catalog_ncm_items.id"), nullable=False)
    attribute_id = Column(BigInteger, ForeignKey("attribute.id"), nullable=False)
    value = Column(String(255), nullable=True, index=True)
    was_filled_by_log_ai = Column(Boolean, default=False, nullable=False)
    
    # Relationships
    catalog_ncm_item = relationship("CatalogNcmItem", back_populates="catalog_ncm_item_attributes")
    attribute = relationship("Attribute")
    
    __table_args__ = (
        UniqueConstraint('catalog_ncm_item_id', 'attribute_id', name='catalog_ncm_item_attribute_catalog_ncm_item_id_attribute_id_uni'),
        Index("catalog_ncm_item_attribute_catalog_ncm_item_id_attribute_id_ind", "catalog_ncm_item_id", "attribute_id"),
        Index("catalog_ncm_item_attribute_catalog_ncm_item_id_index", "catalog_ncm_item_id"),
        Index("catalog_ncm_item_attribute_key_index", "key"),
        Index("catalog_ncm_item_attribute_value_index", "value"),
    ) 