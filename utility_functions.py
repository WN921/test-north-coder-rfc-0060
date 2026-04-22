"""Utility functions for small text and list processing tasks."""


def normalize_words(text: str) -> list[str]:
    cleaned = text.strip().lower()
    if not cleaned:
        return []

    result = []
    current = []
    for char in cleaned:
        if char.isalnum():
            current.append(char)
        elif current:
            result.append("".join(current))
            current = []

    if current:
        result.append("".join(current))
    return result


def group_by_length(words: list[str]) -> dict[int, list[str]]:
    grouped = {}
    for word in words:
        size = len(word)
        if size not in grouped:
            grouped[size] = []
        if word not in grouped[size]:
            grouped[size].append(word)

    for size, items in grouped.items():
        items.sort()
        grouped[size] = items

    return grouped


def format_report(title: str, values: list[int]) -> str:
    if not values:
        return f"{title}: no data"

    total = sum(values)
    average = total / len(values)
    minimum = min(values)
    maximum = max(values)
    lines = [f"Report: {title}"]
    lines.append(f"Count: {len(values)}")
    lines.append(f"Total: {total}")
    lines.append(f"Average: {average:.2f}")
    lines.append(f"Range: {minimum} - {maximum}")
    return "\n".join(lines)
