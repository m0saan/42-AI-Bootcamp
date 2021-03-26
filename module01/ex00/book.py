from datetime import datetime


class Book:
    """This is a book class"""

    recipe_keys = ["starter", "lunch", "dessert"]

    def __init__(self, p_name: str):
        self.name = p_name
        self.last_update = datetime.now()
        self.creation_date = datetime.now()
        self.recipes_list = {
            "starter": [],
            "lunch": [],
            "dessert": [],
        }

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        for _, list_of_recipes in self.recipes_list.items():
            for recipe in list_of_recipes:
                if recipe.name is name:
                    return recipe

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        recipes = self.recipes_list[recipe_type]
        for recipe in recipes:
            print(recipe)

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.now()
