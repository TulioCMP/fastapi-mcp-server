from sqlalchemy import Column, Integer, BigInteger, String, Boolean, DateTime, JSON, ForeignKey, SmallInteger, Numeric, Index
from sqlalchemy.orm import relationship
from ..database.config import Base
from .base_models import TimestampMixin

class City(Base, TimestampMixin):
    __tablename__ = "city"

    id = Column(BigInteger, primary_key=True)
    country_id = Column(Integer, ForeignKey("country.id"), nullable=False)
    state_id = Column(Integer, ForeignKey("state.id"), nullable=False)
    city = Column(String(50), nullable=False)
    latitude = Column(Numeric(10, 7), nullable=False)
    longitude = Column(Numeric(10, 7), nullable=False)
    status = Column(SmallInteger, nullable=False)
    
    # Relationships
    country = relationship("Country", back_populates="cities")
    state = relationship("State", back_populates="cities")
    
    __table_args__ = (
        Index("city_city_country_id_index", "city", "country_id"),
    ) 