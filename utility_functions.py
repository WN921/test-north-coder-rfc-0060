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