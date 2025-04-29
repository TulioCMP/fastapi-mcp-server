from sqlalchemy import Column, Integer, BigInteger, String, Boolean, DateTime, ForeignKey, JSON, Index
from sqlalchemy.orm import relationship
from ..database.config import Base
from .base_models import TimestampMixin

class Ncm(Base, TimestampMixin):
    __tablename__ = "ncm"

    id = Column(BigInteger, primary_key=True)
    code = Column(String(255), nullable=False, unique=True)
    description = Column(JSON, nullable=False)
    image = Column(String(255), nullable=True)
    generating_image = Column(Boolean, default=False, nullable=False)
    
    # Relationships
    catalog_ncms = relationship("CatalogNcm", back_populates="ncm")
    catalog_logs = relationship("CatalogLog", back_populates="ncm")
    ncm_attributes = relationship("NcmAttribute", back_populates="ncm")
    
    __table_args__ = (
        Index("ncm_code_index", "code"),
    ) 