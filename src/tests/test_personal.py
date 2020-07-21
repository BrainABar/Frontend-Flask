""" Test for personal blueprint """


def test_home(test_client):
    """ Test for index page """

    response = test_client.get('/')
    assert response.status_code == 200


def test_projects(test_client):
    """ Test for projects page """

    response = test_client.get('/projects')
    assert response.status_code == 200
