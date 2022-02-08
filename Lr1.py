

from math import cos, sin
from re import L
from functools import reduce

def print_rez(rez):
    print(f"""
    Rezult:
    {rez}
    """)

def task_1(x: float, y: float):
    print_rez(round(cos(x)**2+sin(y)**2, 2))

def task_2(n: int):
    S = sum([x**2 for x in range(1,n+1)])
    print_rez(S)

def task_3(n):
    items = [int(input("=> ")) for x in range(n)]


    print_rez(items)
    print(f"Max item: {max(items)}")
    print(f"Multiplication of items elements: {reduce(lambda x, y: x*y, items)}")
    for x in items:
        if x<0:
            items.remove(x)
    items.reverse()
    print(f"Positive elements in the reverse line: {items}")



if __name__ == "__main__":

    print("Task 1:")
    x = float(input("\nInput float x   =>  "))
    y = float(input("Input float y   =>  "))
    task_1(x, y)

    print("Task 2:")
    n = int(input("\nInput int N   =>  "))
    task_2(n)

    n2 = int(input("Input array length   =>   "))
    task_3(n2)
