numbers = [float(x) for x in input().split()]

# Find the maximum value
max_value = max(numbers)

# Calculate the sum of all numbers
total_sum = sum(numbers)

# Calculate the average
average = total_sum / len(numbers)

# Print the max and average with two digits after the decimal point
print(f'{max_value:.2f} {average:.2f}')