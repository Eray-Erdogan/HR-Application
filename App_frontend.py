# The below frontend code is provided by AWS and Streamlit. I have only modified it to make it look attractive. import streamlit as st
import App_backend as demo ### replace rag_backend with your backend filename
import streamlit as st

st.set_page_config(page_title="HR Q and A with Eray") ### Modify Heading
new_title = '<p style="font-family: sans-serif; color: Green; font-size: 42px;">HR Q & A with Eray ' \

st.markdown (new_title, unsafe_allow_html=True)


if 'vector_index' not in st.session_state:
    with st.spinner ("Wait for magic... All beautiful things in life take time :-)"): ###spinner message
        st.session_state.vector_index = demo.hr_index() ### Your Index Function name from Backend File

input_text = st.text_area("Input text", label_visibility="collapsed")
go_button= st.button("Learn GenAI with Bayram Eray Erdoğan", type="primary") ### Button Name


if go_button:
    with st.spinner ("Anytime someone tells me that I can't do something, I want to do it more Taylor Swift"):
        response_content= demo.hr_rag_response(index=st.session_state.vector_index, question=input_text) #### repla
        st.write(response_content)