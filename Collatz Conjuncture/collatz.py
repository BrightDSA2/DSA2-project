def collatz(n: int):
    print(n)
    if n == 1:
        return
    if n % 2 == 0:
        collatz(n // 2)
    else:
        collatz(3 * n + 1)

# Example usage: collatz(6)
