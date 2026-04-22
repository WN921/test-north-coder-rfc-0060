"""Custom helper functions for small data processing tasks."""


def calculate_score(records: list[dict]) -> dict:
    if not records:
        return {"count": 0, "total": 0, "average": 0}

    total = 0
    valid_count = 0
    for item in records:
        score = item.get("score", 0)
        if isinstance(score, (int, float)):
            total += score
            valid_count += 1

    average = total / valid_count if valid_count else 0
    return {"count": valid_count, "total": total, "average": average}


def group_by_first_letter(words: list[str]) -> dict[str, list[str]]:
    grouped: dict[str, list[str]] = {}
    for word in words:
        cleaned = word.strip()
        if not cleaned:
            continue

        first = cleaned[0].lower()
        if first not in grouped:
            grouped[first] = []
        grouped[first].append(cleaned)

    for key in grouped:
        grouped[key].sort()
    return grouped


def format_user_report(users: list[dict]) -> list[str]:
    lines = []
    for index, user in enumerate(users, start=1):
        name = user.get("name", "Unknown")
        age = user.get("age", "N/A")
        city = user.get("city", "Unknown")

        if isinstance(name, str):
            name = name.strip() or "Unknown"
        summary = f"{index}. {name} | age={age} | city={city}"
        lines.append(summary)

    if not lines:
        return ["No users available."]
    return lines
