def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    for _ in range(n):
        yield "🐑" * _


if __name__ == "__ main__":
    main()