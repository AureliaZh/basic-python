def encodeString(s):
    """
    Encode a string using run-length encoding.
    Example: "AAAAABBBBAAA" -> [('A', 5), ('B', 4), ('A', 3)]
    """
    result = []

    if not s:
        return result

    current_char = s[0]
    count = 1

    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = char
            count = 1

    # Add the last group
    result.append((current_char, count))
    return result


def decodeString(encoded):
    """
    Decode a run-length encoded list back into a string.
    Example: [('A', 5), ('B', 4), ('A', 3)] -> "AAAAABBBBAAA"
    """
    result = ""

    for char, count in encoded:
        result += char * count

    return result


# Example 1: encode
original = "AAAAABBBBAAA"
encoded = encodeString(original)
print("Encoded:", encoded)

# Example 2: encode
print("Encoded:", encodeString("Bookkeeping"))

# Example 3: decode
decoded = decodeString([('W', 5), ('1', 2), ('G', 3)])
print("Decoded:", decoded)

# Full round-trip test
print("Round trip:", decodeString(encodeString(original)))