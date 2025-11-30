# Problem 1 - Max sales

def main():
    Week_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    Sale_list = []

    # Get user input for each day's sales
    for day in Week_list:
        sale = float(input(f"Enter sales for {day}: "))
        Sale_list.append(sale)

    # Start with the first day
    max_sale = Sale_list[0]
    max_day = Week_list[0]

    # Loop through the list to find the maximum
    for i in range(1, len(Sale_list)):
        if Sale_list[i] > max_sale:
            max_sale = Sale_list[i]
            max_day = Week_list[i]

    # Output using f-strings
    print(f"The Max sales is $ {max_sale}")
    print(f"The Max sales day is {max_day}")

main()



# Problem 2 - Determine the range of a list of numbers

def main():
    # Create an empty list
    numbers = []

    # Prompt user for values
    value = float(input("Enter value (or 0 to end): "))

    while value != 0:
        numbers.append(value)
        value = float(input("Enter value (or 0 to end): "))

    # Display the list
    print(numbers)

    # Find highest and lowest values
    highest = numbers[0]
    lowest = numbers[0]

    for n in numbers:
        if n > highest:
            highest = n
        elif n < lowest:
            lowest = n

    # Calculate range
    range_value = highest - lowest

    # Output the result
    print(f"Range = {range_value}")

main()
