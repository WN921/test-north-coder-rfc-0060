"""Simple sample functions for demonstration."""


def summarize_numbers(numbers):
    if not numbers:
        return {"count": 0, "sum": 0, "average": 0, "min": None, "max": None}

    total = 0
    smallest = numbers[0]
    largest = numbers[0]
    for value in numbers:
        total += value
        if value < smallest:
            smallest = value
        if value > largest:
            largest = value

    average = total / len(numbers)
    return {
        "count": len(numbers),
        "sum": total,
        "average": average,
        "min": smallest,
        "max": largest,
    }


def normalize_text(text):
    cleaned = text.strip()
    cleaned = cleaned.replace("_", " ")
    parts = cleaned.split()
    normalized_parts = []

    for part in parts:
        word = part.lower()
        if word in {"api", "http", "json"}:
            normalized_parts.append(word.upper())
        else:
            normalized_parts.append(word.capitalize())

    normalized = " ".join(normalized_parts)
    if normalized and normalized[-1] not in ".!?":
        normalized += "."
    return normalized


def build_report(records):
    lines = ["Report Summary", "=" * 14]
    success_count = 0
    failure_count = 0

    for item in records:
        name = item.get("name", "unknown")
        success = item.get("success", False)
        duration = item.get("duration", 0)
        status = "OK" if success else "FAILED"
        lines.append(f"- {name}: {status} ({duration} ms)")
        if success:
            success_count += 1
        else:
            failure_count += 1

    lines.append(f"Success: {success_count}")
    lines.append(f"Failure: {failure_count}")
    return "\n".join(lines)
