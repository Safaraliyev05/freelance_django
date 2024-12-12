import pytest
from rest_framework import status
from rest_framework.reverse import reverse_lazy


@pytest.mark.django_db
class TestFilters:
    def test_search_users(self, client, users):
        url = reverse_lazy('user-list')
        key = 'hello'
        query = {
            'search': key
        }
        response = client.get(url, query)
        assert response.status_code == status.HTTP_200_OK
        data = response.json()

        for user in data:
            assert key.lower() in user['username'].lower()
