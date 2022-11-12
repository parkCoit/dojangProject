# problem
def num():
    a = int(input("도로와의 거리(m)")) # 거리 12m - 7
    return int(0.2467 * a + 4.159)

# problem2
def num2():
    a = int(input("ap 값 : ")) # ap : 102 -  286.2
    return float(a*0.6+225)

if __name__ == '__main__':
    print(num())
    print(num2())

