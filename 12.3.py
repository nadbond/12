with open('en-ru.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

ru_en = {}

for line in lines:
    line = line.strip()
    if not line:
        continue

    if ' - ' in line:
        eng, rus = line.split(' - ')
    elif ' – ' in line:
        eng, rus = line.split(' – ')
    else:
        continue

    russian_words = rus.split(', ')

    for ru_word in russian_words:
        ru_word = ru_word.strip()

        if ru_word in ru_en:
            if eng not in ru_en[ru_word]:
                ru_en[ru_word].append(eng)
        else:
            ru_en[ru_word] = [eng]

for ru_word in ru_en:
    ru_en[ru_word] = ', '.join(ru_en[ru_word])

sorted_items = sorted(ru_en.items())

with open('ru-en.txt', 'w', encoding='utf-8') as f:
    for ru_word, eng_words in sorted_items:
        f.write(f"{ru_word} – {eng_words}\n")

print("Готово! Создан файл ru-en.txt")