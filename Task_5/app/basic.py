from contextlib import contextmanager

from app.database import MariaDBSession


@contextmanager
def get_db():
    db = MariaDBSession()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
