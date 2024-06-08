# (Не) Активное похудение 🏃🌶️

weight_loss_day = int(input())
weight = float(input())

if weight <= 100 - (0.2 * weight_loss_day):
    print("Все идет по плану")
    print(f"#{weight_loss_day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {weight} кг, ЦЕЛЬ по ВЕСУ = {100 - (0.2 * weight_loss_day)} кг")
else:
    print("Что-то пошло не так")
    print(f"#{weight_loss_day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {weight} кг, ЦЕЛЬ по ВЕСУ = {100 - (0.2 * weight_loss_day)} кг")