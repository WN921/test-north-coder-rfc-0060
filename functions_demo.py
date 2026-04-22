def calculate_average(numbers):
    if not numbers:
        return 0

    total = 0
    count = 0
    for value in numbers:
        total += value
        count += 1

    average = total / count
    return round(average, 2)


def format_user_info(name, age, city):
    cleaned_name = name.strip().title()
    cleaned_city = city.strip().title()

    if age < 0:
        return "Invalid age provided"

    message = (
        f"User {cleaned_name} is {age} years old "
        f"and lives in {cleaned_city}."
    )
    return message
