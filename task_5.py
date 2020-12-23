revenue: int = int(input("Введите выручку: "))
costs = int(input("Введите издержки: "))
if revenue > costs:
    profit_margin = revenue - costs
    rent = profit_margin / revenue
    print(rent)  # рентабельность предприятия
    print(f"Отлично поработали, наша прибыль составила:  {profit_margin} у.е!")
    employee = int(input("Введите количество сотрудников: "))
    print(f"На одного сотрудника приходится {profit_margin / employee} у.е прибыли")
elif revenue == costs:
    print("Неплохо, но надо сократить расходы!")
else:
    print("без комментариев...")