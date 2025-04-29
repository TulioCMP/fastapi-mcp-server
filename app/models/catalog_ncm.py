from sqlalchemy import Column, Integer, BigInteger, String, Boolean, DateTime, ForeignKey, Index, UUID
from sqlalchemy.orm import relationship
from ..database.config import Base
from .base_models import TimestampMixin
import uuid

class CatalogNcm(Base, TimestampMixin):
    __tablename__ = "catalog_ncm"

    id = Column(BigInteger, primary_key=True)
    key = Column(UUID, nullable=False, unique=True, default=uuid.uuid4)
    catalog_id = Column(BigInteger, ForeignKey("catalogs.id"), nullable=False)
    ncm_id = Column(BigInteger, ForeignKey("ncm.id"), nullable=False)
    status = Column(String(255), default='untouched', nullable=False)
    
    # Relationships
    catalog = relationship("Catalog", back_populates="catalog_ncms")
    ncm = relationship("Ncm", back_populates="catalog_ncms")
    catalog_ncm_items = relationship("CatalogNcmItem", back_populates="catalog_ncm")
    
    __table_args__ = (
        Index("catalog_ncm_catalog_id_index", "catalog_id"),
        Index("catalog_ncm_ncm_id_index", "ncm_id"),
        Index("catalog_ncm_key_index", "key"),
        Index("catalog_ncm_deleted_at_index", "deleted_at"),
    ) 