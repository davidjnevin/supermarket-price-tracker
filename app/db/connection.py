from sqlalchemy import create_engine

from app.db.config import DATABASE_URL

engine = create_engine(DATABASE_URL, pool_pre_ping=True, echo=True)
