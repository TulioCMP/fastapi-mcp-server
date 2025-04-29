from sqlalchemy import Column, Integer, BigInteger, String, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from ..database.config import Base
from .base_models import TimestampMixin

class CatalogLog(Base, TimestampMixin):
    __tablename__ = "catalog_logs"

    id = Column(BigInteger, primary_key=True)
    catalog_id = Column(BigInteger, ForeignKey("catalogs.id"), nullable=True)
    ncm_id = Column(BigInteger, ForeignKey("ncm.id"), nullable=True)
    logcomex_user_id = Column(BigInteger, nullable=False)
    user = Column(String(255), nullable=False)
    ip = Column(String(255), nullable=False)
    action = Column(String(255), nullable=False)
    changes = Column(Text, nullable=True)
    customer_id = Column(BigInteger, nullable=True)
    
    # Relationships
    catalog = relationship("Catalog", back_populates="catalog_logs")
    ncm = relationship("Ncm", back_populates="catalog_logs") 