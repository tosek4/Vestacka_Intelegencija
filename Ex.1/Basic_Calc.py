def calc(x, operatro, y):
    if operatro == "+":
        return x + y
    if operatro == "-":
        return x - y


if __name__ == '__main__':
    x = float(input())
    operator = input()
    y = float(input())
    print(calc(x, operator, y))
