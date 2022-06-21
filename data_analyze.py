# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 19:45:04 2022

@author: asus
"""
import os
import  pandas as pd
import numpy as np 
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt 
from matplotlib.ticker import MaxNLocator

def Merge():
    count_list =[]
    inputdir=r'xls//'
    df_empty=pd.DataFrame(columns=['author','project_hours','non_project_hours','project_non_project_ratio'])
    for parents, dirnames, filenames in os.walk(inputdir):
        for filename in filenames:
            df=pd.read_excel(os.path.join(parents,filename))
            len_sum =len(df)
            df_condition_columns = df[['project_non_project_ratio']]
            count_list.append(np.int64(df_condition_columns <85).sum().item()) #COUNTIF(< 85 in df_condition_columns column)and int64 to int to append count_list  
            df_empty=df_empty.append(df,ignore_index=False)
        return  df_empty, count_list,len_sum
       

def plot():
    get_merge_df,get_count_list,get_len_sum = Merge()
    percentage=[]
    weeks =[]
    print(get_count_list,'\n', get_len_sum)
    for value in get_count_list:
        percentage.append(int((value/get_len_sum)*100)) #比率取整數
    print(percentage)
    
    
    for index in range( len(get_count_list)):
        weeks.append(index + 1)
    weeks = np.array(weeks)
    percentage = np.array(percentage)
    '''
    model2 = make_interp_spline(weeks, percentage)#平滑曲線
    xs2=np.linspace(1,len(weeks) , 500)#均勻地撒點 1~len(weeks)取500樣點
    ys2=model2(xs2)
    plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))#x軸為整數
    plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))#y軸為整數
    plt.plot(xs2,ys2)
    plt.title("Work efficiency statistics")
    plt.xlabel("Weeks")
    plt.ylabel("failures")
    plt.show()
    '''
    plt.title("Work efficiency statistics")
    plt.plot(weeks,percentage,'s-',color = 'r', label="Failures_Percentage")
    plt.legend(loc = "best", fontsize=20)
    plt.xlabel("Weeks", fontsize=30, labelpad = 15)
    plt.ylabel("percentage ", fontsize=30, labelpad = 20)
    plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))#x軸為整數
    plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))#y軸為整數
    plt.show()

if __name__ == '__main__':
    plot()
    