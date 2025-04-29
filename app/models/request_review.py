from sqlalchemy import Column, Integer, BigInteger, String, Boolean, DateTime, ForeignKey, JSON
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from ..database.config import Base
from .base_models import TimestampMixin

class RequestReviewItemStatus(Base, TimestampMixin):
    __tablename__ = "request_review_item_status"

    id = Column(BigInteger, primary_key=True)
    name = Column(String(255), nullable=True)
    slug = Column(String(255), nullable=True)
    
    # Relationships
    request_review_items = relationship("RequestReviewItem", back_populates="status")


class RequestReviewItem(Base, TimestampMixin):
    __tablename__ = "request_review_items"

    id = Column(BigInteger, primary_key=True)
    customer_id = Column(BigInteger, nullable=False)
    user_ids = Column(JSONB, default='{}', nullable=False)
    catalog_ncm_item_id = Column(BigInteger, ForeignKey("catalog_ncm_items.id"), nullable=False)
    status_id = Column(BigInteger, ForeignKey("request_review_item_status.id"), nullable=False)
    owner_user_id = Column(BigInteger, nullable=False)
    reviewed_by_user_id = Column(BigInteger, nullable=True)
    
    # Relationships
    catalog_ncm_item = relationship("CatalogNcmItem", back_populates="request_review_items")
    status = relationship("RequestReviewItemStatus", back_populates="request_review_items") 