import csv
import pickle
from pathlib import Path

import altair as alt
import pandas as pd
import streamlit as st
from textblob import TextBlob
import tweepy
import config
from datetime import datetime

def main():
            st.title("Crawling Twitter")
            st.subheader("Streamlit Projects")

            menu = ["Home","About"]
            choice = st.sidebar.selectbox("Menu",menu)
            if choice == "Home":
                BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAOZijgEAAAAAGbnHwM5lcGyXxFj9WTxwYS%2BeGxw%3DnizRHL0Ajz8pPrVZ47sXKAxBJYFgUoO4AorzdxwCaYWtawrIN5'

                with st.form ("text yang dicari"): 
                    query = st.text_area("Masukan keyword")
                    tweet_count = st.text_input("Masukan jumlah tweet: ", 10,100)

                    submit_button2 = st.form_submit_button (label='Cari')
                    if submit_button2:
                        # Masukkan Twitter Token API
                        client = tweepy.Client(bearer_token=BEARER_TOKEN)
                        # Query pencarian
                        hasil = client.search_recent_tweets(query=query, max_results=tweet_count, tweet_fields=['created_at', 'lang'], expansions= ['author_id'])
                        users = {u['id']: u for u in hasil.includes['users']}
                        i = []
                        u = []
                        t = []
                        c = []
                    

                        #menambahkan tweet ke array
                        for tweet in hasil.data:
                            user = users[tweet.author_id]
                            clock = datetime.strftime(tweet.created_at, '%d/%m/%y %H:%M:%S')
                            i.append(tweet.id)
                            u.append(user.username)
                            t.append(tweet.text)
                            c.append(clock)

          
                        #menampilkan ke dataframe
                        dictTweets = {"id":i,"username":u, "text":t, "time":c}
                        df = pd.DataFrame(dictTweets,columns=["id", "username", "text", "time"])
                        df
                    
            else:
                st.subheader("About")

if __name__ == '__main__':
    main()


