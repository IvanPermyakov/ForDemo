import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)
    district = pd.read_csv('district.csv').set_index('id')
    district = st.sidebar.selectbox('Выберите район', district.index, format_func=lambda x: district['name'].loc[x])
    numRoom = pd.read_csv('numRoom.csv').set_index('id')
    numRoom = st.sidebar.selectbox('Выберите количество комнат', numRoom.index, format_func=lambda x: numRoom['name'].loc[x])
    AllData = pd.read_csv('data.csv')


    FilterData = AllData[(AllData['district'] == district) & (AllData['numRoom'] == numRoom)]
    

    fig, ax = plt.subplots(2, 1)
    fig.subplots_adjust(top=3)
    sns1 = sns.barplot(x='districtName', y='cost', data=AllData, color='blue', linewidth = 0.01, ax=ax[0])
    sns1.set_title('Стоимость относительно к району')
    sns1.tick_params(axis='both', which='major', labelsize= 5 ) 
    sns1.set_xlabel('Район', fontsize=8)
    sns1.set_ylabel('Стоимость', fontsize=8)

    sns2 = sns.barplot(x='square', y='cost', data=FilterData, color='blue', linewidth = 0.01, ax=ax[1])
    sns2.set_title('Стоимость относительно к площади')
    ax[1].set(xticklabels='')
    sns2.set_xlabel('Площадь', fontsize=8)
    sns2.set_ylabel('Стоимость', fontsize=8)

    

    FilterData = FilterData.drop(['district', 'numRoom'], axis=1)
    st.dataframe(FilterData, use_container_width=True)
    
    st.write(fig)



if __name__ == "__main__":
    main()