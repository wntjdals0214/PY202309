import operator
import os, re
import requests
import urllib.request as ur
from bs4 import BeautifulSoup as bs

sentences = [] # 문장을 담을 빈 리스트 생성

url = 'https://quotes.toscrape.com/tag/life/'
html = ur.urlopen(url)
soup = bs(html.read(), 'html.parser')
quotes = soup.find_all('div', {"class":"quote"})
for quote in quotes:
    quote = quote.find_all('span', {"class":"text"})
    for i in quote:
        sentences.append(i.text) # 만들어둔 리스트에 소문자로 바꿔 추가

total_terms = set()

tokens = [] # 빈 리스트 생성
for sentence in sentences:
    token = sentence.replace("."," ").replace(","," ").replace("“"," ").replace("”"," ").strip().split(" ") # 필요없는 것 제거, 공백 기준으로 토큰 쪼개기
    for i in token:
        tokens.append(i.lower()) # 만들어둔 리스트에 소문자로 바꿔 추가
total_terms = set(tokens) # 집합으로 만들어 중복 토큰 제거
term_frequency_dict = {} # 토큰 별 단어 빈도 저장할 딕셔너리

token_list = list(total_terms) # 집합을 리스트로 변환
for token in (token_list):
    count = 0
    for word in tokens:
        if token == word:
            count += 1 # token_list에서 토큰을 하나씩 tokens 리스트에 있는 토큰들과 비교해가며 중복 개수 카운트
    term_frequency_dict[token] = count # 만들어둔 딕셔너리에 저장
del term_frequency_dict[''] # 공백이 단어 딕셔너리에 저장되는것 방지

# 토큰 빈도 출력
print("-----TF dictionary-----")
print(term_frequency_dict)

print("-----Top-5 TF terms-----")
# TODO 3: Top-3 토큰 빈도를 갖는 단어의 순위, 단어, 빈도 출력 코드 작성
sorted_frequency_tokens = sorted(term_frequency_dict.items(), key = operator.itemgetter(1), reverse = True)
# 딕셔너리 value값 내림차순 정렬
for i in range(0,5):
    sorted_frequency = list(sorted_frequency_tokens[i]) # 튜플을 리스트화 시켜서 연산가능하게 
    print(i+1, sorted_frequency[0], sorted_frequency[1])
    # 가장 많이 나타난 단어와 빈도 5개 출력
