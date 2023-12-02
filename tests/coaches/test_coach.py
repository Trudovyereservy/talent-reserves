import pytest
from coaches.models import Coach, Direction

@pytest.mark.django_db
def test_create_coach() -> None:
    
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

    assert Coach.objects.count() == 2