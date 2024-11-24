from random import choice
translation = {
    'soup':  'Zupa',
    'dinner':  'Drugie danie',
    'dessert':  'Deser'
}
dishes = {
    'soup':  ['pomidorowa', 'barszcz', 'rosol'],
    'dinner':  ['pulpety', 'shabowy', 'golabki'],
    'dessert':  ['lody', 'kisiel', 'ciasto']
}


for category, dishes_at_categor in dishes.items():
    dish_at_category = choice(dishes_at_categor)
    print(translation.get(category, category), dish_at_category)