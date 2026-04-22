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
