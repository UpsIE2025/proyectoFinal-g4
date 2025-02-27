from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

import os

DATABASE_MARIADB_URL = os.getenv("DATABASE_MARIADB_URL")
DATABASE_POSTGRES_URL = os.getenv("DATABASE_POSTGRES_URL")

mariadb_engine = create_engine(DATABASE_MARIADB_URL)
postgresql_engine = create_engine(DATABASE_POSTGRES_URL)
Base = declarative_base()

MariaDBSession = sessionmaker(bind=mariadb_engine)
PostgreSQLSession = sessionmaker(bind=postgresql_engine)
PostgresBase = declarative_base()

