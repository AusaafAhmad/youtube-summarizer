import streamlit as st
import Transcript
from model import summarize


st.header("Youtube Video Summmarizer")
with st.sidebar:
    st.header("About This App")
    st.markdown("""

        Made by Ausaaf Ahmad
        """)
    
with st.form("root"):
    link = st.text_input("Paste Youtube Video Link Here")
    st.form_submit_button()
    
    

if link:
    transcript = Transcript.get_transcript(link)
    st.header("Summary")
    st.write(summarize(transcript).split("</think>")[-1])
    st.header("Transcript")
    st.write(transcript)