import random

lotto_num = range(1,46) # 1~46까지의 랜덤한 숫자를 lotto_num변수에 넣음.

for i in range(5): # 5번 반복
    print(random.sample(lotto_num,6)) # 결과 출력(6개의 숫자)