import os
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly

# заголовок приложения
st.title('Домашнее задание по прикладному Python')

df = pd.read_csv('datasets/joined_dataset.csv')

# построение графиков распределений признаков

# st.text("Построим графики распределения признаков")
st.header("1. Построим графики распределения признаков")

columns = list(df.columns)
columns.remove('AGREEMENT_RK')

col_dict = {'AGREEMENT_RK' : 'Уникальный идентификатор объекта в выборке',
            'TARGET' : 'Целевая переменная: отклик на маркетинговую кампанию (1 — отклик был зарегистрирован, 0 — отклика не было)',
            'AGE' : 'Возраст клиента',
            'SOCSTATUS_WORK_FL' : 'Социальный статус клиента относительно работы (1 — работает, 0 — не работает)',
            'SOCSTATUS_PENS_FL' : 'Социальный статус клиента относительно пенсии (1 — пенсионер, 0 — не пенсионер)',
            'GENDER' : 'Пол клиента (1 — мужчина, 0 — женщина)',
            'CHILD_TOTAL' : 'Количество детей клиента',
            'DEPENDANTS' : 'Количество иждивенцев клиента',
            'PERSONAL_INCOME' : 'Личный доход клиента (в рублях)',
            'LOAN_NUM_TOTAL' : 'Количество ссуд клиента',
            'LOAN_NUM_CLOSED' : 'Количество погашенных ссуд клиента'
           }

option = st.selectbox(
     'Выберите параметр, по которому хотите посмотреть распределение',
     (columns))
st.write(f'Вы выбрали: {option} - {col_dict[option]}')

bins = st.number_input("Выберите количество корзин для  распределения",20, 200)

title_name = col_dict[option].split("(")[0]
if len(col_dict[option].split("(")) < 2:
    subtitle_name = ""
else:
    subtitle_name = col_dict[option].split("(")[-1][:-1]

fig, ax = plt.subplots()
plt.title(f'График распределения по параметру\n{title_name}\n{subtitle_name}')
ax.hist(df[option], bins=bins)

# ax.set_xlabel('Имя', loc='right')
ax.set_ylabel('Количество')
plt.grid('all')

fig

# построение графиков зависимостей целевой переменной и признаков
st.header("2. Построим графики зависимостей целевой переменной и признаков")
dep_cols = columns.copy()
dep_cols.remove('TARGET')

# Select box
option1 = st.selectbox(
     'Выберите параметр, от которого хотите посмотреть зависимость целевой переменной',
     (dep_cols))

st.write(f'Ваш выбор: {option1} - {col_dict[option1]}')
title_name = col_dict[option1].split("(")[0]
if len(col_dict[option1].split("(")) < 2:
    subtitle_name = ""
else:
    subtitle_name = col_dict[option1].split("(")[-1][:-1]

fig, ax = plt.subplots()
plt.title(f'График зависимости целевой переменной от параметра\n{title_name}\n{subtitle_name}')
ax.scatter(df[option1], df['TARGET'])

# ax.set_xlabel('Имя', loc='right')
# ax.set_ylabel('Целевая переменная')
plt.grid('all')

fig


