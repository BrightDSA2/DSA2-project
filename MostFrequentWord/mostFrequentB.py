from collections import Counter

def findMostFrequentFollower(inputList: list[str], targetWord: str) -> str:
    followers = [inputList[i+1] for i in range(len(inputList)-1) if inputList[i] == targetWord]
    if not followers:
        return ""
    counts = Counter(followers)
    max_freq = max(counts.values())
    candidates = [w for w, freq in counts.items() if freq == max_freq]
    # Find the last occurrence among candidates
    for i in reversed(range(len(inputList)-1)):
        if inputList[i] == targetWord and inputList[i+1] in candidates:
            return inputList[i+1]
    return ""
