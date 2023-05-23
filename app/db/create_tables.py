from sqlalchemy import create_engine

from app.db.config import DATABASE_URL
from app.models.product_listing import create_product_listing

engine = create_engine(DATABASE_URL, echo=True)


def create_tables():
    create_product_listing()


if __name__ == "__main__":
    create_tables()
