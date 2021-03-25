cookbook = {
    "sandwich": {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": 10
    },

    "cake": {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60
    },

    "salad": {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": 15
    }
}

recipe_values = ["ingredients", "meal", "prep_time"]


def start():
    choices = ["Add a recipe", "Delete a recipe", "Print a recipe", "Print the cookbook", "Quit"]
    while True:
        for i, choice in enumerate(choices):
            print("{}: {}".format(i + 1, choice))
        choice = int(input(">>"))

        if choice == 1:
            user_add_recipe()

        if choice == 2:
            recipe_name = input("Enter the name of the recioe you want to delete: ")
            delete_recipe(recipe_name)

        if choice == 3:
            recipe_name = input("Enter the name of the recioe you want to delete: ")
            print_recipe(recipe_name)

        if choice == 4:
            print_all_recipe_names()

        if choice == 5:
            print("Cookbook closed.")
            break

        else:
            print("Please enter a valid choice")


def user_add_recipe():
    user_inputs = list()
    recipe_name = input("Enter the recipe name: ")
    for v in recipe_values:
        user_input = input("Enter the {}: ".format(v))
        if v == recipe_values[0]:
            user_input = user_input.split(" ")
        user_inputs.append(user_input)
    add_recipe(recipe_name, user_inputs[0], user_inputs[1], user_inputs[2])
    user_inputs.clear()


def print_recipe(name: str):
    recipe = cookbook[name]
    print(f"{name} recipe is:")
    i = 0
    for item in recipe:
        print("\t{}: {}".format(recipe_values[i], cookbook[name][item]))
        i += 1
    print()


def delete_recipe(name: str):
    if cookbook.get(name):
        cookbook.pop(name)
    else:
        print("No such recipe name")


def add_recipe(recipe_name: str, ingredients: list, meal_type: str, prep_time: str):
    cookbook.setdefault(recipe_name, {"ingredients": ingredients, "meal": meal_type, "prep_time": prep_time})


def print_all_recipe_names():
    for key in cookbook.keys():
        print(f"{key} recipe is: ")
        i = 0
        for recipe in cookbook[key]:
            print("\t {}: {}".format(recipe_values[i], cookbook[key][recipe]))
            i += 1


if __name__ == '__main__':
    start()
