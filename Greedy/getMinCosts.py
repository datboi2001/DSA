# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    """
    A group of friends want to buy a bouquet of flowers.
     The florist wants to maximize his number of new customers and the money he makes.
     To do this, he decides he'll multiply the price of each flower by the number of that
     customer's previously purchased flowers plus 1
    :param k: number of friends
    :param c: array of prices for flowers
    :return: minimum cost to purchase all flowers
    """
    # Main idea: sort the array in descending order and then
    # multiply each element by the number of friends who have
    # not yet purchased a flower.

    # Sort the array in descending order
    c.sort(reverse=True)

    # Initialize the total cost
    total = 0

    # Initialize the number of flowers purchased by each friend
    flowers_purchased = [0] * k

    # Iterate through the array
    for i in range(len(c)):
        # Calculate the total cost
        total += (flowers_purchased[i % k] + 1) * c[i]

        # Increment the number of flowers purchased by the friend
        flowers_purchased[i % k] += 1

    return total