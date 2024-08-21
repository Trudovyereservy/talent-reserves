import pytest
from django.core.paginator import Paginator
from news.models import ContentNews, News
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_list_news(api_client: APIClient) -> None:
    """
    Тест на доступ эндпоинта списка новостей.
    """
    response = api_client.get("/api/news/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_news_id(
        api_client: APIClient,
        create_news: list[News],
        ) -> None:
    """
    Тестирование доступности эндпоинта выбранной новости.
    """
    response = api_client.get("/api/news/1/")
    assert response.status_code == 200
    assert response.json()['title'] == 'Новость 1'


@pytest.mark.django_db
def test_content_news(create_news: list[News],) -> None:
    """
    Тестирование, что все новости созданы и фото-контент принадлежит
    определенной новости.
    """
    assert News.objects.count() == 2
    assert ContentNews.objects.filter(news=create_news[1]).count() == 2


@pytest.mark.django_db
def test_pagination_news(api_client: APIClient):
    """
    Тестирование пагинации, создаем несколько новостей, тестируем отображение
    заданного числа, что данные пагинируются, подтверждаем количеством страниц,
    сравниваем сколько новостей должно остаться на последней странице.
    """
    news_all = News.objects.bulk_create(
        [
            News(
                title=f'Новость {i}',
                description=f'Особо важная новость {i}',
                date_published='2023-12-07T07:01:21Z',
            )
            for i in range(15)
        ]
    )

    response = api_client.get("/api/news/?limit=9")

    data = response.json()
    assert 'results' in data
    assert 'count' in data
    assert 'next' in data
    assert 'previous' in data

    results = data['results']
    assert len(results) == 9

    paginator = Paginator(news_all, 9)
    assert paginator.num_pages == 2

    response2 = api_client.get("/api/news/"+'?page=2')
    data2 = response2.json()
    results2 = data2['results']
    assert len(results2) == 6


@pytest.mark.django_db
def test_tags_filtration(api_client: APIClient,
                         create_news: list[News],):
    """Тестирование фильтрации тегов."""
    response = api_client.get('/api/news/?tags_ids=1')
    data = response.json()

    assert len(data['results']) == 2
