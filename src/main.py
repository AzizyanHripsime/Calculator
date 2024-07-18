from typing import Union

class Calculator:
    def add(self, a: Union[int, float], b:Union[int, float]) -> int | float:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError('Both arguments should be numeric')
        return a+b

    def divide(self, a: Union[int, float], b:Union[int, float]) -> int | float:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError('Both arguments should be numeric')
        if b==0:
            raise ZeroDivisionError('Cannot divide by zero')
        return a/b

    def minus(self, a: Union[int, float], b: Union[int, float]) -> int | float:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError('Both arguments should be numeric')
        return a - b

    def mul(self, a: Union[int, float], b: Union[int, float]) -> int | float:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError('Both arguments should be numeric')
        return a*b

if __name__ =='__main__':
    b = Calculator()