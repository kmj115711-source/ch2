# 문자열 만들기
print("Hello")

# 문자열 자르기
# 문자열 안에서 문자 하나를 추출
# 문자열 [index]
# index란? 문자의 위치
# 무조건 0부터 시작이며 연속적
print('hello'[0])
print('hello'[1])
print('hello'[2])
print('hello'[3])
print('hello'[4])

# 문자 슬라이스
# [index]=> 문자 하나만 추출
# 슬라이스[index시작:index끝] => 범위로 추출
# 슬라이스에서 끝 번호는 포함x
print('hello'[0:2])
print('hello'[2:5]) #끝번호 포함x 2~4까지만 추출 됨
print('hello'[2:]) #끝번호x, 자동으로 마지막 문자까지 추출 됨
print('hello'[ :2]) #시작번호x, 자동으로 시작부터 
print('hello'[:]) #전체


#문자열의 길이를 구하는 함수 : len()
print(len('aaa'))
print(len("hello, world!")) #공백도 문자로 취급
print(len("안녕하세요"))