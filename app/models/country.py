from sqlalchemy import Column, Integer, BigInteger, String, Boolean, DateTime, JSON, ForeignKey, SmallInteger
from sqlalchemy.orm import relationship
from ..database.config import Base
from .base_models import TimestampMixin

class Country(Base, TimestampMixin):
    __tablename__ = "country"

    id = Column(BigInteger, primary_key=True)
    code = Column(String(2), nullable=False)
    country = Column(String(50), nullable=False)
    status = Column(SmallInteger, nullable=False)
    country_pt = Column(String(255), nullable=True)
    
    # Relationships
    states = relationship("State", back_populates="country")
    cities = relationship("City", back_populates="country") 