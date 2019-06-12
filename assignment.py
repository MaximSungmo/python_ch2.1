# 치환문의 예시
a = 1
b = a+1

print(a, b, sep=', ')

# 세미콜론으로 py version 2.x 기능 사용, 치환문을 구분할 수 있다.
e = 3.5; f = 5.3
print(e, f)

# 여러 개를 한 번에 치환하기
e, f = 3.5, 5.3
print(e, f)

# 같은 값을 여러 변수에 대입
x = y = z = 10
print(x, y, z)

# C 스타일 지원하지 않음
# x = (y = 10)


# 동적 타이핑 : 변수에 새로운 값이 할당되면 값을 버리고 새로운 값으로 치환된다.
a = 1
print(a, type(a))
b = a
a = '2'
print(b, type(b))
print(a, type(a))

# 확장 치환문
a = 10
a += 10
print(a)



