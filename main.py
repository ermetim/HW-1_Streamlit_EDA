import os
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import plotly
import plotly.figure_factory as ff
from plotly.offline import iplot

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

fig, ax = plt.subplots()
plt.title('График распределения по параметру\n Возраст клиента')
ax.hist(df['AGE'], bins=50)

ax.set_xlabel('Возраст клиента')
ax.set_ylabel('Количество')
plt.grid('all')

fig

# Построение графика boxplot
st.subheader("Построим график boxplot")

hue_dict = {'GENDER' : 'Пол клиента (1 — мужчина, 0 — женщина)',
            'SOCSTATUS_WORK_FL' : 'Социальный статус клиента относительно работы (1 — работает, 0 — не работает)',
            'SOCSTATUS_PENS_FL' : 'Социальный статус клиента относительно пенсии (1 — пенсионер, 0 — не пенсионер)',
           }

hue = st.selectbox(
     'Выберите параметр "hue", по которому хотите посмотреть распределение',
     (hue_dict.keys()))
st.write(f'Вы выбрали: {hue} - {hue_dict[hue]}')

fig, ax = plt.subplots(figsize=(10, 10))
plt.title('График зависимости целевого признака от возраста', fontsize = 20)
ax = sns.boxplot(x="TARGET",
                 y="AGE",
                 hue=hue,
                 data=df,
                 palette="coolwarm",
                 showmeans=True)
plt.grid('all')
plt.grid('all')
# plt.legend(loc=1)
fig

st.write('Посмотрим основные числовые характеристики по возрасту')
st.table(round(df['AGE'].describe(), 1))
st.write('Самый распространенный возраст от 30 до 50 лет')


st.subheader("График распределения по параметру Личный доход клиента")

fig, ax = plt.subplots()
plt.title('График распределения по параметру\n Личный доход клиента (в рублях)')
ax.hist(df['PERSONAL_INCOME'], bins=200)

ax.set_xlabel('Личный доход клиента (в рублях)')
ax.set_ylabel('Количество')
ax.set_xlim([0, 40000])
plt.grid('all')
fig

st.subheader("Построим график boxplot")


fig, ax = plt.subplots(figsize=(10, 10))
plt.title('График зависимости целевого признака от возраста', fontsize = 20)
ax = sns.boxplot(x="TARGET",
                 y="PERSONAL_INCOME",
                 hue=hue,
                 data=df,
                 palette="coolwarm",
                 showmeans=True,
                 showfliers=1,
                )
plt.grid('all')
# plt.legend(loc=1)
fig


st.write('Посмотрим основные числовые характеристики по доходу')
st.table(round(df['PERSONAL_INCOME'].describe(), 1))
st.write('''Самый распространенный доход от 7000 до 20000 рублей.
         При этом есть привязки дохода к числам кратным 5000''')


# Построение матрицы корреляций признаков
st.subheader("Построим матрицу корреляций признаков")

crr = round(df[columns].corr(), 2)

fig, ax = plt.subplots(figsize=(15, 15))
# plt.title('Матрица корреляции признаков')#, fontsize = 20)
ax = sns.heatmap(crr,
                 annot = True,
                 cmap="YlGnBu",
                 linecolor='white',
                 linewidths=1,
                 annot_kws={"fontsize":10}
            )
fig

st.write('''Пары ярковыраженных зависимостей между признаками''')
st.table(abs(crr[(crr < 1) & (crr > -1)]).max().sort_values(ascending=False))

st.write('''
1. Наблюдается ярковыраженная зависимость между признаками LOAN_NUM_TOTAL и 
LOAN_NUM_CLOSED что довольно логично - количество выданных кредитов обычно 
коррелирует с количеством закрытых кредитов;\n
2. Наблюдается ярковыраженная обратная зависимость между признаками 
SOCSTATUS_WORK_FL и SOCSTATUS_PENS_FL. Это логично, ведь когда человек выходит
на пенсию, он обычно перестает работать;\n
3. Есть выраженная зависимость количества детей и иждевенцев. Зачастую дети и 
являются иждевенцами. Но так как это не всегда тае, то поэтому зависимость не 
такая сильная;\n
4. Есть выраженная зависимость возраста и пенсионного статуса, и это тоже логично.
''')
