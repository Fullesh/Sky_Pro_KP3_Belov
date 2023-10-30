def make_mask(acc_number_from, acc_number_to, description=''):
    string_acc_number_from = string_acc_number_to = masked_to = masked_from = ''
    position = 0
    if description == 'Открытие вклада':
        masked_to = '**' + acc_number_to[-4:]
        return masked_to
    else:
        if len(acc_number_to) == 20:
            masked_to = '**' + acc_number_to[-4:]
        if len(acc_number_from) == 20:
            masked_from = '**' + acc_number_from[-4:]
        if len(acc_number_to) or len(acc_number_from) == 16:
            for i in range(5):
                string_acc_number_from += (acc_number_from[position:position+4] + ' ')
                string_acc_number_to += (acc_number_to[position:position+4] + ' ')
                position += 4
            string_acc_number_from = string_acc_number_from.rstrip()
            string_acc_number_to = string_acc_number_to.rstrip(' ')
            if len(acc_number_to) == 16:
                for j in range(len(string_acc_number_to)):
                    if 7 <= j <= 14 and string_acc_number_to[j] != ' ':
                        masked_to += string_acc_number_to[j].replace(string_acc_number_to[j], '*')
                    else:
                        masked_to += string_acc_number_to[j]
            if len(acc_number_from) == 16:
                for j in range(len(string_acc_number_from)):
                    if 7 <= j <= 14 and string_acc_number_from[j] != ' ':
                        masked_from += string_acc_number_from[j].replace(string_acc_number_from[j], '*')
                    else:
                        masked_from += string_acc_number_from[j]
        return masked_from, masked_to
