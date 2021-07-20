old_recipe, recipe_without_onions = [], []
newPoint = [old_recipe.append(str(input())) for i in range(int(input()))]
MAGICIAN = [recipe_without_onions.append(old_recipe[i]) for i in range(len(newPoint)) if 'лук' not in old_recipe[i]]
MAGICIAN_2 = [print(recipe_without_onions[i], end=', ') for i in range(len(recipe_without_onions))]
