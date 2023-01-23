import pandas as pd
import numpy as np
import streamlit as st

@st.cache(show_spinner = False)
def read_data():
    df = pd.read_csv('dataset/zomato_cleaned.csv')
    return df

@st.cache(show_spinner = False)
def rank_restaurants(df = read_data()):
    
    # ranking restaurants
    C = np.mean(df['rating'])
    m = df['votes'].quantile(0.90)
    q_restaurants = df.copy().loc[df['votes'] >= m]

    @st.cache(show_spinner = False)
    def weighted_rating(x, m = m, C = C):
        v = x['votes']
        R = x['rating']
        return (v/(v+m) * R) + (m/(m+v) * C)

    q_restaurants['score'] = q_restaurants.apply(weighted_rating, axis = 1)
    highest_rated_restaurants = q_restaurants.sort_values('score', ascending = False).head(50).name.values

    seen = {}
    unique_restaurants = []

    for r in highest_rated_restaurants:
        name = r.split(',')[0]
        if name not in seen:
            seen[name] = r
            unique_restaurants.append(r)

    # Convert to numpy array
    return unique_restaurants[:10]

@st.cache(show_spinner = False)
def get_highest_rated_restaurants():
    restau = ['Byg Brewski Brewing Company, Sarjapur Road', "AB's - Absolute Barbecues, Koramangala 7th Block", 'The Black Pearl, Marathahalli', "Chili's American Grill & Bar, Rajajinagar", 'Flechazo, Whitefield', 'The Boozy Griffin, Marathahalli', 'House Of Commons, Koramangala 4th Block', 'CTR, Rajajinagar', 'Toit, Indiranagar', 'Truffles, Koramangala 7th Block']
    low_restau = ['CTR, Rajajinagar', "Brahmin's Coffee Bar, Basavanagudi", 'O.G. Variar & Sons, Rajajinagar', 'Taaza Thindi, Banashankari', 'Natural Ice Cream, Old Airport Road', 'Mavalli Tiffin Room (MTR), Basavanagudi', 'Veena Stores, Rajajinagar', 'Vidyarthi Bhavan, Banashankari', 'Hari Super Sandwich, Jayanagar', 'Ayodhya Upachar, Banashankari']

    return restau, low_restau