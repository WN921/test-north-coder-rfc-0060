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


def format_user_profile(name, age, city):
    clean_name = name.strip().title()
    clean_city = city.strip().title()

    profile_lines = []
    profile_lines.append(f"Name: {clean_name}")
    profile_lines.append(f"Age: {age}")
    profile_lines.append(f"City: {clean_city}")

    if age >= 18:
        profile_lines.append("Status: Adult")
    else:
        profile_lines.append("Status: Minor")
    return " | ".join(profile_lines)
