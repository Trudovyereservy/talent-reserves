import pytest

from rest_framework.test import APIClient

from coaches.models import Coach, Direction


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
        Direction(title='бокс', slug='box'),
        Direction(title='лыжи', slug='ski'),
        Direction(title='биатлон', slug='biathlon')
    ])

    test_coach_1 = Coach.objects.create(
            surname = 'Поддубный',
            name = 'Иван',
            patronymic = 'Максимович',
            birthday = '1871-10-08',
            achievements = 'Шестикратный чемпион мира',
            photo = '',
    )
    test_coach_1.directions.add(
        Direction.objects.get(slug='box'),
    )

    test_coach_2 = Coach.objects.create(
            surname = 'Тихонов',
            name = 'Александр',
            patronymic = 'Иванович',
            birthday = '1947-01-02',
            achievements = 'Четырехкратный олимпийский чемпион',
            photo = '',
    )
    test_coach_2.directions.add(
        Direction.objects.get(slug='ski'),
        Direction.objects.get(slug='biathlon')
    )

    test_coach_3 = Coach.objects.create(
            surname = 'Белоцерковская',
            name = 'Юлия',
            patronymic = 'Николаевна',
            birthday = '1985-07-05',
            achievements = ('Чемпионка мира по лыжным гонкам ',
                            'и по боксу в легком весе'),
            photo = '',
    )
    test_coach_3.directions.add(
        Direction.objects.get(slug='ski'),
        Direction.objects.get(slug='box')
    )

    return [test_coach_1, test_coach_2, test_coach_3]
