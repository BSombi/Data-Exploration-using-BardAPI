from bardapi import Bard
import os
import pandas as pd
import streamlit as st

#Headings
st.markdown(" # <span style='color:blue'>Wellcome!</span> This App will help you Explore and understand your data", unsafe_allow_html=True)
st.info("Upload your CSV data and proceed to asking the questions")

os.environ['_BARD_API_KEY']="WAgfaacFovM6livq4Boqxmy0okx470y79XcqGXmj7DlYfGJencks2EVlQZqGTkDwE79OuA."

file = st.file_uploader("Upload your CSV file", type=["csv"])
if file: 
    my_data = pd.read_csv(file, index_col=None)
        # df.to_csv("dataset.csv", index=None)
    st.dataframe(my_data)
    
    input_text = st.text_input("Ask your data question")
    
    answer = Bard().get_answer(f'{input_text} this data {my_data}')['content']
    st.write(f'{answer}')

    # if st.button("Get Answer"):
    #     answer = Bard().get_answer(f'{input_text} this data {my_data}')['content']
    #     st.write(answer)

else:
    st.write("There is no data upload")