from sqlalchemy import Column, Integer, BigInteger, String, Boolean, DateTime, ForeignKey, Index
from sqlalchemy.orm import relationship
from ..database.config import Base
from .base_models import TimestampMixin

class CatalogNcmItemsForeignOperator(Base, TimestampMixin):
    __tablename__ = "catalog_ncm_items_foreign_operator"

    id = Column(BigInteger, primary_key=True)
    catalog_ncm_items_id = Column(Integer, ForeignKey("catalog_ncm_items.id"), nullable=False)
    foreign_operator_id = Column(Integer, ForeignKey("foreign_operator.id"), nullable=False)
    
    # Relationships
    catalog_ncm_item = relationship("CatalogNcmItem", back_populates="foreign_operators")
    foreign_operator = relationship("ForeignOperator", back_populates="catalog_ncm_items_foreign_operators")
    
    __table_args__ = (
        Index("catalog_ncm_items_foreign_operator_catalog_ncm_items_id_index", "catalog_ncm_items_id"),
        Index("catalog_ncm_items_foreign_operator_foreign_operator_id_index", "foreign_operator_id"),
        Index("catalog_ncm_items_foreign_operator_deleted_at_index", "deleted_at"),
    ) 