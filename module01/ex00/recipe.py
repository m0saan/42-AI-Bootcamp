class Recipe:
    """This is a recipe class"""

    @classmethod
    def init_obj(cls):
        return cls("Tajine", 2, 15, ["potatos, tomatos", "oil", "meat"], "lunch", "Blah blah")

    @staticmethod
    def has_bad_item(ls):
        for item in ls:
            if not isinstance(str, item):
                return True
        return False

    @staticmethod
    def has_bad_recipe_type(p_recipe_type):
        recipes_tpe = ["starter", "lunch", "dessert"]
        if not isinstance(str, p_recipe_type) or p_recipe_type not in recipes_tpe:
            return True
        return False

    def __init__(self, p_name, p_cooking_lvl, p_cooking_time, p_ingredients, p_recipe_type, p_description=""):
        self.test_passed_args(p_cooking_lvl, p_ingredients, p_recipe_type)
        self.name = p_name
        self.cooking_lvl = p_cooking_lvl
        self.cooking_time = p_cooking_time
        self.ingredients = p_ingredients
        self.recipe_type = p_recipe_type
        self.description = p_description

    def test_passed_args(self, p_cooking_lvl, p_ingredients, p_recipe_type, p_cooking_time):
        if p_cooking_lvl not in range(1, 6) or not isinstance(p_cooking_lvl, int):
            raise ValueError("p_cooking_lvl must be in range 0-5.")
        elif p_cooking_time < 0 or not isinstance(p_cooking_time, int):
            raise ValueError("p_cooking_time got an unexpected value.")
        elif not isinstance(list, p_ingredients) or self.has_bad_item(p_ingredients):
            raise ValueError("ingredients must be of type str")
        elif self.has_bad_recipe_type(p_recipe_type):
            raise ValueError("recipe type must be one of the types: “starter”, “lunch” or “dessert”.")

    def __str__(self):
        """Return the string to print with the recipe info"""

        txt = f"{self.name} is a {self.recipe_type} meal. the recipe have a cooking level of {self.cooking_lvl}," \
              f" it can be made in {self.cooking_time} minutes and it is composed of {self.ingredients}"
        return txt

