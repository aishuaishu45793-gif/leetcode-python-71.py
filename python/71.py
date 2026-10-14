# Program 143: Find the Second-Largest Number

numbers = [10, 25, 8, 40, 30]

unique_numbers = list(set(numbers))
unique_numbers.sort()

if len(unique_numbers) >= 2:
    print("Second-largest number:", unique_numbers[-2])
else:
    print("Second-largest number does not exist")