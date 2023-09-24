import pytest
from base_request import BaseRequest

BASE_URL = 'https://jsonplaceholder.typicode.com'
api = BaseRequest(BASE_URL)


def test_get_users_status_code():
    """Проверка статус-кода при запросе списка пользователей"""
    response = api.get('/users')
    assert response.status_code == 200


@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_get_user_by_id_status_code(user_id):
    """Проверка статус-кода при запросе конкретного пользователя"""
    response = api.get(f'/users/{user_id}')
    assert response.status_code == 200


def test_create_new_post_status_code():
    """Проверка статус-кода при создании нового поста"""
    payload = {
        "title": "Test new post",
        "body": "This is a new test post.",
        "userId": 1
    }
    response = api.post(f'/posts', json=payload)
    assert response.status_code == 201


@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_update_post_status_code(post_id):
    """Проверка статус-кода при обновлении поста"""
    payload = {
        "title": "Updated post title",
        "body": "This post has been updated."
    }
    response = api.put(f'/posts/{post_id}', json=payload)
    assert response.status_code == 200


@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_delete_post_status_code(post_id):
    """Проверка статус-кода при удалении поста"""
    response = api.delete(f'/posts/{post_id}')
    assert response.status_code == 200
