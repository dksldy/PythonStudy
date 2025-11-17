# 람다 (lambda) : 익명함수를 한 줄로 표현하는 방법

def practice1():
  # 람다 기본
  
  square = lambda x: x**2
  """
      def square(x):
        return x**2
  """
  print(square(4))
# practice1()

def practice2():
  # map 함수에 lambda 적용
  numbers = [1,2,3,4]
  
  # 각 요소에 2배하여 리스트 재구성
  result = list(map(lambda n:n*2, numbers))
  print(result)
# practice2()

def practice3():
  #filter 함수에 lambda 적용
  numbers = [3,6,9,12,15]

  # 6의 배수만 추출하여 리스트로 재구성
  result = list(filter(lambda n:n%6 == 0, numbers))
  print(result)
# practice3()

def practice4():
  # 정렬 기준을 람다로 표현
  words = ['java', 'python', 'sql', 'javascropt', 'html',]

  # st_words = sorted(words) # => 오름차순(기본)(sorted)
  # st_words = sorted(words, reverse=True) # => 내림차순(reverse항목 True)

  #글자수 기준으로 정렬
  st_words_ = sorted(words)
  st_words = sorted(words, key=lambda w: len(w)) # => 기준을 요소의 길이로 설정 (key 항목)
  print(st_words)
# practice4()

def practice5():
  products = [
    {'name' : 'keyboard', 'price': 40000},
    {'name' : 'mouse', 'price': 20000},
    {'name' : 'monitor', 'price': 100000},
    {'name' : 'speaker', 'price': 5000},
    {'name' : 'applepad', 'price': 20000},
  ]

  #가격, 이름 순으로 정렬 -> 튜플
  result = sorted(products, key = lambda item: (item.get('price'), item['name']))
  # => 방식 두가지 (item.get('price'), item['price']) -> 통일하는게 좋음
  print(result)
# practice5()

def practice6():
  # 숫자 관련 전처리
  prices = ['\ 10,000', '\ 5,500', '\,\ 300,000']
  # 원화표시(\) 제거, 콤마(,) 제거, 공백 제거
  result = list(map(lambda p: int(p.replace('\\','').replace(',', '').strip()), prices))
  print(result)
practice6()