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


def build_status_report(items):
    total_items = len(items)
    completed_items = 0
    pending_items = 0
    for item in items:
        if item.get("done"):
            completed_items += 1
        else:
            pending_items += 1

    if total_items == 0:
        completion_rate = 0.0
    else:
        completion_rate = completed_items / total_items
    return {
        "total": total_items,
        "completed": completed_items,
        "pending": pending_items,
        "completion_rate": completion_rate,
    }
