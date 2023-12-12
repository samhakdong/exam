from matplotlib import figure, pyplot as plt
import streamlit as st
import numpy as np
import pandas as pd

import os
os.system('cls')

import streamlit as st

col1, col2 = st.columns(2)
with col1:
    st.image('독도.jpg', width=200)
with col2:
    st.write('박건호')
    '전화번호(☎) : 010-xxx-xxxx'
    '이메일(📧) : supershy@konyang.ac.kr'
    '주소(🏚️) 충청남도 논산시 대학로 121'

col = st.columns(4)
with col[0]:
    st.link_button("Google(🌎)", "https://google.com/")
with col[1]:
    st.link_button("Naver(✔️)", "https://www.naver.com/")
with col[2]:
    st.link_button("Daum(☑️)", "https://www.daum.net/")
with col[3]:
    st.link_button("Facebook(🇫)", "https://www.facebook.com/")

col = st.columns(2)
with col1:
    st.write('자기소개')
    '저는 이런 사람 입니다!'
    '1.도전 정신'
    '2.꾸준한 자기계발'
    '3.창의적인 사고'
    ''
    '명언'
    '포기하면 그 순간이 바로 시합 종료에요'
    '(슬램덩크 안감독)'






# import matplotlib.pyplot as plt
# fig, ax = plt.subplots()






# st.write('Hello, world 웃음')
# 'Hello, *world!* **tt** ***ccc***'

# fig, ax = plt.subplots()
# x = []
# y = []
# for i in range(-10, 11, 2):
#     x.append(i)
#     y.append(3*i**3 - 5*i**2 + 3*i - 7)

# cc = st.radio('선의 색을 선택하시오', ['red', 'green', 'blue', 'orange'])
# ma = st.radio('마커의 형태를 선택하시오', ['o', '^', 's', 'p', 'h'])
# ls = st.radio('선의 형태를 선택하시오', [ '-', '-.', ':', '--'])
# plt.plot(x, y, color= cc, linestyle= ls, marker=ma)
# st.pyplot(fig)

# fig, ax = plt.subplots()

# a = 2
# b = -5
# c = 3
# d = -7

# x = []
# y = []
# for i in range(-100, 101, 50):
#     x.append(i)
#     y.append(a*i**3 + b*i**2 + c*i + d)

# col1, col2, col3 = st. columns(3)
# with col1:
#     color = st.radio('색을 선택하시오.', ('red', 'green', 'blue'))
# with col2:
#     linestyle = st. radio('선의 스타일을 선택하시오.', ('-', '-.', ':'))
# with col3:
#     marker = st. radio('마커의 스타일을 선택하시오.', ('s', '^', 'o'))
    

# plt.plot (x, y, color = color, marker = marker, linestyle = linestyle)
# st.pyplot(fig)

# color = st.radio('color', ('red', 'green', 'blue'))

# if 'red' in color:
#     t = '-r^'
# if 'green' in color:
#     t = '-g^'
# if 'blue' in color:
#     t = '-b^'



# plt.plot(x, y, t)
# st.pyplot(fig)





# list1 = list([['한빛', '남자', '20', '180'],
#         ['한결', '남자', '21', '177'],
#         [' 김한결', '중성', '51', '155'],
#         ['현라', '여자', '20', '160']])
# n = np.array(list1)
# col_names = ['이름', '성별', '나이', '키']
# df = pd.DataFrame(list1, columns=col_names, index=['1행','2행', '3행', '4행'])
# df

# genre = st.radio("선택하시오.",
#     ["오름차순", "내림차순", "기타", "요약"],
#         horizontal =True, index=2)

# number = st.number_input('Insert a numver', value=20, step=1)
# df.iloc[3,2] = number

# if '오름' in genre:
#     st.dataframe(df.sort_values(by=['키']))
# if '내림' in genre:
#     st.dataframe(df.sort_values(by=['키'], ascending=False))
# if '기타' in genre:
#     st.dataframe(df)
# if '요약' in genre:
#     st.dataframe(df.describe())


# li = [1, 2, 3, 4]
# n = np.array(li)
# p = pd.Series(li)

# li = [1, 2, 3, 4]
# li

# for i in range(4):
#     li[i] = li[i] +3
# li
# li = np.array([1, 2, 3, 4])
# li
# li_sort = np. sort(li)[::-1]
# li_sort




# a = np.array([1, 10, -5, 2])
# print(np.abs(a))
# print(np.sqrt(a))
# print(a**0.5)
# print()

# a = np.arange(8)
# a
# a.shape = (2, 4)
# a
# b = a.flatten()
# b
# b.reszie((2,4))
# b


# 중간고사
# n = 5
# arr = np.full((n,n), '나머지')
# arr

# for i in range(n):
#     for j in range(n):
#         arr[i, j] = '나머지'
#         if i == j:
#             arr[i,j] = '대각선'
#         if i + j == 4:
#             arr[i, j] = '대각선'
# arr

# n = 100
# for i in range(1, n+1):
#     if 1%7 == 3:
#         i


# list1 = [(10, 10, 10, 10, 10), (10, 10, 10, 10, 10),(10, 10, 10, 10, 10),(10, 10, 10, 10, 10)]
# a = np.array(list1)
# a

# e = np.eye(7)
# 'e\n', e

# def user_eye(n):
#     arr = np.zeros((n,n))
#     for i in range(n):
#         for j in range(n):
#             if i == n-j-1:
#                 arr[i, j] = 1
#     return arr
# arr = user_eye(10)
# arr


# n =50
# for i in range(1, n):
#     if i % 7 == 3:
#         i





# list1 =  [(1, 2, 3, 4), (3, 5, 7, 9)]
# a = np.array(list1)
# a

# a.ndim
# n = np.ndim(a)
# n


# a= np.zeros(2)
# 'a\n' , a
# b = np.zeros((2,2))
# 'b\n', b
# c = np.ones((2,3))
# 'c\n', c
# d = np.full((2,3), 5)
# 'd\n', d
# e = np.eye(3)
# 'e\n', e



# list1 =  [(1, 2, 3, 4), (3, 5, 7, 9)]
# a = np.array(list1)
# a
# # a + 10
# a.shape
# s = a.sum(axis=0)
# s
# mn = a.min(axis=0)
# mn


# s = 0
# for i in range(2, 10+1, 2):
#     s = s + 




# list_1 = [1, 2, 7, 4, 50, 33]
# s = sum(list_1)
# mx = max(list_1)
# mn = min(list_1)
# s,mx, mn


# def sta(arr):
#     s = 0
#     mx = -1e10
#     mn = 1e10
#     for i in arr:
#         s = s + i
#         if mx < i:
#             mx = i
#         if mn > i:
#             mn = i
#     arr
#     'sum = ', s, 'min = ', mn, 'max = ', mx
#     return s, mx, mn
# # sta([5, 13, 7, 4, 11])



# list_1 = [5, 13, 7, 4, 11]
# [s1, mx1, mn1] = sta(list_1)
# s1, mx1, mn1



# import turtle

# t = turtle.Turtle()
# t. shape('turtle')

# t.speed(1)

# t.left(90)
# t.forward(200)
# t.backward(100)
# t.left(90)
# t.forward(100)
# t.left(180)
# t.forward(100)
# t.backward(200)
# turtle.done()






# st.write('파이썬의 세계에 오신 것을 환영합니다.')





# r = 15
# Area = 3.14*r*r
# Area
# st.write(Area)
# print(Area)

# a = 11
# b = 4

# print('덧셈 결과', a + b)
# print('뺄셈 결과', a - b)
# print('곱셈 결과', a * b)
# print('나눗셈 결과', a / b)
# print('나눗셈 정수 몫', a // b)
# print('나눗셈 나머지', a % b)
# print('거듭제곱 결과', a**b)


# a = 5
# if a == 5:
#     print('Right!')
#     print('a is 5')
# if a ==3:
#     print('Right!')
#     print('a is 3')
# if a != 3:
#     print('Right')
#     print('a is not 3')

# grade = 72
# if grade >= 90:
#     'A'
# elif grade >= 80:
#     'B'
# elif grade >= 70:
#     'C'

# a = 5
# if a < 5:
#     print('a is smaller than 5')
# elif a > 5:
#     print('a is larger than 5')
# else:
#     print('a is 5')

# 'a' + 'bcd' + str(5)
# 'a' + 'bcd' + '5'

# for a in range(2, 10):
#     a, '단입니다'
#     for i in range(1, 10, 1):
#         b = str(a) + 'X' + str(i) + ' = ' + str(a*i)
#         b

# li = [1, 2, 3, 4, 5, 1, 3]
# li.append(100)
# li
# c = li.count(0)
# c
# ty = type(li)
# ty

# li.sort(reverse=True)
# li

# list_1 = [1, 2, 3, 4, 5, 1, 3]
# list_2 = []
# list_1
# list_2
# len(list_1)

# list_1[3] = 9999
# list_1
# list_1.append(100)
# list_1

# list_1.remove(9999)
# list_1
# list_1.insert(0,777)
# list_1

# list_2 = list_1.copy()
# list_2

# list_1 = [897, 2, 1, 4, 99, 5.24, 17]
# list_1

# list_1.reverse()
# list_1

# list_1.sort()
# list_1

# list_1.sort(reverse=True)
# list_1

# dict_1 = {'name':'홍길동', 
#         'birth':1990,
#         'addrss':'KR'
#         }
# dict_1
# dict_1['birth']

# dict_1['weight'] = 60.5
# dict_1['family'] = ['아빠', '엄마', '여동생']
# dict_1

# dict_1.update({'weight':67.8,'hobby': ['게임', '독서']})
# dict_1

# dict_1['hobby'] = ['축구', '등산']
# dict_1

# del dict_1['weight']
# dict_1

# for key in dict_1.keys():
#     key
# for i in dict_1.values():
#     i
# for k, v in dict_1.items():
#     k
#     v

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

