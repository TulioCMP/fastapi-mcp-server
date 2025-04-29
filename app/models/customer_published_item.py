from sqlalchemy import Column, Integer, BigInteger, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from ..database.config import Base
from .base_models import TimestampMixin

class CustomerPublishedItem(Base, TimestampMixin):
    __tablename__ = "customer_published_items"

    id = Column(BigInteger, primary_key=True)
    customer_id = Column(BigInteger, nullable=False)
    catalog_ncm_item_id = Column(BigInteger, ForeignKey("catalog_ncm_items.id"), nullable=False)
    
    # Relationships
    catalog_ncm_item = relationship("CatalogNcmItem", back_populates="customer_published_items") 