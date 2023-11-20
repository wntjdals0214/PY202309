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
