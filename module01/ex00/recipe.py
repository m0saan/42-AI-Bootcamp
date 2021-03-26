class Recipe:
    """This is a recipe class"""

    @classmethod
    def zero(cls):
        return cls("Tajine", 2, 15, ["potatos, tomatos", "oil", "meat"], "lunch", "Blah blah")

    def __init__(self, p_name, p_cooking_lvl, p_cooking_time, p_ingredients, p_recipe_type, p_description=""):
        self.name = p_name
        self.cooking_lvl = p_cooking_lvl
        self.cooking_time = p_cooking_time
        self.ingredients = p_ingredients
        self.recipe_type = p_recipe_type
        self.description = p_description

    def __str__(self):
        """Return the string to print with the recipe info"""

        txt = f"{self.name} is a {self.recipe_type} meal. the recipe have a cooking level of {self.cooking_lvl}," \
              f" it can be made in {self.cooking_time} minutes and it is composed of {self.ingredients}"
        return txt

