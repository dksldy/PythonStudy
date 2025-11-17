# 정규 표현식 (Regular Expressions)
# : 문자열에서 특정 패턴을 기준으로 검색 / 추출 / 변환 하는 기술

# 내장 모듈 re 사용
import re

def practice1():
  data = 'data-1234-5678'

  # match(패턴, 문자열) : 문자열의 시작이 패턴가 일치 하는지 확인
  if re.match(r'data', data):
    print('문자열은 data로 시작')
  else:
    print('문자열은 data로 시작되지 않습나')
# practice1()

def practice2():
  # 이메일 검증
  #     sample@test.com -> 문자 @ 문자.문자
  #   * 표준 이메일 패턴 : ^[\w\.-]+@[\w\.-]+\.\w+$
  print('검증 시작 ---- *')
  # email = "chl2347@naver.com"
  email = "chl2347@naver.co/m"
  pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

  if re.match(pattern, email):
    print(f'{email} : 유효한 이메일입니다.')
  else:
    print(f'{email} 유효하지 않은 이메일 입니다.')
# practice2()

def practice3():
  # 연락처 패턴
  #         010-1234-1234 => 010-숫자4자리-숫자4자리
  #     * 표준 연락처 패턴 : 010-\d{4}-\d{4}

  data = '문의는 010-1234-5678 로 바랍니다.'

  phone = re.search(r'010-\d{4}-\d{4}', data)
  print(phone)      # Match 객체가 반환됨.

  # 검색한 결과를 사용하고자 할 경우 group() 사용
  print(phone.group())      # 결과 데이터 바로 출력
# practice3()

def practice4():
  # 주민등록번호 뒷자리 마스킹(숨기기)
  data = '홍길동 001117-3123456'
  # 주민 번호 => 숫자6자리-숫자7자리
  # masking = re.sub(r'(\d{6})-(\d{7})', r'\1-*******', data)
  masking = re.sub(r'(\d{6})-(\d)(\d{6})', r'\1-\2*******', data)
  print(masking)
# practice4()

def practice5():
  # 스크래핑 -> HTML 태그가 포함되어 있는 문자열
  #   태그 제거

  html = '<p>Hello <b>World</b></p>'
  # => 패턴 : <.*?>
  rm_tag = re.sub(r'<.*?>', '', html)
  print(rm_tag)
# practice5()