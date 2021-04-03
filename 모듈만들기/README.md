# 모듈 생성하는 방법

1. 모듈로 사용하기 위한 함수를 넣은 .py를 생성한다.
    
    예시

        def add(value1, value2):
            return value1 + value2
        def subtract(value1, value2):
            return value1 - value2
        def multiply(value1, value2):
            return value1 * value2
        def divide(value1, value2):
        return value1 / value2

2. 새로운 .py에서 만든 모듈을 불러온다.
    
    예시
        
        import calculator_module

3. 불러온 모듈을 사용한다.
    > calculator_module.[불러올함수명]
    > calculator_module.[변수명] # 변수도 불러올 수 있다.

    예시
    
        print('20 + 10 = ', calculator_module.add(20, 10))
        print('20 - 10 = ', calculator_module.subtract(20, 10))
        print('20 * 10 = ', calculator_module.multiply(20, 10))
        print('20 / 10 = ', calculator_module.divide(20, 10))

+ from, import 로도 사용 가능하다.

    예시
        from calculator_module import add
        add(20, 10)