#The Ingredient Checker
def check_ingredients(pantry_list, recipe_list):
    lower_pantry = [item.lower() for item in pantry_list]
    lower_recipe = [item.lower() for item in recipe_list]

    pantry_set = set(lower_pantry)
    recipe_set = set(lower_recipe)
    missing_items = sorted(recipe_set - pantry_set)
    available_items = sorted(pantry_set & recipe_set)
    
    missing = list(missing_items)
    available = list(available_items)
    
    return missing, available
pantry = ["Eggs", "flour", "Milk", "eggs", "salt"]
recipe = ["flour", "milk", "Sugar", "Eggs", "butter"]

missing, available = check_ingredients(pantry, recipe)

print(f"Need to buy: {missing}")
print(f"Already have: {available}")