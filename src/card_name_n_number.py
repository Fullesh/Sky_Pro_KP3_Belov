def get_card_info(data, description):
    if description == 'Открытие вклада':
        acc_full_info_to = data['to'].split()
        card_number_to = acc_full_info_to[-1]
        acc_full_info_to.remove(card_number_to)
        card_name_to = ' '.join(acc_full_info_to)
        return card_number_to, card_name_to
    else:
        acc_full_info_from = data['from'].split()
        acc_full_info_to = data['to'].split()
        card_number_from = acc_full_info_from[-1]
        card_number_to = acc_full_info_to[-1]
        acc_full_info_from.remove(card_number_from)
        acc_full_info_to.remove(card_number_to)
        card_name_from = ' '.join(acc_full_info_from)
        card_name_to = ' '.join(acc_full_info_to)
        return card_number_from, card_number_to, card_name_from, card_name_to
