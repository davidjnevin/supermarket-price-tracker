from fastapi import APIRouter

from app.api_routes import crud
from app.api_routes.schemas.pydantic import ProductPayloadSchema, ProductResponseSchema

router = APIRouter()


@router.post("/products", response_model=ProductResponseSchema, status_code=201)
async def create_product(payload: ProductPayloadSchema) -> ProductResponseSchema:
    product_id = await crud.post(payload)

    response_object = {
        "site_origin": payload.site_origin,
        "product_id": payload.product_id,
        "category_id": payload.category_id,
        "name": payload.name,
        "description": payload.description,
        "image": payload.image,
        "created_at": payload.created_at,
        "updated_at": payload.updated_at,
        "prices": [payload.prices],
    }
    return response_object
