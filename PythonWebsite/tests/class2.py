def test_correct_format(client):
    """
        Test to ensure we have a list of lists, and the embedded list
        contains four items
    """
    resp = client.get("/getdata")
    assert resp.status_code == 200
    json = resp.data
    assert isinstance(json, list)  # Is this an outer list?
    assert isinstance(json[0], list)  # Is this a list inside the outer list?
    assert len(json[0]) == 4  # Does the embedded list contain 4 items?
