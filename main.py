import os
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import plotly
import plotly.figure_factory as ff
from plotly.offline import iplot

# Заголовок приложения
st.title('Домашнее задание по прикладному Python')

df = pd.read_csv('datasets/joined_dataset.csv')

# Сделаем копию для корреляции признаков
df_corr = df.copy()

# Приведем категориальные признаки от чисел к словам
df['GENDER'] = df['GENDER'].apply(lambda x: 'Мужчина' if x == 1 else 'Женщина')
st.text("Посмотрим на баланс по признаку Пол клиента")
st.table(df['GENDER'].value_counts())

df['SOCSTATUS_WORK_FL'] = df['SOCSTATUS_WORK_FL'].apply(lambda x: 'Работает' if x == 1 else 'Не работает')
st.text("Посмотрим на баланс по признаку Социальный статус клиента относительно работы")
st.table(df['SOCSTATUS_WORK_FL'].value_counts())

df['SOCSTATUS_PENS_FL'] = df['SOCSTATUS_PENS_FL'].apply(lambda x: 'Пенсионер' if x == 1 else 'Не пенсионер')
st.text("Посмотрим на баланс по признаку Социальный статус клиента относительно пенсии")
st.table(df['SOCSTATUS_PENS_FL'].value_counts())

df['TARGET'] = df['TARGET'].apply(lambda x: 'Отклик был' if x == 1 else 'Отклика не было')
st.text("Посмотрим на баланс по целевому признаку")
st.table(df['TARGET'].value_counts())

st.dataframe(df)

# Построение графиков распределений признаков

# st.text("Построим графики распределения признаков")
st.header("1. Построим графики распределения признаков")

# Yдалим AGREEMENT_RK, так как это просто идентификатор
columns = list(df.columns)
columns.remove('AGREEMENT_RK')

# Соберем словарь с описанием столбцов, чтобы использовать его в дальнейшем
col_dict = {'AGREEMENT_RK' : 'Уникальный идентификатор объекта в выборке',
            'TARGET' : 'Целевая переменная: отклик на маркетинговую кампанию',
            'AGE' : 'Возраст клиента',
            'SOCSTATUS_WORK_FL' : 'Социальный статус клиента относительно работы',
            'SOCSTATUS_PENS_FL' : 'Социальный статус клиента относительно пенсии',
            'GENDER' : 'Пол клиента',
            'CHILD_TOTAL' : 'Количество детей клиента',
            'DEPENDANTS' : 'Количество иждивенцев клиента',
            'PERSONAL_INCOME' : 'Личный доход клиента (в рублях)',
            'LOAN_NUM_TOTAL' : 'Количество ссуд клиента',
            'LOAN_NUM_CLOSED' : 'Количество погашенных ссуд клиента'
           }

fig, ax = plt.subplots() #figsize=(10, 10))
plt.title('График распределения по параметру \nВозраст клиента')
ax.hist(df['AGE'], bins=50)

ax.set_xlabel('Возраст клиента')
ax.set_ylabel('Количество')
plt.grid('all')

fig

# Построение графика boxplot
st.subheader("Построим график boxplot")

hue_dict = {'None': None,
            'GENDER' : 'Пол клиента',
            'SOCSTATUS_WORK_FL' : 'Социальный статус клиента относительно работы',
            'SOCSTATUS_PENS_FL' : 'Социальный статус клиента относительно пенсии',
           }

hue = st.selectbox(
     'Выберите параметр "hue", по которому хотите посмотреть распределение',
     (hue_dict.keys()))
st.write(f'Вы выбрали: {hue} - {hue_dict[hue]}')

if hue == 'None':
    hue = None

fig, ax = plt.subplots()#figsize=(10, 10))
plt.title('График зависимости целевого признака от возраста')#, fontsize = 20)
ax = sns.boxplot(x="TARGET",
                 y="AGE",
                 hue=hue,
                 data=df,
                 palette="coolwarm",
                 showmeans=True,
                 width=0.3
                 )
plt.grid('all')
ax.legend(title_fontsize = 8, prop = {'size' : 8})
fig

st.write('Посмотрим основные числовые характеристики по возрасту')
st.table(round(df['AGE'].describe(), 1))

st.write('''
На графике видно не нормальное распределение с небольшим хвостом в сторону увеличения возраста, 
поэтому наблюдаем незначительное смещение среднего относительно медианы на боксплоте.

Самый распространенный возраст от 30 до 50 лет
''')


# Построим график распределения по личному доходу клиента
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

hue_dict1 = {'None': None,
            'SOCSTATUS_WORK_FL' : 'Социальный статус клиента относительно работы',
            'GENDER' : 'Пол клиента',
            'SOCSTATUS_PENS_FL' : 'Социальный статус клиента относительно пенсии',
           }

hue1 = st.selectbox(
     'Выберите новый параметр "hue", по которому хотите посмотреть распределение',
     (hue_dict1.keys()))
st.write(f'Вы выбрали: {hue1} - {hue_dict1[hue1]}')

if hue1 == 'None':
    hue1 = None

fig, ax = plt.subplots()#figsize=(10, 10))
plt.title('График зависимости целевого признака от возраста')#, fontsize = 20)
ax = sns.boxplot(x="TARGET",
                 y="PERSONAL_INCOME",
                 hue=hue1,
                 data=df,
                 palette="coolwarm",
                 showmeans=True,
                 showfliers=0,
                 width=0.3,
                 )
plt.grid('all')
ax.legend(title_fontsize = 8, prop = {'size' : 8})
fig


st.write('Посмотрим основные числовые характеристики по доходу')
st.table(round(df['PERSONAL_INCOME'].describe(), 1))
st.write('''
На Графике видно не нормальное распределение с довольно большим хвостом в сторону 
увеличения дохода (на графике он обрезан). В связи с этим видно значительное 
смещение среднего относительно медианы.
Самый распространенный доход от 7000 до 20000 рублей.
При этом есть привязки дохода к числам кратным 5000
''')


# Построим График зависимости личного дохода от возраста
st.subheader("Построим график boxplot")

fig, ax = plt.subplots(2)#figsize=(10, 10))
plt.suptitle('График зависимости личного дохода от возраста')#, fontsize = 20)

for i in range(2):
    ax[i].scatter(x=df["AGE"], y=df["PERSONAL_INCOME"])
    ax[i].set_ylabel('Личный доход клиента')
    ax[i].grid('all')
ax[1].set_xlabel('Возраст')
ax[1].set_ylim([0, 60000])

fig


# Построение матрицы корреляций признаков
st.header("2. Построим матрицу корреляций признаков")

crr = round(df_corr[columns].corr(), 2)

fig, ax = plt.subplots()#figsize=(10, 10))
plt.title('Матрица корреляции признаков')#, fontsize = 40)
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
