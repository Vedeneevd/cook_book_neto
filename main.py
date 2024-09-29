def load_recipes(filename):
    """Загрузка рецептов из файла."""
    recipes = {}
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            index = 0

            while index < len(lines):
                recipe_name = lines[index].strip()
                index += 1

                if index >= len(lines):
                    break

                num_ingredients = int(lines[index].strip())
                index += 1

                ingredients = []
                for _ in range(num_ingredients):
                    if index < len(lines):
                        part = lines[index].strip().split(' | ')
                        ingredient = {
                            'ingredient_name': part[0],
                            'quantity': float(part[1]),
                            'measure': part[2]
                        }
                        ingredients.append(ingredient)
                        index += 1

                recipes[recipe_name] = ingredients
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")

    return recipes


def save_to_file(cook_book, filename):
    """Сохраняет кулинарную книгу в файл."""
    with open(filename, 'w', encoding='utf-8') as file:
        for dish, ingredients in cook_book.items():
            file.write(f"{dish}\n")
            file.write(f"{len(ingredients)}\n")
            for ingredient in ingredients:
                file.write(f"{ingredient['ingredient_name']} | {ingredient['quantity']} | {ingredient['measure']}\n")
            file.write("\n")  # Пустая строка для разделения рецептов


def print_recipes(recipes):
    """Вывод всех рецептов на экран."""
    if not recipes:
        print("Нет доступных рецептов.")
        return

    for name, ingredients in recipes.items():
        print(f"Рецепт: {name}")
        print("Ингредиенты:")
        for ingredient in ingredients:
            print(f"- {ingredient['ingredient_name']} | {ingredient['quantity']} | {ingredient['measure']}")
        print("-" * 40)


def add_recipe(filename):
    """Добавление нового рецепта."""
    recipe_name = input("Введите название рецепта: ")
    num_ingredients = int(input("Введите количество ингредиентов: "))
    ingredients = []

    for _ in range(num_ingredients):
        ingredient_name = input("Введите название ингредиента: ")
        quantity = float(input("Введите количество ингредиента: "))
        measure = input("Введите единицы измерения: ")
        ingredient = {
            'ingredient_name': ingredient_name,
            'quantity': quantity,
            'measure': measure
        }
        ingredients.append(ingredient)

    return recipe_name, ingredients

def get_shop_list_by_dishes(dishes, person_count, cook_book):
    """Возвращает список ингредиентов по заданным блюдам и количеству персон."""
    shop_list = {}

    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                ingredient_name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']

                if ingredient_name not in shop_list:
                    shop_list[ingredient_name] = {
                        'measure': measure,
                        'quantity': quantity
                    }
                else:
                    shop_list[ingredient_name]['quantity'] += quantity

    shop_list = get_shop_list_by_dishes(['Омлет'], 4, cook_book)

    return shop_list




def main():
    """Главная функция программы."""
    filename = 'recipes.txt'
    cook_book = load_recipes(filename)

    while True:
        print("1. Показать рецепты")
        print("2. Добавить новый рецепт")
        print("3. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            print_recipes(cook_book)
        elif choice == '2':
            recipe_name, ingredients = add_recipe(filename)
            cook_book[recipe_name] = ingredients
            save_to_file(cook_book, filename)
            print("Рецепт успешно добавлен!")
        elif choice == '3':
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите снова.")


if __name__ == '__main__':
    main()
