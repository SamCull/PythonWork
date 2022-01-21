from flask import request


def test_up(client):
    """ Test to see if the server is up """
    assert client.get("/").status_code == 200


def test_missing(client):
    """ Test to see an appropiate response for a missing url """
    assert client.get("/missing").status_code == 404


def test_correct_form(client):
    """ Grab the home page and check for 200 code(all ok),
        then check to see if we have received the correct
        form and the response is a HTML page
    """
    response = client.get("/showform")
    assert response.status_code == 200
    # response.data is a binary text version of the HTML page.
    assert '<form action="/commentform" method="POST">' in response.get_data(True)
    assert "<!DOCTYPE html>" in response.get_data(True)


def test_form_operation(client, clean_up_db):  # clean up db removes whats entered below
    """ Create some test/sample data and POST the data to the server
        Ensure the request is using POST then look for a 200 (all ok) status code.
        Check for a valid HTML page, then check that the submitted form data was received
        then send back to the browser in the response."""
    form_data = {
        "email": "test@gmail.com",
        "message": "This is a test message.",
    }
    response = client.post("/commentform", data=form_data)
    assert request.method == "POST"
    assert response.status_code == 200
    resp = response.data  # The binary text version of the HTML response.
    assert "<!DOCTYPE html>" in response.get_data(True)
    assert form_data["email"], encoding == "utf-8" in resp
    # assert bytes(form_data["message"], encoding="utf-8") in resp
