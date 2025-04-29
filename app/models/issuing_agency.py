from sqlalchemy import Column, Integer, BigInteger, String, Boolean, DateTime, Text
from sqlalchemy.orm import relationship
from ..database.config import Base
from .base_models import TimestampMixin

class IssuingAgency(Base, TimestampMixin):
    __tablename__ = "issuing_agencies"

    id = Column(BigInteger, primary_key=True)
    code = Column(Text, nullable=False, unique=True)
    description = Column(Text, nullable=False)
    
    # Relationships
    foreign_operators = relationship("ForeignOperator", back_populates="issuing_agency") 