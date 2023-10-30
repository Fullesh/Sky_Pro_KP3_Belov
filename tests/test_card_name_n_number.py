from src.card_name_n_number import get_card_info


def test_get_card_info():
    assert get_card_info({
        "id": 596171168,
        "state": "EXECUTED",
        "date": "2018-07-11T02:26:18.671407",
        "operationAmount": {
            "amount": "79931.03",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Открытие вклада",
        "to": "Счет 72082042523231456215"
    }, 'Открытие вклада') == ('72082042523231456215', 'Счет')
    assert get_card_info({
        "id": 716496732,
        "state": "EXECUTED",
        "date": "2018-04-04T17:33:34.701093",
        "operationAmount": {
          "amount": "40701.91",
          "currency": {
            "name": "USD",
            "code": "USD"
          }
        },
        "description": "Перевод организации",
        "from": "Visa Gold 5999414228426353",
        "to": "Счет 72731966109147704472"
  }, 'Перевод организации') == ('5999414228426353', '72731966109147704472', 'Visa Gold', 'Счет')
