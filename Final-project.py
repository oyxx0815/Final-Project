import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn')

st.title('Somethings related with hospital charges')

df = pd.read_csv('final.csv')
st.write(df)

form = st.sidebar.form("children_form")
children_filter = form.text_input('children number (0 - 5)', 'ALL')
form.form_submit_button("APPLY")

bmi_filter = st.slider("Maximum BMI:",16,53,27)

smoker_filter = st.sidebar.radio("Smoker or not:",('all','yes','no'))
sex_filter = st.sidebar.radio("sex:",('all', 'female', 'male'))

df = df[df.bmi <= bmi_filter]

if smoker_filter != "all":
    df = df[df.smoker == smoker_filter]

if sex_filter != "all":
    df = df[df.sex == sex_filter]

if children_filter != "ALL":
    df = df[df.children == int(children_filter)]
    


st.subheader('relation between region and charges')
fig, ax = plt.subplots(figsize=(10, 5))
m = df.groupby('region')['charges'].mean()
m.plot.bar(ax=ax)
st.pyplot(fig)

st.subheader('relation between age and charges')
fig, ax = plt.subplots(figsize=(10, 5))
df.plot.scatter(x = 'age', y = 'charges',ax=ax)
st.pyplot(fig)

st.subheader('bmi situations')
fig, ax = plt.subplots(figsize=(10, 5))
df['bmi'].plot.hist(bins = 10)
st.pyplot(fig)
