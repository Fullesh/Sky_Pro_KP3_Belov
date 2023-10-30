import json
import datetime as dt
from src.make_mask import make_mask
from src.card_name_n_number import get_card_info
from src.date_format import format_date

with open('operations.json', 'r', encoding='UTF-8') as json_file:
    data_json = json.load(json_file)

results = []
non_empty_data_json = [d for d in data_json if 'date' in d]
sorted_data_json = sorted(non_empty_data_json, key=lambda x: dt.datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'),
                          reverse=True)

for data in sorted_data_json:
    if data['state'] == 'EXECUTED':
        operation_date = format_date(data['date'])
        if data['description'] == 'Открытие вклада':
            card_number_to, card_name_to = get_card_info(data, data['description'])
            to_acc, _ = make_mask(card_number_to, data['description'])
            results.append(f'{operation_date} {data["description"]} \n'
                           f'{card_name_to} {to_acc} \n'
                           f'{data["operationAmount"]["amount"]} '
                           f'{data["operationAmount"]["currency"]["name"]}')
        else:
            card_number_from, card_number_to, card_name_from, card_name_to = get_card_info(data, data['description'])
            from_acc, to_acc = make_mask(card_number_from, card_number_to, data['description'])
            results.append(f'{operation_date} {data["description"]} \n'
                           f'{card_name_from} {from_acc} -> {card_name_to} {to_acc} \n'
                           f'{data["operationAmount"]["amount"]} '
                           f'{data["operationAmount"]["currency"]["name"]}')

for i in range(5):
    print(results[i])
    print(' ')
