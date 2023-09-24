import pytest
from base_request import BaseRequest

BASE_URL = 'https://dog.ceo/api'
api = BaseRequest(BASE_URL)


def test_random_dog_image():
    """Проверка успешного ответа при запросе случайного изображения"""
    response = api.get('/breeds/image/random')
    response_data = response.json()
    assert response.status_code == 200
    assert 'message' in response_data
    assert response_data['status'] == 'success'


def test_all_breeds():
    """Проверка успешного ответа при запросе списка всех пород"""
    response = api.get('/breeds/list/all')
    response_data = response.json()
    assert response.status_code == 200
    assert 'message' in response_data
    assert response_data['status'] == 'success'


@pytest.mark.parametrize('breed_name', ['bulldog', 'poodle', 'corgi'])
def test_specific_breed_info(breed_name):
    """Проверка успешного ответа при запросе информации о конкретной породе"""
    response = api.get(f'/breed/{breed_name}/images/random')
    response_data = response.json()
    assert response.status_code == 200
    assert 'message' in response_data
    assert response_data['status'] == 'success'


@pytest.mark.parametrize('breed_name', ['beagle', 'boxer', 'akita'])
def test_random_images_for_breed(breed_name):
    """Проверка успешного ответа при запросе случайных изображений породы"""
    response = api.get(f'/breed/{breed_name}/images/random/3')
    response_data = response.json()
    assert response.status_code == 200
    assert 'message' in response_data
    assert response_data['status'] == 'success'


@pytest.mark.parametrize('breed_name', ['buhund', 'collie', 'retriever'])
def test_sub_breeds_for_breed(breed_name):
    """Проверка успешного ответа при запросе списка подпород для породы"""
    response = api.get(f'/breed/{breed_name}/list')
    response_data = response.json()
    assert response.status_code == 200
    assert 'message' in response_data
    assert response_data['status'] == 'success'
