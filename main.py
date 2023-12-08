import os
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# заголовок приложения
st.title('Домашнее задание по прикладному Python')

df = pd.read_csv('datasets/joined_dataset.csv')
# st.text("Введите ваш рост")

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
st.write(f'You selected: {option} - {col_dict[option]}')


# fig, ax = plt.subplots()
# ax.hist(df[option], bins=50)
# plt.grid('all')
#
# fig

plt.hist(df[option], bins=50)
plt.grid('all')
# plt.show()
