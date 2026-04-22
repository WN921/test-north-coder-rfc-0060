def calculate_average(numbers):
    if not numbers:
        return 0

    total = 0
    count = 0
    for value in numbers:
        total += value
        count += 1

    average = total / count
    rounded_average = round(average, 2)
    return rounded_average
