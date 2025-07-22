
# Hiring Assistant ChatBot

An hiring assistant chatbot that assists in the initial screening of candidates by gathering essential information and posing relevant technical questions based on the candidate's declared tech stack.

## Project Overview

1. Gather Initial Candidate Information: Collecting essential details such as name, contact information, years of experience, and desired positions. 

2. Generate Technical Questions: Based on the candidate’s specified tech stack *(e.g. programming languages, frameworks, tools),* generating relevant technical questions to assess their proficiency.

## Installation Instructions

#### Install the following libraries

    1. streamlit
    2. groq

Just download the repository and install the libraries altogether from **requirements.txt** file which can be done with the following command.
```http
pip install -r requirements.txt
```
* #### API Reference

   *Note:* Input your groq API Key in **config.json** before running the program.


## Technical Details

#### Streamlit: 
   An open-source Python library that makes it easy to create and share custom web apps for machine learning and data science. I've chosen Streamlit for this project, because I found it more appropriate to integrate the ChatBot feature in this app as it is already inbuilt with it.

#### Groq:

   It is an inference for LLM models. Its API is a free-to-use tool. The model used includes meta-llama's **llama-4-scout-17b-16e-instruct**    


## Prompt Design

* #### Persona:
   Assigning a **role.** 

   You are an intelligent hiring assistant working for a recruitment agency specializing in technology placements.

* #### Requirements:
   Defining the **parameters** for output.   

   Keep your content short and simple.

* #### Organization:
   Describing the **structure** of output.    

   Deliver the messages based on the language preferred by the user. Gather informations like Full Name, Email Address, Phone Number, Years of Experience, Desired Positions, Current Location and Tech Stacks. Then generate total of 3-5 technical questions to assess the candidates proficiency in the stacks mentioned. 

* #### Purpose:
   Identify the **rhetorical purpose**

   If you found any messages to be unrelated to your context, provide meaningful responses such that you are not deviating from your purpose.

* #### Tone: 
  Specifying the **tone** of output 

  If the candidate wants to end the conversation, gracefully conlude the conversation informing them about the next steps.

## Challenges & Solutions        

   Initially, I encountered some obstacles in getting the LLM API key for free. Later, I came across Groq, an inference tool for LLM models, which provides free API keys and chose it.

   Storing the collected data into a csv file is somewhere I faced difficulty in. Later, the solution I came with was overwriting the csv file in locally each time the user raises the prompt.  


  * #### Expanding the scope:   
     1. *Voice-enabled Search:* Integration of voice-enabled search with Speech to text and Text to Speech features can make it more user-friendly.
     2. *Storing details in cloud:* Storing of details automatically in the cloud can reduce consuming local storage.


## UI Appearance

<img src="https://yourimageshare.com/ib/flBHwi1sU0.png" width=600 height=300>
