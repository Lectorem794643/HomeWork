recipe = set()
sum_recipe = int(input())
for _ in range(sum_recipe):
    sum_ingredient = int(input())
    for __ in range(sum_ingredient):
        ingredient = str(input())
        recipe.add(ingredient)
print(recipe)
# странный вывод ответа но не знаю как исправить
