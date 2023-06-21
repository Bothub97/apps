import streamlit as st
import pandas as pd

app_title = "Fraud $ Identity Theft Report 🦓"
app_sub_title = "source : Federal Trade commission"

def main():
    st.set_page_config(app_title)
    st.title(app_title)
    st.caption(app_sub_title)

    # load data
    df = pd.read_csv(r'C:\Users\hepl\OneDrive - Hemas Enterprises pvt Ltd\backup\Desktop\New folder\smdb\data\AxS-Fraud Box_Full Data_data.csv')

    year = 2022
    quarter = 1
    state_name = 'Texas'
    report_type = 'Fraud'
    field_name = 'State Fraud/Other Count'
    metric_title = f'#{report_type} Reports'

    df = df[(df['Year'] == year) & (df['Quarter'] == quarter) & (df['Report Type']== report_type)]

    if state_name:
        df = df[df['State Name'] == state_name]

    df.drop_duplicates(inplace=True)
    total = df['field_name'].sum()
    st.metric(metric_title,total)
   

    st.write(df.shape)
    st.write(df.head())
    st.write(df.columns)



    # display filters and map



    # display metrices


if __name__ == "__main__":
    main()
