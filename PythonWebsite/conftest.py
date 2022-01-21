import pytest
import app as webapp
import DBcm

from appconfig import config


@pytest.fixture
def app():
    """
    This fixture creates the client object before each test runs, assuming
    the test references the client object
    """
    app = webapp.app
    return app


@pytest.fixture
def clean_up_db():
    """
    This code removes any and all test data from the database *after" the
    tests which refer to it run
    """

    # This code before the yield runs before the test runs
    yield
    # This code after the yield runs after the test completes
    with DBcm.UseDatabase(config) as db:
        SQL = """
            delete from comments
            where email = "test@gmail.com"
        """
        db.execute(SQL)
