def cook_book(file):
    with open(file, 'r', encoding='utf-8') as file:
        file.seek(0)
        for line in file:
            cook_book = {}
            ingredients = []
            name_of_dish = line.strip()
            amount_of_ingredients = int(file.readline().strip())

            for i in range(amount_of_ingredients):
                name, count, measure = file.readline().strip().split('|')
                ingredients.append({'ingredient_name': name.strip(), 'quantity': int(count), 'measure': measure.strip()})
            file.readline()
            cook_book[name_of_dish] = ingredients
            print(cook_book)