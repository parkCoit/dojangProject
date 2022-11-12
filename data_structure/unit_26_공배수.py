# problem
def num(a):
    return {i for i in a if i % 3 == 0 and i % 5== 0}

#problem2
def num2(c, d):
    a = {i  for i in range(1, d+1) if c % i == 0}
    b = {i for i in range(1, d + 1) if d % i == 0}

    #a = {i for i in range(1, d + 1) if c % i == 0 and d % i == 0}  이것도 같은 코드
    #divisor = a


    divisor = a & b

    result = 0
    if type(divisor) == set:
        result = sum(divisor)
    return result


if __name__ == '__main__':
    print(num(range(1,101)))
    print(num2(int(input("첫 번째 수")), int(input("두 번째 수"))))