#!/usr/bin/python

import argparse


def find_max_profit(prices):
    # creates a lowest price variable so far, initializing it at the first item in the 'prices' array
    lowest = prices[0]
    # creates a highest price variable so far, initializing it at the first item in the 'prices' array
    highest = prices[0]
    # Creates a maximum variable that will store the maximum differences between the items
    maximum = None
    # this starts our for loop at the second item in the array, and continuing until the end.
    for price in prices[1:]:
        # Creates a variable once the lowest item is subtracted from the highest
        diff = price - lowest
        # This sets the maximum number by comparing it to the looped over numbers.
        # if diff is larger than maximum it becomes the new maximum number.
        if maximum == None or diff > maximum:
            maximum = diff
        # if the price is higher than  the highest number set to 'highest', it will replace it.
        if price > highest:
            highest = price
        # if the price is lower than  the lowest number set to 'lowest', it will replace it.
        if price < lowest:
            lowest = price
    # once this is looped through, it will have decided which is the highest and which is the lowest
    # and it will return the difference of the price - the lowest.
    return maximum


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
