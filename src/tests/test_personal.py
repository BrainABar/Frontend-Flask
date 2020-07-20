def test_home(test_client):

    response = test_client.get('/')
    assert response.status_code == 200


def test_contact(test_client):

    response = test_client.get('/contact')
    assert response.status_code == 200
