import calculator_module # 엔트리포인트가 아니기 때문에 __name__이 main이 아니다.

print('20 + 10 = ', calculator_module.add(20, 10))
print('20 - 10 = ', calculator_module.subtract(20, 10))
print('20 * 10 = ', calculator_module.multiply(20, 10))
print('20 / 10 = ', calculator_module.divide(20, 10))

print('use_calculator.py', __name__)
if __name__ == '__main__': # __name__이 '__main__'이면 엔트리포인트이다.
    print('user_calculator.py 엔트리포인트')