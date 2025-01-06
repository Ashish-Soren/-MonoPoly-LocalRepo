def get_input(n, prompt):
    return [int(input(prompt)) for _ in range(n)]

n = int(input("How many entries are needed? "))

# Get the lower limits and frequencies
ll = get_input(n, "Enter the lower limits: ")
freq = get_input(n, "Enter the frequencies: ")

# Calculate class interval and cumulative frequencies
ci = ll[1] - ll[0]
cf = [sum(freq[:i+1]) for i in range(n)]

# Find the median class
median_class_index = next(i for i in range(n) if cf[i] >= cf[-1] / 2)

# Calculate the median
median = ll[median_class_index] + ((cf[-1] / 2 - cf[median_class_index - 1]) * ci) / freq[median_class_index]

# Display the results
print("\nThe Data Given: ")
print("Class \t Frequencies \t Cumulative Freq")
for i in range(n):
    print(f"{ll[i]} - {ll[i] + ci} \t {freq[i]} \t {cf[i]}")

print(f"\nThe Median Class is: {ll[median_class_index]} - {ll[median_class_index] + ci}")
print(f"The Median is: {median}")