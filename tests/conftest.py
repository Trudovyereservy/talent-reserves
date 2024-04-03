import pytest
from rest_framework.test import APIClient

from blog.models import Post, Tag
from coaches.models import Coach, Direction
from news.models import ContentNews, News


@pytest.fixture(scope="function")
def api_client() -> APIClient:
    '''
    Фикстура для использования APIClient.
    '''
    yield APIClient()


@pytest.fixture(scope="function")
def create_coaches(db) -> list[Coach]:
    '''
    Фикстура для создания тестовых направлений и тренеров.

    '''
    Direction.objects.bulk_create([
        Direction(id=1, title='бокс', slug='box'),
        Direction(id=2, title='лыжи', slug='ski'),
        Direction(id=3, title='биатлон', slug='biathlon')
    ])

    test_coach_1 = Coach.objects.create(
        surname='Поддубный',
        name='Иван',
        patronymic='Максимович',
        birthday='1871-10-08',
        achievements='Шестикратный чемпион мира',
        photo='',
    )
    test_coach_1.directions.add(
        Direction.objects.get(id=1),
    )

    test_coach_2 = Coach.objects.create(
        surname='Тихонов',
        name='Александр',
        patronymic='Иванович',
        birthday='1947-01-02',
        achievements='Четырехкратный олимпийский чемпион',
        photo='',
    )
    test_coach_2.directions.add(
        Direction.objects.get(id=2),
        Direction.objects.get(id=3)
    )

    test_coach_3 = Coach.objects.create(
        surname='Белоцерковская',
        name='Юлия',
        patronymic='Николаевна',
        birthday='1985-07-05',
        achievements=('Чемпионка мира по лыжным гонкам ',
                      'и по боксу в легком весе'),
        photo='',
    )
    test_coach_3.directions.add(
        Direction.objects.get(id=2),
        Direction.objects.get(id=1)
    )

    return [test_coach_1, test_coach_2, test_coach_3]


@pytest.fixture(scope="function")
def create_news(db) -> list[News]:
    """
    Фикстура для создания тестовых новсотей.
    """
    Tag.objects.bulk_create([
        Tag(id=1, name='Новости дня', slug='daily_news'),
        Tag(id=2, name='Спортивные события', slug='sport_events')
    ])
    news_1 = News.objects.create(
            title='Новость 1',
            description='Особо важная 1',
            date_published='2023-12-07T07:01:21Z',
    )
    news_1.tags.add(
        Tag.objects.get(id=1),
    )
    news_2 = News.objects.create(
            title='Новость 2',
            description='Особо важная 2',
            date_published='2023-12-07T07:01:22Z',
    )
    news_2.tags.add(
        Tag.objects.get(id=1),
    )
    contentnews_1 = ContentNews.objects.create(
        news=news_1,
        # image="test_image1.jpg",
        title_photo="Test Title 1",
        author_photo="Test Author 1",
        )
    contentnews_2 = ContentNews.objects.create(
        news=news_2,
        # image="test_image2.jpg",
        title_photo="Test Title 2",
        author_photo="Test Author 2",
        )
    contentnews_3 = ContentNews.objects.create(
        news=news_2,
        # image="test_image3.jpg",
        title_photo="Test Title 3",
        author_photo="Test Author 3",
        )
    return [news_1, news_2, contentnews_1, contentnews_2, contentnews_3]


@pytest.fixture(scope="function")
def create_posts(db):
    '''Fixture to create posts.'''
    Tag.objects.bulk_create([
        Tag(id=1, name='events', slug='events'),
        Tag(id=2, name='exercises', slug='exercises')
    ])

    test_post1 = Post.objects.create(
        text='В воскресенье, 15 декабря 2023 года, состоятся соревнования.',
        short_description='Соревнования',
        publication_date='2023-11-20',
    )
    test_post1.tags.add(
        Tag.objects.get(id=1),
    )

    test_post2 = Post.objects.create(
        text='Упражнения для укрепления мышц спины',
        short_description='Мышцы спины',
        publication_date='2023-11-30',
    )
    test_post2.tags.add(
        Tag.objects.get(id=2),
    )

    test_post3 = Post.objects.create(
        text='5 декабря наша команда едет на соревнования в Москву.',
        short_description='Соревнования в Москве',
        publication_date='2023-11-20',
    )
    test_post3.tags.add(
        Tag.objects.get(id=1),
    )

    return [test_post1, test_post2, test_post3]
