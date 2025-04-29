from sqlalchemy import Column, Integer, BigInteger, String, Boolean, DateTime, ForeignKey, Index, UUID
from sqlalchemy.orm import relationship
from ..database.config import Base
from .base_models import TimestampMixin
import uuid

class Catalog(Base, TimestampMixin):
    __tablename__ = "catalogs"

    id = Column(BigInteger, primary_key=True)
    key = Column(UUID, nullable=False, unique=True, default=uuid.uuid4)
    consignee_id = Column(BigInteger, ForeignKey("consignees.id"), nullable=False)
    is_loading = Column(Boolean, default=False, nullable=False)
    status = Column(String(255), default='untouched', nullable=False)
    
    # Relationships
    consignee = relationship("Consignee", back_populates="catalogs")
    catalog_ncms = relationship("CatalogNcm", back_populates="catalog")
    catalog_logs = relationship("CatalogLog", back_populates="catalog")
    
    __table_args__ = (
        Index("catalogs_key_index", "key"),
    ) 