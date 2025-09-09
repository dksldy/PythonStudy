# form 패키지명 import 모듈명, ...
'''
from calculator import calc, utils

result = calc.add(10,5)
utils.show_result(result)
'''

# init 파일 설정 후
from calculator import add, subtract, show_result

result = add(10, 30)
show_result(result)
result = subtract(30, 10), add(20, 10), subtract(20, 1)
show_result(result)