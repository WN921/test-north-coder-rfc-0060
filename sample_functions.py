def normalize_name(name):
    cleaned = str(name).strip()
    if not cleaned:
        return ""

    parts = cleaned.replace("_", " ").split()
    normalized_parts = []
    for part in parts:
        if len(part) == 1:
            normalized_parts.append(part.upper())
        else:
            normalized_parts.append(part[0].upper() + part[1:].lower())

    return " ".join(normalized_parts)


def collect_even_numbers(values):
    even_numbers = []
    for value in values:
        if isinstance(value, bool):
            continue
        if not isinstance(value, int):
            continue
        if value % 2 != 0:
            continue

        even_numbers.append(value)

    even_numbers.sort()
    return even_numbers
