from sqlalchemy import Column, Integer, BigInteger, String, Boolean, DateTime, UniqueConstraint
from sqlalchemy.orm import relationship
from ..database.config import Base
from .base_models import TimestampMixin

class Consignee(Base, TimestampMixin):
    __tablename__ = "consignees"

    id = Column(BigInteger, primary_key=True)
    logcomex_consignee_id = Column(BigInteger, unique=True, nullable=True)
    logcomex_customer_id = Column(BigInteger, nullable=False)
    consignee_name = Column(String(255), nullable=False)
    consignee_cnpj = Column(String(255), nullable=False)
    customer_name = Column(String(255), nullable=False)
    customer_cnpj = Column(String(255), nullable=True)
    portal_unico_synced_at = Column(DateTime(timezone=True), nullable=True)
    is_synchronizing = Column(Boolean, default=False, nullable=False)
    fictional = Column(Boolean, default=False, nullable=True)
    archived_at = Column(DateTime(timezone=True), nullable=True)
    load_dis_from_aereo = Column(Boolean, default=True, nullable=False)
    
    # Relationships
    catalogs = relationship("Catalog", back_populates="consignee")
    real_acquirers = relationship("RealAcquirer", back_populates="consignee")
    foreign_operators = relationship("ForeignOperator", back_populates="consignee")
    users_consignees = relationship("UserConsignee", back_populates="consignee") 