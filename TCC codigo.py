# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 13:23:02 2023

@author: e-pedro.soares
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel('Base.xlsx')

escolas_unicas = data['Nomedaescola'].unique()

dfs = {}

for school in escolas_unicas:
    df_school = data.loc[data['Nomedaescola'] == school]
    dfs[school] = df_school
    
escola_controle1 = dfs['Centro de Ensino Fundamental Jardim II']
escola_tratada = dfs['Centro de Ensino Fundamental Queima Lençol']
escola_controle2 = dfs['Centro de Ensino Fundamental Rio Preto']

escola_controle1['Time_tra'] = pd.to_datetime(escola_controle1['Time_tra'])
escola_controle2['Time_tra'] = pd.to_datetime(escola_controle2['Time_tra']) #.dt.date if needed
escola_tratada['Time_tra'] = pd.to_datetime(escola_tratada['Time_tra'])

escola_controle1['Time_tra'] = escola_controle1['Time_tra'].dt.month
escola_controle2['Time_tra'] = escola_controle2['Time_tra'].dt.month
escola_tratada['Time_tra'] = escola_tratada['Time_tra'].dt.month

escola_controle1 = escola_controle1[['matriculadoaluno_num', 'porcent_acertos_pt', 'porcent_acertos_mat', 'Time_tra']]
escola_controle2 = escola_controle2[['matriculadoaluno_num', 'Time_tra', 'porcent_acertos_pt', 'porcent_acertos_mat']]
escola_tratada = escola_tratada[['matriculadoaluno_num', 'Time_tra', 'porcent_acertos_pt', 'porcent_acertos_mat']]

controle1 = escola_controle1.pivot(index=['matriculadoaluno_num'], columns='Time_tra', values=['porcent_acertos_pt', 'porcent_acertos_mat'])
controle1.columns = [f"{col}_Month{month}" for col, month in controle1.columns]
controle1 = controle1.reset_index()

controle2 = escola_controle2.pivot(index=['matriculadoaluno_num'], columns='Time_tra', values=['porcent_acertos_pt', 'porcent_acertos_mat'])
controle2.columns = [f"{col}_Month{month}" for col, month in controle2.columns]
controle2 = controle2.reset_index()

tratada = escola_tratada.pivot(index=['matriculadoaluno_num'], columns='Time_tra', values=['porcent_acertos_pt', 'porcent_acertos_mat'])
tratada.columns = [f"{col}_Month{month}" for col, month in tratada.columns]
tratada = tratada.reset_index()







intervals = ['1%-25%', '26%-50%', '51%-75%', '76%-100%']

# Create a dictionary to store the counts
count_dict = {'Interval': intervals, 'Count': []}

# Count the occurrences of numbers in each interval
for i in range(len(intervals)):
    start = i * 25 + 1
    end = (i + 1) * 25
    count = tratada[(tratada['porcent_acertos_pt_Month5'] >= start) & (tratada['porcent_acertos_pt_Month5'] <= end)].shape[0]
    count_dict['Count'].append(count)
    
tratada_count_pt_5 = pd.DataFrame(count_dict)

count_dict = {'Interval': intervals, 'Count': []}

for i in range(len(intervals)):
    start = i * 25 + 1
    end = (i + 1) * 25
    count = tratada[(tratada['porcent_acertos_mat_Month5'] >= start) & (tratada['porcent_acertos_mat_Month5'] <= end)].shape[0]
    count_dict['Count'].append(count)
    
tratada_count_mat_5 = pd.DataFrame(count_dict)



count_dict = {'Interval': intervals, 'Count': []}

# Count the occurrences of numbers in each interval
for i in range(len(intervals)):
    start = i * 25 + 1
    end = (i + 1) * 25
    count = tratada[(tratada['porcent_acertos_pt_Month12'] >= start) & (tratada['porcent_acertos_pt_Month12'] <= end)].shape[0]
    count_dict['Count'].append(count)
    
tratada_count_pt_12 = pd.DataFrame(count_dict)

count_dict = {'Interval': intervals, 'Count': []}

for i in range(len(intervals)):
    start = i * 25 + 1
    end = (i + 1) * 25
    count = tratada[(tratada['porcent_acertos_mat_Month12'] >= start) & (tratada['porcent_acertos_mat_Month12'] <= end)].shape[0]
    count_dict['Count'].append(count)
    
tratada_count_mat_12 = pd.DataFrame(count_dict)



count_dict = {'Interval': intervals, 'Count': []}

# Count the occurrences of numbers in each interval
for i in range(len(intervals)):
    start = i * 25 + 1
    end = (i + 1) * 25
    count = controle1[(controle1['porcent_acertos_pt_Month5'] >= start) & (controle1['porcent_acertos_pt_Month5'] <= end)].shape[0]
    count_dict['Count'].append(count)
    
controle_count_pt_5 = pd.DataFrame(count_dict)

count_dict = {'Interval': intervals, 'Count': []}

for i in range(len(intervals)):
    start = i * 25 + 1
    end = (i + 1) * 25
    count = controle1[(controle1['porcent_acertos_mat_Month5'] >= start) & (controle1['porcent_acertos_mat_Month5'] <= end)].shape[0]
    count_dict['Count'].append(count)
    
controle_count_mat_5 = pd.DataFrame(count_dict)

count_dict = {'Interval': intervals, 'Count': []}

# Count the occurrences of numbers in each interval
for i in range(len(intervals)):
    start = i * 25 + 1
    end = (i + 1) * 25
    count = controle1[(controle1['porcent_acertos_pt_Month12'] >= start) & (controle1['porcent_acertos_pt_Month12'] <= end)].shape[0]
    count_dict['Count'].append(count)
    
controle_count_pt_12 = pd.DataFrame(count_dict)

count_dict = {'Interval': intervals, 'Count': []}

for i in range(len(intervals)):
    start = i * 25 + 1
    end = (i + 1) * 25
    count = controle1[(controle1['porcent_acertos_mat_Month12'] >= start) & (controle1['porcent_acertos_mat_Month12'] <= end)].shape[0]
    count_dict['Count'].append(count)
    
controle_count_mat_12 = pd.DataFrame(count_dict)



plt.bar(controle_count_mat_5['Interval'], controle_count_mat_5['Count'])
plt.xlabel('Intervalo')
plt.ylabel('Quantidade')
plt.title('Notas em Matemática Antes - Controle')
plt.savefig('Notas em Matemática Antes - Controle.png')
plt.show()

plt.bar(controle_count_mat_12['Interval'], controle_count_mat_12['Count'])
plt.xlabel('Intervalo')
plt.ylabel('Quantidade')
plt.title('Notas em Matemática Depois - Controle')
plt.savefig('Notas em Matemática Depois - Controle.png')
plt.show()

plt.bar(controle_count_pt_5['Interval'], controle_count_pt_5['Count'])
plt.xlabel('Intervalo')
plt.ylabel('Quantidade')
plt.title('Notas em Português Antes - Controle')
plt.savefig('Notas em Português Antes - Controle.png')
plt.show()

plt.bar(controle_count_pt_12['Interval'], controle_count_pt_12['Count'])
plt.xlabel('Intervalo')
plt.ylabel('Quantidade')
plt.title('Notas em Português Depois - Controle')
plt.savefig('Notas em Português Depois - Controle.png')
plt.show()

plt.bar(tratada_count_mat_5['Interval'], tratada_count_mat_5['Count'])
plt.xlabel('Intervalo')
plt.ylabel('Quantidade')
plt.title('Notas em Matemática Antes - Tratada')
plt.savefig('Notas em Matemática Antes - Tratada.png')
plt.show()

plt.bar(controle_count_mat_12['Interval'], controle_count_mat_12['Count'])
plt.xlabel('Intervalo')
plt.ylabel('Quantidade')
plt.title('Notas em Matemática Depois - Tratada')
plt.savefig('Notas em Matemática Depois - Tratada.png')
plt.show()

plt.bar(controle_count_pt_5['Interval'], controle_count_pt_5['Count'])
plt.xlabel('Intervalo')
plt.ylabel('Quantidade')
plt.title('Notas em Português Antes - Tratada')
plt.savefig('Notas em Português Antes - Tratada.png')
plt.show()

plt.bar(controle_count_mat_12['Interval'], controle_count_mat_12['Count'])
plt.xlabel('Intervalo')
plt.ylabel('Quantidade')
plt.title('Notas em Português Depois - Tratada')
plt.savefig('Notas em Português Depois - Tratada.png')
plt.show()