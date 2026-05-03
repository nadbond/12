import json

with open('продукты.json', 'r', encoding='utf-8') as file:
    reader = json.load(file)

for product in reader['products']:
    print(f"Название: {product['name']}")
    print(f"Цена: {product['price']}")
    print(f"Вес: {product['weight']}")

    if product ['available']:
     print("В наличии")
    else:
     print("Нет в наличии!")
    print()
