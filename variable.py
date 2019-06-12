# 변수 이름은 문자, 숫자,  _ 로 구성된다.

from keyword import kwlist

friends = 1
a = 10
my_name = '김성모'
myName = '김성모'
_yourname = '둘리'

# friends$ = 1 에러 코드
# a! = 10 에러 코드
# 1abc = 10  에러 코드

print(kwlist)

# 한글 이름의 변수도 사용이 가능하다.

def 내이름출력(name) :
    return print(name)
내이름출력('김성모')

