lines = open("student.csv","r", encoding="utf8").readlines()
del(lines[0]) # 필요없는 줄 삭제

class Student(): # 클래스 선언
    이름 = ""
    국어 = 0
    수학 = 0
    영어 = 0

    def __init__(self, 이름, 국어, 수학, 영어):
        self.이름 = 이름
        self.국어 = 국어
        self.수학 = 수학
        self.영어 = 영어
    
    # TODO 2: 학생 별 평균 점수를 계산, 출력
    def get_average(self, i):    
        average_score = (float(self.국어) + float(self.수학) + float(self.영어))/3 # 평균점수 계산
        return float (average_score)

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
fp = open("average2.txt", "w", encoding = "utf8")
for line in print_line:
    fp.write(line+"\n") # 리스트에 저장한 출력 내용을 한줄씩 파일에 작성
fp.close()