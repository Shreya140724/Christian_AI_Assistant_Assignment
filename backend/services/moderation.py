def is_safe(text: str) -> bool:

    blocked_words = [
        "kill",
        "murder",
        "terrorist",
        "genocide",
        "suicide",
        "hate",
        "violence"
    ]

    text = text.lower()

    for word in blocked_words:

        if word in text:
            return False

    return True