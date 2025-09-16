from collections import Counter
def frequencySort(s: str) -> str:
    d = Counter(s)
    s_d = sorted(d.items(), key=lambda x: -x[1])
    result = ""
    for key, value in s_d:
        result += key * value
    return result
s = "tree"
print("Sorted by frequency:", frequencySort(s))
