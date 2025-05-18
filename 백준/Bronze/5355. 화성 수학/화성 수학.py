t = int(input())
for _ in range(t):
    tokens = input().split()
    result = float(tokens[0])

    for symbol in tokens[1:]:
        if symbol == '@':
            result *= 3
        elif symbol == '%':
            result += 5
        elif symbol == '#':
            result -= 7
    print(f"{result:.2f}")