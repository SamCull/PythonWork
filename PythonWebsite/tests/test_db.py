import DBcm

from appconfig import config


def test_running_locally():
    """Check to ensure the config is running for local settings"""
    assert config["host"] == "127.0.0.1"


def test_count_increase(client, clean_up_db):
    """Check to ensure the number of rows in the database incremented by 1"""
    # Go get the count of rows.

    with DBcm.UseDatabase(config) as db:
        SQL = "select count(*) from comments"
        db.execute(SQL)
        results = db.fetchall()
    initial_count = results[0][0]  # We get back a list of tuples

    form_data = {
        "email": "test@gmail.com",
        "message": "test message",
    }
    # Send the data to webapp using the FORM's URL
    client.post("/savedata", data=form_data)

    # Go get the count of rows and check that it is +1

    with DBcm.UseDatabase(config) as db:
        SQL = "select count(*) from comments"
        db.execute(SQL)
        results = db.fetchall()
    new_count = results[0][0]  # We get back a list of tuples


# assert new_count == initial_count + 1


def test_last_row(client, clean_up_db):
    """Is the last row of data equal to what was submitted via the form?"""
    form_data = {
        "email": "test@gmail.com",
        "message": "test message",
    }
    # Send the data to webapp using the FORM's URL
    client.post("/commentform", data=form_data)

    with DBcm.UseDatabase(config) as db:
        SQL = """
        select email, message, time
        from comments
        order by id desc
        limit 1
        """
        db.execute(SQL)
        results = db.fetchall()
    assert results[0][0] == form_data["email"]
    assert results[0][1] == form_data["message"]
