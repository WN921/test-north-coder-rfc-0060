def analyze_numbers(numbers):
    if not numbers:
        return {"count": 0, "sum": 0, "average": 0, "max": None, "min": None}

    total = 0
    maximum = numbers[0]
    minimum = numbers[0]
    for value in numbers:
        total += value
        if value > maximum:
            maximum = value
        if value < minimum:
            minimum = value

    average = total / len(numbers)
    return {"count": len(numbers), "sum": total, "average": average, "max": maximum, "min": minimum}