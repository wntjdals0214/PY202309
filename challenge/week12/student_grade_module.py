from student import Student

lines = open("student.csv","r", encoding="utf8").readlines()
del(lines[0]) # 필요없는 줄 삭제

# TODO 1: 
def loadData(lines):
    temp = [] # 만든 인스턴스를 담을 빈 리스트
    for line in lines:
        tokens=line.strip().replace(","," ").split(" ") # 파일의 각 라인을 리스트화
        i = Student(tokens[0], tokens[1], tokens[2], tokens[3],) # 인스턴스 생성
        temp.append(i)
    return temp
    
print("-----학생들의 평균 점수-----")

line_list = loadData(lines)
print_line = []
for i in line_list:
    line = ("%s의 평균 점수는 %f입니다." %(i.이름, i.get_average(i)))
    print(line)
    print_line.append(line) # 필요한 내용 출력과 동시에 리스트에 저장


# TODO 3: 평균 점수를 코드 실행결과와 동일하게 파일로 출력
fp = open("average3.txt", "w", encoding = "utf8")
for line in print_line:
    fp.write(line+"\n") # 리스트에 저장한 출력 내용을 한줄씩 파일에 작성
fp.close()