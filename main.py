import random                           # 랜덤모듈 가져오기

lotto_num = range(1, 46)                # lotto_num변수에 범위를 1~45까지 지정

for i in range(5):                      # for문과 range를 통해 5번실행하게하는 리스트 생성
    print(random.sample(lotto_num, 6))  # random모듈의 sample클래스를 사용하여 lotto_num변수에 6개 무작위수 대입

