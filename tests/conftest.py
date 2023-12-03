import pytest

from rest_framework.test import APIClient

from blog.models import Post, Tag


@pytest.fixture(scope="function")
def api_client() -> APIClient:
    """
    Fixture to provide an API client
    :return: APIClient
    """
    yield APIClient()


@pytest.fixture(scope="function")
def create_posts(db):
    '''Fixture to create posts.'''
    Tag.objects.bulk_create([
        Tag(name='События', slug='events'),
        Tag(name='Упражнения', slug='exercises')
    ])

    test_post1 = Post.objects.create(
        text='В воскресенье, 15 декабря 2023 года, состоятся соревнования.',
        short_description='Соревнования',
        publication_date='2023-11-20',
        image='',
    )
    test_post1.tags.add(
        Tag.objects.get(slug='events'),
    )

    test_post2 = Post.objects.create(
        text='Упражнения для укрепления мышц спины',
        short_description='Мышцы спины',
        publication_date='2023-11-30',
        image='',
    )
    test_post2.tags.add(
        Tag.objects.get(slug='exercises'),
    )

    test_post3 = Post.objects.create(
        text='5 декабря наша команда едет на соревнования в Москву.',
        short_description='Соревнования в Москве',
        publication_date='2023-11-20',
        image='',
    )
    test_post3.tags.add(
        Tag.objects.get(slug='events'),
    )

    return [test_post1, test_post2, test_post3]
