l = []
n = int(input("No of observations? "))

for i in range(n):
    y = int(input("Enter a value: "))
    l.append(y)

# Sort the list
l.sort()

# Print the sorted list
print(l)

# Print the median
print(n//2)
if n%2 == 0:   
    print((l[n//2]+l[n//2-1])/2)
else:
    print(l[n//2])

# Print the mean
print(sum(l)/n)

# Print the mode
freq = {}
for i in l:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

mode = max(freq, key=freq.get)
print(mode)

# Find the range
print(l[-1]-l[0])  


# Find the variance
mean = sum(l)/n
variance = sum((x - mean)**2 for x in l) / n
print(variance)

# Find mean median and mode of a continuous distribution

