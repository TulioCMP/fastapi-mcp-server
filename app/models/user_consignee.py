from sqlalchemy import Column, Integer, BigInteger, String, Boolean, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from ..database.config import Base
from .base_models import TimestampMixin

class UserConsignee(Base, TimestampMixin):
    __tablename__ = "users_consignees"

    id = Column(BigInteger, primary_key=True)
    logcomex_user_id = Column(BigInteger, nullable=False)
    consignee_id = Column(BigInteger, ForeignKey("consignees.id"), nullable=False)
    
    # Relationships
    consignee = relationship("Consignee", back_populates="users_consignees")
    
    __table_args__ = (
        UniqueConstraint('logcomex_user_id', 'consignee_id', name='users_consignees_logcomex_user_id_consignee_id_unique'),
    ) 