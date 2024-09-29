def display_recipe(cook_book):
    """Выводит все рецепты из кулинарной книги в заданном формате."""
    for dish, ingredients in cook_book.items():
        print(dish)
        print(len(ingredients))  # Вывод количества ингредиентов
        for ingredient in ingredients:
            print(f"{ingredient['ingredient_name']} | {ingredient['quantity']} | {ingredient['measure']}")
        print()  # Пустая строка для разделения рецептов


def add_recipe(cook_book):
    """Добавляет новый рецепт в кулинарную книгу."""
    dish = input("Введите название блюда: ")
    num_ingredients = int(input("Введите количество ингредиентов: "))

    ingredients = []
    for _ in range(num_ingredients):
        ingredient_name = input("Введите название ингредиента: ")
        quantity = float(input("Введите количество: "))
        measure = input("Введите единицу измерения: ")
        ingredients.append({
            'ingredient_name': ingredient_name,
            'quantity': quantity,
            'measure': measure
        })

    cook_book[dish] = ingredients
    print(f"Рецепт '{dish}' добавлен!")


def save_to_file(cook_book, filename):
    """Сохраняет кулинарную книгу в файл."""
    with open(filename, 'w', encoding='utf-8') as file:
        for dish, ingredients in cook_book.items():
            file.write(f"{dish}\n")
            file.write(f"{len(ingredients)}\n")
            for ingredient in ingredients:
                file.write(f"{ingredient['ingredient_name']} | {ingredient['quantity']} | {ingredient['measure']}\n")


def load_from_file(filename):
    """Загружает кулинарную книгу из файла."""
    cook_book = {}
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            i = 0
            while i < len(lines):
                dish = lines[i].strip()
                num_ingredients = int(lines[i + 1].strip())
                ingredients = []
                for j in range(num_ingredients):
                    ingredient_info = lines[i + 2 + j].strip().split(' | ')
                    ingredient_name = ingredient_info[0]
                    quantity = float(ingredient_info[1])
                    measure = ingredient_info[2]
                    ingredients.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
                cook_book[dish] = ingredients
                i += num_ingredients + 2
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")
    return cook_book


def main():
    cook_book = {
        'Омлет': [
            {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
            {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
            {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
        ],
        'Утка по-пекински': [
            {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
            {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
            {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
            {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
        ],
        'Запеченный картофель': [
            {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
            {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
            {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
        ]
    }

    filename = 'cook_book.txt'

    while True:
        print("1. Показать все рецепты")
        print("2. Добавить новый рецепт")
        print("3. Сохранить рецепты в файл")
        print("4. Загрузить рецепты из файла")
        print("5. Выход")

        choice = input("Выберите опцию: ")

        if choice == '1':
            display_recipe(cook_book)
        elif choice == '2':
            add_recipe(cook_book)
        elif choice == '3':
            save_to_file(cook_book, filename)
        elif choice == '4':
            cook_book = load_from_file(filename)
        elif choice == '5':
            break
        else:
            print("Неверный выбор, попробуйте снова.")


if __name__ == '__main__':
    main()