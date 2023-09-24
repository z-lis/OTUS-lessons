import pytest
from base_request import BaseRequest

BASE_URL = 'https://api.openbrewerydb.org/v1/breweries'
api = BaseRequest(BASE_URL)


def test_successful_request_status_code():
    """Проверка статус-кода при успешном запросе случайной пивоварни"""
    response = api.get('/random')
    assert response.status_code == 200


def test_brewery_by_id():
    """Проверка наличия определенной пивоварни по ID"""
    brewery_id = '1dc3e29e-702f-42df-9561-aead46dce8f3'
    response = api.get(f'/{brewery_id}')
    response_data = response.json()
    assert response.status_code == 200
    assert response_data['id'] == brewery_id


@pytest.mark.parametrize('brewery_city', ['San Diego', 'Worcester', 'Cincinnati'])
def test_filter_breweries_by_city(brewery_city):
    """Проверка фильтрации по городу пивоварни"""
    params = {'by_city': brewery_city}
    response = api.get(path='', params=params)
    response_data = response.json()
    assert response.status_code == 200
    for brewery in response_data:
        assert brewery['city'] == brewery_city


def test_search_brewery_by_name():
    """Проверка поиска по имени пивоварни"""
    search_name = 'dog'
    params = {'query': search_name, 'per_page': 10}
    response = api.get(path='/search', params=params)
    response_data = response.json()
    assert response.status_code == 200
    for brewery in response_data:
        assert search_name.lower() in brewery['name'].lower()


@pytest.mark.parametrize('per_page', [5, 10, 100])
def test_sort_breweries_per_page(per_page):
    """Проверка количества пивоварен при запросе"""
    params = {'per_page': per_page}
    response = api.get(path='', params=params)
    response_data = response.json()
    assert response.status_code == 200
    assert len(response_data) == per_page
