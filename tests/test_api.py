from unittest.mock import patch
from src.interface.services.clima import pegar_clima


def test_pegar_clima():
    mock_response = {
        "main": {
            "temp": 30,
            "humidity": 20,
            "feels_like": 32
        },
        "weather": [
            {"description": "céu limpo"}
        ],
        "wind": {
            "speed": 5
        },
        "name": "Brasília"
    }

    class MockResponse:
        status_code = 200

        def json(self):
            return mock_response

    with patch("src.interface.services.clima.requests.get", return_value=MockResponse()):
        resultado = pegar_clima()

        assert resultado is not None
        assert resultado["temp"] == 30
        assert resultado["umidade"] == 20
        assert resultado["sensacao"] == 32
        assert resultado["cidade"] == "Brasília"
