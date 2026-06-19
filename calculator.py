"""간단한 계산기 모듈 (일부러 버그를 심어둔 데모용)."""


def add(a, b):
    return a + b


def subtract(a, b):
    # 버그: 빼기인데 더하기로 잘못 구현되어 있음
    return a + b


def multiply(a, b):
    return a * b


def divide(a, b):
    # 버그: 0으로 나누는 경우를 처리하지 않아 ZeroDivisionError 발생
    return a / b
