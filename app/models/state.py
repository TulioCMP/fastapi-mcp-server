from sqlalchemy import Column, Integer, BigInteger, String, Boolean, DateTime, JSON, ForeignKey, SmallInteger
from sqlalchemy.orm import relationship
from ..database.config import Base
from .base_models import TimestampMixin

class State(Base, TimestampMixin):
    __tablename__ = "state"

    id = Column(BigInteger, primary_key=True)
    country_id = Column(Integer, ForeignKey("country.id"), nullable=False)
    state = Column(String(50), nullable=False)
    status = Column(SmallInteger, nullable=False)
    state_code = Column(String(255), nullable=True)
    
    # Relationships
    country = relationship("Country", back_populates="states")
    cities = relationship("City", back_populates="state")
    foreign_operators = relationship("ForeignOperator", back_populates="state") 