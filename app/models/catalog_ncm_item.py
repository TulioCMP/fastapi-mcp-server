from sqlalchemy import Column, Integer, BigInteger, String, Boolean, DateTime, ForeignKey, Index, UUID, Text, Numeric
from sqlalchemy.orm import relationship
from ..database.config import Base
from .base_models import TimestampMixin
import uuid

class CatalogNcmItem(Base, TimestampMixin):
    __tablename__ = "catalog_ncm_items"

    id = Column(BigInteger, primary_key=True)
    key = Column(UUID, nullable=False, unique=True, default=uuid.uuid4)
    catalog_ncm_id = Column(BigInteger, ForeignKey("catalog_ncm.id"), nullable=False)
    di_pu_addition_id = Column(BigInteger, nullable=True)
    di_pu_addition_item_id = Column(BigInteger, nullable=True)
    addition_number = Column(Integer, default=0, nullable=False)
    num_item = Column(Integer, default=0, nullable=False)
    di_number = Column(String(255), nullable=True)
    di_digit = Column(String(255), nullable=True)
    di_date = Column(DateTime, nullable=True)
    keywords = Column(Text, nullable=True)
    description = Column(Text, nullable=True)
    denomination = Column(String(255), nullable=True)
    cpf_cnpj = Column(String(255), nullable=True)
    status = Column(String(255), default='untouched', nullable=False)
    is_archived = Column(Boolean, default=False, nullable=False)
    was_imported = Column(Boolean, default=False, nullable=False)
    product_image = Column(String(255), nullable=True)
    qtd_input_token = Column(Integer, nullable=True)
    qtd_output_token = Column(Integer, nullable=True)
    log_ai_finished_at = Column(DateTime, nullable=True)
    log_ai_error = Column(Text, nullable=True)
    filled_percentage = Column(Numeric(8, 2), nullable=True)
    portal_unico_code = Column(String(255), nullable=True)
    portal_unico_version = Column(String(255), nullable=True)
    portal_unico_created_at = Column(DateTime, nullable=True)
    portal_unico_updated_at = Column(DateTime, nullable=True)
    complementary_description = Column(Text, nullable=True)
    generated_ai_product_image = Column(Boolean, default=False, nullable=False)
    is_completed = Column(Boolean, default=False, nullable=False)
    is_published = Column(Boolean, default=False, nullable=False)
    is_awaiting_review = Column(Boolean, default=False, nullable=False)
    updated_not_published = Column(Boolean, default=False, nullable=False)
    line_business = Column(String(255), nullable=True)
    real_acquirer_id = Column(BigInteger, ForeignKey("real_acquirers.id"), nullable=True)
    is_publishing = Column(Boolean, default=False, nullable=True)
    
    # Relationships
    catalog_ncm = relationship("CatalogNcm", back_populates="catalog_ncm_items")
    real_acquirer = relationship("RealAcquirer", back_populates="catalog_ncm_items")
    catalog_ncm_item_attributes = relationship("CatalogNcmItemAttribute", back_populates="catalog_ncm_item")
    catalog_ncm_items_attributes = relationship("CatalogNcmItemAttributes", back_populates="catalog_ncm_item")
    internal_codes = relationship("CatalogNcmItemInternalCode", back_populates="catalog_ncm_item")
    foreign_operators = relationship("CatalogNcmItemsForeignOperator", back_populates="catalog_ncm_item")
    customer_published_items = relationship("CustomerPublishedItem", back_populates="catalog_ncm_item")
    request_review_items = relationship("RequestReviewItem", back_populates="catalog_ncm_item")
    
    __table_args__ = (
        Index("ccatalog_ncm_items_deleted_at_idx", "deleted_at"),
        Index("ccatalog_ncm_items_catalog_ncm_id_idx", "catalog_ncm_id"),
        Index("catalog_ncm_items_key_index", "key"),
        Index("catalog_ncm_items_is_published_index", "is_published"),
        Index("catalog_ncm_items_is_completed_index", "is_completed"),
        Index("catalog_ncm_items_is_archived_index", "is_archived"),
        Index("catalog_ncm_items_is_awaiting_review_index", "is_awaiting_review"),
        Index("catalog_ncm_items_filled_percentage_index", "filled_percentage"),
    ) 