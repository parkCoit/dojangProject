x = 5

# problem
def practice(a):
    if a != 10 :
        answer = "ok"
    else : answer = "no"
    return answer

# problem2
def practice2(a):
    b ,c = a
    if c[:4] == "Cash":
        answer = int(b) - int(c[4:])
    else: answer = "잘못 된 값"
    return answer


if __name__ == '__main__':
    print(practice(x)) # 5
    print(practice2(input().split()))   # 27000 Cash3000 -> 24000 , 72000 Cash5000 -> 67000
