#기본 계산기

#더하기
def add(a, b):
    return a+b

#빼기
def sub(a, b):
    return a-b

#곱하기
def mul(a, b):
    return a*b

#나누기
def div_new(a,b):
    return a/b

#평균
def get_average(a, b):
    return (a+b)/2

#나머지
def get_reminder(a, b):
    return a//b

#절댓값
def get_Abs(num):
    if num >=0 :
        return num
    else :
        return -num
    
#백분율
def get_percent(a, b):
    return (a/b) * 100

#합공식
def get_sum_ver1(n):
    return n(n+1)/2

#팩토리얼
def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num