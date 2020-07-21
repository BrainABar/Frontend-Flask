def test_home(test_client):

    response = test_client.get('/')
    assert response.status_code == 200


def test_projects(test_client):

    response = test_client.get('/projects')
    assert response.status_code == 200
