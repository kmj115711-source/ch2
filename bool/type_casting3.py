# 형변환의 종류
# 자동 형변환(묵시적 형변환)
# 컴퓨터가 계산 중에 자동으로 자료형을 바꾸는 것

print(type(4.5), type(2)) #float int
# 컴퓨터가 계산을 위해 2를 2.0으로 변환한 것
print(4.5 / 2 ) #float/int => float/float

# 타입을 확인하는 함수들
# type
print(type(4.5)) #float
#isinstance : 해당 타입이 맞는지 확인
print(isinstance(4.5, float)) #true
print(isinstance(4.5, (int, float)))