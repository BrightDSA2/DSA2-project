from collections import Counter

def findMostFrequentWord(inputList1: list[str], inputList2: list[str]) -> str:
    excluded = set(inputList2)
    counts = Counter(w for w in inputList1 if w not in excluded)
    if not counts:
        return ""
    return max(counts, key=counts.get)
