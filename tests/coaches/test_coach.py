import pytest
from coaches.models import Coach
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_coach_list(
    api_client: APIClient,
    ) -> None:
    """
    Тестирование доступности эндпоинта со списком тренеров.
    """
    response = api_client.get("/api/coaches/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_coach_id(
    api_client: APIClient,
    create_coaches: list[Coach],
    ) -> None:
    """
    Тестирование доступности эндпоинта c конкретным тренером.
    """
    response = api_client.get("/api/coaches/2/")
    assert response.status_code == 200
    assert response.json()["name"] == "Александр"


@pytest.mark.django_db
def test_coach_pagination(
    api_client: APIClient,
    create_coaches: list[Coach],
    ) -> None:
    """
    Тестирование пагинации списка тренеров.
    Требуется вывести - 2 тренера.
    """
    response = api_client.get("/api/coaches/?limit=2")
    data = response.json()

    assert len(data["results"]) == 2


@pytest.mark.django_db
def test_coach_filtration(
    api_client: APIClient,
    create_coaches: list[Coach],
    ) -> None:
    """
    Тестирование фильтрации списка тренеров по направлению работы.
    Требуется вывести тренеров с направлением "бокс".
    """
    response = api_client.get("/api/coaches/?direction_ids=1")
    data = response.json()

    assert len(data["results"]) == 2


@pytest.mark.django_db
def test_coach_surname(
    api_client: APIClient,
    create_coaches: list[Coach],
    ) -> None:
    """
    Тестирование поля "фамилия" в списке тренеров.
    """
    response = api_client.get("/api/coaches/")
    data = response.json()

    assert data["results"][2]["surname"] == "Белоцерковская"
