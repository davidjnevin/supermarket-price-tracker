from app.models.product_listing import create_product_listing


def create_tables():
    create_product_listing()


if __name__ == "__main__":
    create_tables()
