def hanoi(n, star, mid, des):
    if n == 1:
        print(star, "->", des)
    else:
        hanoi(n - 1, star, des, mid)
        print(star, "->", des)
        hanoi(n - 1, mid, star, des)


hanoi(3, "A", "B", "C")