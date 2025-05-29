def minimal_string(s):
    min_string = None
    for i in range(len(s)):
        # Move character at index i to the beginning
        new_s = s[i] + s[:i] + s[i+1:]
        # Update the minimum string if needed
        if min_string is None or new_s < min_string:
            min_string = new_s
    return min_string

# Example usage:
s = input().strip()
print(minimal_string(s))
