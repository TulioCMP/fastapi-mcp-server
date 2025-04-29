from sqlalchemy import Column, Integer, BigInteger, String, Boolean, DateTime, JSON, ForeignKey, CheckConstraint, Index
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import func
from ..database.config import Base
from .base_models import TimestampMixin

class Attribute(Base, TimestampMixin):
    __tablename__ = "attribute"

    id = Column(BigInteger, primary_key=True)
    attr_code = Column(String(255), nullable=False, unique=True, index=True)
    presentation_name = Column(String(255), nullable=False, index=True)
    filling_form = Column(String(255), nullable=False)
    max_length = Column(Integer, nullable=True)
    filling_guidance = Column(String(255), nullable=True)
    modality = Column(String(255), nullable=False)
    domain = Column(JSONB, nullable=True)
    goals = Column(JSONB, nullable=True)
    organizations = Column(JSONB, nullable=True)
    decimal_places = Column(Integer, nullable=True)

    __table_args__ = (
        CheckConstraint(
            "filling_form IN ('BOOLEAN', 'COMPOUND', 'STATIC_LIST', 'INTEGER', 'FLOAT', 'TEXT')",
            name="attribute_filling_form_check"
        ),
        Index("attribute_attr_code_index", "attr_code"),
        Index("attribute_presentation_name_index", "presentation_name"),
    ) 