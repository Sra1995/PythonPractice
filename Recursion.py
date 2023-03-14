def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    if n < 1:
        return n


    return n + sum_positive_numbers(n - 1)
    # What got me was n - 1. I was using + until I went to the below website to see visualize it

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15