def test_get_ok(api_client) -> None:
    '''
    Тестовый тест на тестовый endpoint
    '''
    response = api_client.get("/api/healthcheck/")
    data = response.json()

    assert response.status_code == 200
    assert data == {"message": "ok"}
