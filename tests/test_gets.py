import os
import tempfile

import pytest

from property_search import property_search


@pytest.fixture
def client():
    db_fd, property_search.app.config['DATABASE'] = tempfile.mkstemp()
    property_search.app.config['TESTING'] = True

    with property_search.app.test_client() as client:
        yield client

def test_getting_selected_properties(client):
	response = client.get('/search/get')
	assert response.status_code == 200

def test_getting_all_properties(client):
	response = client.get('/search/data')
	assert response.status_code == 200