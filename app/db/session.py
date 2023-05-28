from sqlalchemy.orm import sessionmaker

from app.db.connection import engine

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
