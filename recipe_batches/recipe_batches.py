#!/usr/bin/python

import math

# creates the recipe method which takes in two parameters
# in this case, an array of the recipe and the array of ingredients


def recipe_batches(recipe, ingredients):
    # creates and sets the batch_count to None
    batch_count = None
    # loops through the key value pairs in the recipe items
    for recipe_ingred, recipe_count in recipe.items():
        # checks is the ingredient is matched in the other array
        if recipe_ingred in ingredients:
            # creates and sets the ingredient_count variable to the amount of each item in the ingredients array.
            ingredient_count = ingredients[recipe_ingred]
            # Sets the maximum amount of batches for each ingredient by diving the amount we have by the requirement.
            maximum = int(ingredient_count / recipe_count)
            # if we do have enough for one batch, it will set the function to return how many.
            if batch_count == None or maximum < batch_count:
                batch_count = maximum
        else:
            # if we don't, it returns 0.
            return 0

    return batch_count or 0


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
