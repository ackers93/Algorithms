#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    batch_count = None
    for recipe_ingred, recipe_count in recipe.items():
        if recipe_ingred in ingredients:
            ingredient_count = ingredients[recipe_ingred]
            maximum = int(ingredient_count / recipe_count)
            if batch_count == None or maximum < batch_count:
                batch_count = maximum
        else:
            return 0

    return batch_count or 0


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
