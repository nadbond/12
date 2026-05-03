import json

with open('продукты.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

name = input("Название нового продукта: ")
price = int(input("Цена: "))
weight = int(input("Вес: "))
available = input("В наличии? (да/нет): ")

if available == "да":
    available = True
else:
    available = False

new_product = {"name": name, "price": price, "available": available, "weight": weight}
data["products"].append(new_product)

with open('продукты.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=2)

print()
for p in data["products"]:
    print(f"Название: {p['name']}")
    print(f"Цена: {p['price']}")
    print(f"Вес: {p['weight']}")
    if p["available"]:
        print("В наличии")
    else:
        print("Нет в наличии")
    print()