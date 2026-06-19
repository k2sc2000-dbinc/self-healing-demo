"""간단한 계산기 모듈 (일부러 버그를 심어둔 데모용)."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    # 일부러 버그: 곱하기인데 더하기로 바꿔서 test_multiply가 실패하게 만듦
    return a + b


def divide(a, b):
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다.")
    return a / b
