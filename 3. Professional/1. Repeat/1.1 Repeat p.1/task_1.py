# Функция hide_card()

def hide_card(card_number):
    if " " in card_number:
        card_number_arr = card_number.split()
        result_number = "".join(card_number_arr)
        result_number = "*" * 12 + result_number[-4:]
    else:
        result_number = "*" * 12 + card_number[-4:]
    
    return result_number