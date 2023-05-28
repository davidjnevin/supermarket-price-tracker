from datetime import datetime
from typing import List

from pydantic import BaseModel

from app.models.product_listing import PriceHistory, ProductListing


class PricePayloadSchema(BaseModel):
    unit_price: float
    bulk_price: float
    unit_price_unit_type: str
    created_at: datetime
    updated_at: datetime
    product_id: int


class PriceResponseSchema(PricePayloadSchema):
    id: int

    class Config:
        orm_mode = True


class ProductPayloadSchema(BaseModel):
    site_origin: str
    product_id: int
    category_id: int
    name: str
    description: str
    image: str
    created_at: datetime
    updated_at: datetime
    prices: List[PriceResponseSchema]


class ProductResponseSchema(ProductPayloadSchema):
    id: int

    class Config:
        orm_mode = True
