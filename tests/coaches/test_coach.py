from coaches.models import Coach, Direction


def test_create_coach(db) -> None:
    
    Direction.objects.bulk_create([
        Direction(name='бокс', slug='box'),
        Direction(name='лыжи', slug='ski'),
        Direction(name='биатлон', slug='biathlon')
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

    assert test_coach_1.username == 'Иван'