import time
import os


def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

            # Visualize the DP table
            os.system("cls" if os.name == "nt" else "clear")  # Clear the console
            print("DP Table at step i =", i, "w =", w)
            print_table(dp)
            time.sleep(0.5)  # Adjust the delay as needed

    return dp[n][capacity]


def print_table(table):
    for row in table:
        for col in row:
            print(f"{col:3}", end=" ")
        print()


# Example usage
values = [1, 6, 10, 16]
weights = [1, 2, 3, 5]
capacity = 7
max_value = knapsack(values, weights, capacity)
print("Maximum value:", max_value)

