def max_profit(prices):
    if not prices:
        return 0

    min_price = float('inf')  # Initialize to a very high value
    max_profit = 0  # Initialize max profit

    for price in prices:
        # Update the minimum price if the current price is lower
        if price < min_price:
            min_price = price
        
        # Calculate the profit if selling at the current price
        profit = price - min_price
        
        # Update max profit if the calculated profit is higher
        if profit > max_profit:
            max_profit = profit

    return max_profit


# Driver code with test cases
test_cases = [
    [1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9],
    [7, 1, 5, 3, 6, 4],
    [7, 6, 4, 3, 1],
    [2, 6, 8, 7, 8, 7, 9, 4, 1, 2, 4, 5, 8],
    [1, 4, 2]
]

for i, prices in enumerate(test_cases):
    print(f"Test Case {i + 1}: Prices = {prices}, Max Profit = {max_profit(prices)}")