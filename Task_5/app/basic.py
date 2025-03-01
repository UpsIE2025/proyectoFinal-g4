from contextlib import contextmanager

from app.database import MariaDBSession


@contextmanager
def get_db():
    """
    Context manager for getting a database connection.

    This function returns a context manager that provides a database connection
    using the MariaDBSession class. The connection is automatically closed
    when the context is exited, and any exceptions that occur within the
    context are caught and the database transaction is rolled back.

    Usage:
    ```
    with get_db() as db:
        # Use the db connection here
    ```

    Returns:
    A database connection object.

    Raises:
    Any exception that occurs within the context.
    """
    db = MariaDBSession()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
