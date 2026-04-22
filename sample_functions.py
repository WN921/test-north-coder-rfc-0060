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


def format_user_profile(name, age, city, hobbies):
    cleaned_name = name.strip().title()
    cleaned_city = city.strip().title()
    normalized_hobbies = [hobby.strip().lower() for hobby in hobbies if hobby.strip()]

    profile_lines = [
        f"Name: {cleaned_name}",
        f"Age: {age}",
        f"City: {cleaned_city}",
        f"Hobbies: {', '.join(normalized_hobbies) if normalized_hobbies else 'None'}",
    ]
    summary = " | ".join(profile_lines)
    return {"name": cleaned_name, "city": cleaned_city, "hobbies": normalized_hobbies, "summary": summary}


def build_report(items):
    report = []
    completed = 0
    pending = 0

    for index, item in enumerate(items, start=1):
        title = item.get("title", "Untitled")
        done = item.get("done", False)
        status = "done" if done else "pending"
        report.append(f"{index}. {title} [{status}]")
        if done:
            completed += 1
        else:
            pending += 1

    footer = f"Completed: {completed}, Pending: {pending}, Total: {len(items)}"
    return "\n".join(report + [footer])
