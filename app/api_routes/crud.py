from app.api_routes.schemas.pydantic import ProductPayloadSchema
from app.models.product_listing import ProductListing


async def post(payload: ProductPayloadSchema) -> int:
    product = ProductListing(
        site_origin=payload.site_origin,
        product_id=payload.product_id,
        category_id=payload.category_id,
        name=payload.name,
        description=payload.description,
        image=payload.image,
        created_at=payload.created_at,
        updated_at=payload.updated_at,
        prices=payload.prices,
    )
    await product.save()
    return product.id
