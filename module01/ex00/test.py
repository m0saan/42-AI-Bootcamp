from book import Book
from recipe import Recipe

recipe1 = Recipe.init_obj()
recipe2 = Recipe("Tacos", 2, 10, ["3ish, sos", "chicken meat"], "lunch", "Blah blah Hopiti hobla")
recipe3 = Recipe("Tacoss", 2, 10, ["3ish, sos", "chicken meat"], "lunch", "Blah blah Hopiti hobla")
recipe4 = Recipe("Pattess", 4, 10, ["les pattes"], "dessert", "dir les pattes a jemmi")
recipe5 = Recipe("Pattesss", 4, 10, ["les pattes"], "dessert", "dir les pattes a jemmi")
recipe6 = Recipe("Pattesssss", 4, 10, ["les pattes"], "dessert", "dir les pattes a jemmi")
book = Book("nutrition_book")
book.add_recipe(recipe1)
book.add_recipe(recipe2)
book.add_recipe(recipe3)
book.add_recipe(recipe4)
book.add_recipe(recipe5)
book.add_recipe(recipe6)

print(book.get_recipe_by_name("Pattesssss"))
print(book.get_recipes_by_types("lunch"))
