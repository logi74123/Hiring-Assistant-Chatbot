import os
import json
import streamlit as st
from groq import Groq
import csv


#Finding and storing the file location
working_dir = os.path.dirname(os.path.abspath(__file__))
#Loading the JSON file using json library
config_data = json.load(open(f"{working_dir}/config.json"))

#Setting the API Key for the groq
client = Groq(api_key=config_data["API_KEY"])

#All the datas(by both user and assistant) gets stored in this variable 
collected_data = ''

# Configuring streamlit page settings
st.set_page_config(
    page_title="TalentScout",
    page_icon="🤖",
    layout="centered" 
)

# Initializing chat session in streamlit if not already present
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

#Styling the title
st.markdown('''<h2 style='
            text-align:center;
            background: linear-gradient(90deg, #FC466B 0%, #3F5EFB 100%);
            font-size: 50px;
            -webkit-background-clip:text;
            color:transparent;
            display: inline-block';
            >TalentScout</h2>''',
                unsafe_allow_html=True)

#Displaying all the recent content inside the chatbot, given by both user and assistant
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])  

#If the prompt by the user is active 
if prompt := st.chat_input("Type a message..."):

    st.chat_message("user").markdown(prompt)
    st.session_state.chat_history.append({"role": "user", "content": prompt})

    # send uesr's message to GPT-40 and get a response
    response = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[
            {
                "role": "system",

                "content":  "You are an intelligent hiring assistant working for a recruitment agency specializing in technology placements. Keep your content short and simple. If you found any messages to be unrelated to your context, provide meaningful responses such that you are not deviating from your purpose. The information to be gathered from the user includes: 1.Full Name 2.Email Address 3.Phone Number 4.Years of Experience 5.Desired Positions 6.Current Location 7.Tech Stack(including programming languages, frameworks, databases) one by one. After that, generate a total of 3-5 technical questions tailored to assess the candidates proficiency in the mentioned tech stack. Deliver the messages based on the language preferred by the user. If the candidate wants to end the conversation, gracefully conclude the conversation informing them about the next steps."},
             *st.session_state.chat_history
        ]
    )
    
    #Storing and appending the recent data to the chat_history 
    assistant_response = response.choices[0].message.content           
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

    #displaying the recent content by the assistant inside the chatbot
    with st.chat_message("assistant"):
        st.write(assistant_response)

    #Storing all the datas in the collected_data which can the be used to stored in the csv file  
    temp_str = assistant_response
    collected_data += (temp_str)
        

    #Overwriting the csv file evertime the app is refreshed. The csv file is stored in local.
    with open('output.csv', 'w', newline='', encoding="utf-8") as file:
        fieldnames = ['role', 'content']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(st.session_state.chat_history)
