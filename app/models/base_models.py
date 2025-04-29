from sqlalchemy import Column, Integer, String, Boolean, DateTime, JSON, ForeignKey, BigInteger, Float, Date, SmallInteger, Text, TIMESTAMP, JSON, CHAR, CheckConstraint, MetaData, UniqueConstraint
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import func
from ..database.config import Base

class TimestampMixin:
    """Mixin for created_at, updated_at, and deleted_at columns"""
    created_at = Column(DateTime(timezone=True))
    updated_at = Column(DateTime(timezone=True))
    deleted_at = Column(DateTime(timezone=True), nullable=True) 