# problem
def num(d):
    #a,b,c = map(int, input("숫자 3개 입력 : ").split()) # -10 20 30 타이타닉 map.({"S": 1, "C" : 2, "Q" : 3}) deference
    a, b, c = d
    return type(a) and a+b+c


# problem2
def num2(d):
    #a, b = map(int, input("숫자 2개 입력 :").split()) # 50 , 100
    a,b = d
    c = None
    return a, b , c

# problem3
def num3(e):
    #a,b,c,d = map(int, input().split()) # 83 92 87 90 -> 88  , 32 53 22 95 -> 50
    a,b,c,d = e
    return int((a+b+c+d)/4)

if __name__ == '__main__':
    print(num(map(int, input("숫자 3개 입력 : ").split())))
    print(num2(map(int, input("숫자 2개 입력 :").split())))
    print(num3(map(int, input().split())))
