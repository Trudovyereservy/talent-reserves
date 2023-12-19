import pytest

from blog.models import Post, Tag, TagPost, ContentPost


@pytest.mark.django_db
def test_get_post_list(api_client):
    """ Тестирование доступности эндпоинта со списком постов."""
    response = api_client.get('/post/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_post_detail(api_client, create_posts):
    """ Тестирование доступности эндпоинта c постом."""
    response = api_client.get('/post/2/')
    assert response.status_code == 200
    assert response.json()['short_description'] == 'Мышцы спины'


@pytest.mark.django_db
def test_posts_pagination(api_client, create_posts):
    """Тестирование пагинации списка постов."""
    response = api_client.get('/post/?limit=3')
    data = response.json()

    assert len(data['results']) == 3


@pytest.mark.django_db
def test_tags_filtration(api_client, create_posts):
    """Тестирование фильтрации тегов."""
    response = api_client.get('/post/?tags_ids=2')
    data = response.json()

    assert len(data['results']) == 1
