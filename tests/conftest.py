import pytest
from rest_framework.test import APIClient

from news.models import ContentNews, News


@pytest.fixture(scope="function")
def api_client() -> APIClient:
    """
    Fixture to provide an API client
    :return: APIClient
    """
    yield APIClient()


@pytest.fixture(scope="function")
def create_news(db) -> list[News]:
    """
    Фикстура для создания тестовых новсотей.
    """
    news_1 = News.objects.create(
            title='Новость 1',
            description='Особо важная 1',
            date_published='2023-12-07T07:01:21Z',
    )
    news_2 = News.objects.create(
            title='Новость 2',
            description='Особо важная 2',
            date_published='2023-12-07T07:01:22Z',
    )
    contentnews_1 = ContentNews.objects.create(
        news=news_1,
        image="test_image1.jpg",
        title_photo="Test Title 1",
        author_photo="Test Author 1",
        )
    contentnews_2 = ContentNews.objects.create(
        news=news_2,
        image="test_image2.jpg",
        title_photo="Test Title 2",
        author_photo="Test Author 2",
        )
    contentnews_3 = ContentNews.objects.create(
        news=news_2,
        image="test_image3.jpg",
        title_photo="Test Title 3",
        author_photo="Test Author 3",
        )
    return [news_1, news_2, contentnews_1, contentnews_2, contentnews_3]
