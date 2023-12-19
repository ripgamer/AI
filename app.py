import os
from dotenv import load_dotenv      #import dotenv to load .env file
import google.generativeai as genai #import google genai
import streamlit as st              #import streamlit

load_dotenv()                       #load .env file
api_key = os.getenv('API_TOKEN')    #get api token from .env file
Nobita = os.getenv('NOBITA')        #get nobita character info from .env file
Doremon = os.getenv('DOREMON')      #get doremon character info from .env file
Shizuka = os.getenv('SHIZUKA')      #get shizuka character info from .env file
Gian = os.getenv('GIAN')            #get gian character info from .env file
Suneo = os.getenv('SUNEO')          #get suneo character info from .env file

#function to convert character name to story
def NameToStory(char_name):
    if char_name == 'Nobita':
        return Nobita
    elif char_name == 'Doremon':
        return Doremon
    elif char_name == 'Shizuka':
        return Shizuka
    elif char_name == 'Gian':
        return Gian
    elif char_name == 'Suneo':
        return Suneo

#gemni ai function
def ai(ai_input,char_name="Nobita"):
        load_dotenv()                       #load .env file
        api_key = os.getenv('API_TOKEN')    #get api token from .env file
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model_name='gemini-pro')
        story=NameToStory(char_name)
        pre_prompt = "your character is: \""+ story + "\" and qution is: \"" + ai_input + "\""
        output = model.generate_content(pre_prompt,generation_config={'temperature': 0,'max_output_tokens': 800} )
        ai_output = output.text

        return ai_output

#main function
def main():
    st.header("Talk to your favourite character")
    st.sidebar.title("Navigation")
    char_name = st.sidebar.selectbox("Select a character", options=['Nobita', 'Doremon', 'Shizuka', 'Gian', 'Suneo'])
    ai_input = st.chat_input("Enter your question")
    #print(api_key)
    if ai_input is not None:
        st.write("You : "+ ai_input)
        st.write(str(char_name+" : "+ai(ai_input,char_name)))
    


#main function call
main()