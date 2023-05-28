from datetime import datetime, timezone
from typing import List, Optional

from sqlalchemy import DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from app.db.connection import engine


class Base(DeclarativeBase):
    pass


class ProductListing(Base):
    __tablename__ = "product_listing"

    id: Mapped[int] = mapped_column(primary_key=True)
    site_origin: Mapped[str] = mapped_column(String(50))
    product_id: Mapped[int] = mapped_column(Integer)
    category_id: Mapped[str] = mapped_column(Integer)
    name: Mapped[str] = mapped_column(String(50))
    description: Mapped[Optional[str]] = mapped_column(String(100))
    image: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), onupdate=datetime.now(timezone.utc)
    )
    # One-Many relationship
    prices: Mapped[List["PriceHistory"]] = relationship()

    def __repr__(self) -> str:
        return f"ProductListing(id={self.id!r}, site_origin={self.site_origin!r}, product_id={self.product_id!r}, category_id={self.category_id!r}, name={self.name!r}, description={self.description!r}, image={self.image!r})"  # noqa : E501


class PriceHistory(Base):
    __tablename__ = "price_history"

    id: Mapped[int] = mapped_column(primary_key=True)
    unit_price: Mapped[float] = mapped_column(Float)
    bulk_price: Mapped[Optional[float]] = mapped_column(Float)
    unit_price_unit_type: Mapped[Optional[str]] = mapped_column(String(50))
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )
    product_id: Mapped[int] = mapped_column(ForeignKey("product_listing.id"))

    def __repr__(self) -> str:
        return f"PriceHistory(id={self.id!r}, unit_price={self.unit_price!r}, bulk_price={self.bulk_price!r}, unit_price_unit_type={self.unit_price_unit_type!r}, product_id={self.product_id!r}, created_at={self.created_at!r} )"  # noqa : E501


def create_product_listing():
    Base.metadata.create_all(engine, checkfirst=True)
