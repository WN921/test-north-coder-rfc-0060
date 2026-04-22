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