def test_coach_list(api_client) -> None:
    '''
    Тестовый тест на тестовый endpoint
    '''
    response = api_client.get("/healthcheck/")
    data = response.json()

    assert response.status_code == 200
    assert data == {"message": "ok"}
