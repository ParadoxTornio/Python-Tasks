name_of_product = input()
price_of_product = int(input())
weight_of_product = int(input())
price = price_of_product * weight_of_product
string_price = str(price)
money_of_user = int(input())
print('================Чек================')
second_line = (35 - 6 - len(name_of_product)) * ' '
print(f'Товар:{second_line}{name_of_product}')
third_line = (
    35 - 5 - len(f'{weight_of_product}кг * {price_of_product}руб/кг')) * ' '
print(f'Цена:{third_line}{weight_of_product}кг * {price_of_product}руб/кг')
fourth_line = (35 - 6 - len(f'{string_price}руб')) * ' '
print(f'Итого:{fourth_line}{price}руб')
fifth_line = (35 - 8 - len(f'{money_of_user}руб')) * ' '
print(f'Внесено:{fifth_line}{money_of_user}руб')
change = money_of_user - price
sixth_line = (35 - 6 - len(f'{money_of_user - price}руб')) * ' '
print(f'Сдача:{sixth_line}{money_of_user - price}руб')
print('===================================')
