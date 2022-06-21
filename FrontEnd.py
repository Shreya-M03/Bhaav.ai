import streamlit as st
from streamlit_option_menu import option_menu
from predictions77 import predictions
from translation import translator

import nltk
import pickle
import pandas as pd
from nltk.corpus import stopwords
from textblob import Word
from collections import Counter
from keras.models import Sequential
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from tensorflow.keras import models


#Navigation Bar
selected = option_menu(
            menu_title="Bhaav", 
            options=[" "],  # required
            menu_icon="twitch",  # optional
            default_index=0,  # optional
            orientation="horizontal",

            styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                "icon": {"color": "black", "font-size": "18px"},
                "nav-link": {
                    "font-size": "18px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "black"},
            },
        )

st.title("Bhaav: A Multilingual Sentiment Analyzer for Indian Languages")
st.write("At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est")
st.header('Analyzer')
lang = st.selectbox("Enter Language",options=['Hindi','English','Bengali', 'Gujarati','Malayalam','Marathi','Tamil','Telugu','Urdu'])
input_text = st.text_input("Enter text",placeholder="Enter text")

if st.button('Analyze Now'):
    if lang != 'English':
        translated_text = translator(input_text,lang)
    else:
        translated_text = input_text
    results = predictions(translated_text)
    sentiment = results[0]
    positive = results[1]
    negative = results[2]
    st.text_area('Translated Text (En):',translated_text) 
    st.text_area('Your Bhaav, unfiltered ;)',sentiment)
    col1, col2 = st.columns(2)
    col1.metric("Sentiment", "Positive", str(round(positive*100,6))+"%")
    col2.metric("Sentiment", "Negative", str(round(negative* -100,6))+"%")

