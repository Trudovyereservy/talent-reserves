import pytest
from rest_framework.test import APIClient

from coaches.models import Coach, Direction


@pytest.mark.django_db
def test_coach_list(
    api_client: APIClient,
    ) -> None:
    """
    Тестирование доступности эндпоинта со списком тренеров.
    """
    response = api_client.get("/coaches/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_coach_id(
    api_client: APIClient,
    create_coaches: list[Coach],
    ) -> None:
    """
    Тестирование доступности эндпоинта c конкретным тренером.
    """
    response = api_client.get("/coaches/2/")
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
    response = api_client.get("/coaches/?limit=2")
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
    response = api_client.get("/coaches/?directions__slug=box")
    data = response.json()

    assert len(data["results"]) == 2
    assert "бокс" in data["results"][0]["directions"]
    assert "бокс" in data["results"][1]["directions"]


@pytest.mark.django_db
def test_coach_filtration(
    api_client: APIClient,
    create_coaches: list[Coach],
    ) -> None:
    """
    Тестирование поля "фамилия" в списке тренеров.
    """
    response = api_client.get("/coaches/")
    data = response.json()

    assert data["results"][2]["surname"] == "Белоцерковская"
