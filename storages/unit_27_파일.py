def file(txt):

    # words.txt 파일 리스트로 생성
    ls = ["anonymously\n", "compatibility\n", "dashboard\n", "experience\n", "photography\n", "spotlight\n", "warehouse\n"]
    with open(txt, 'w') as file :
        file.writelines(ls)  # writelines 는 문자열 리스트 write 는 문자열



    # words.txt 파일 읽고 로직 만들기
    with open(txt, 'r') as file :
        count = 0
        words = file.readlines()  # 한 줄씩 리스트 형태로 가져옴
        print(words) # 확인용
        for word in words :
            if len(word.strip("\n")) <= 10:  # strip 은 해당 문자열 삭제
                count += 1
        return count


def file2(txt):
    pass


if __name__ == '__main__':
    print(file('./data/words.txt'))
    file2('./data/word.txt')