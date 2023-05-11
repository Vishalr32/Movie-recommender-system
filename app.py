import streamlit as st
import pickle
import requests
import numpy as np
from PIL import Image
import pandas as pd


image = Image.open('mr.png')
st.image(image,width=360)

def fetch_poster(id):
    response =requests.get('https://api.themoviedb.org/3/movie/{}?api_key=a7aace4eeba2c626f8d1cbd8164880b9&language=en-US'.format(id))
    data = response.json()
    return "https://image.tmdb.org/t/p/original/"+data['poster_path']


def recommend(movie):
    movie_index = movies[movies ['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:11]
    
    recommended_movies = [ ]
    recommended_movies_poster = [ ]
    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        #print(movie_id)
        recommended_movies.append(movies.iloc[i[0]].title)
         # fetch poster from API
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster

movies_dict = pickle.load(open('movies_dict.pkl','rb')) 
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb')) 


st.title('Movie Recommendation System')

selected_movie_name = st.selectbox(
    'Enter your Favourite movie to get most similiar recommendations ',
    movies['title'].values)

if st.button('RECOMMEND'):
    names,posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    



    with col1:
        st.markdown(names[0])
        st.image(posters[0])

    with col2:
        st.markdown(names[1])
        st.image(posters[1])

    with col3:
        st.markdown(names[2])
        st.image(posters[2])

    with col4:
        st.markdown(names[3])
        st.image(posters[3])

    with col5:
        st.markdown(names[4])
        st.image(posters[4])

    
    with st.container():
        st.write(" ")

        col6, col7, col8, col9, col10 = st.columns(5)

        with col6:
            st.markdown(names[5])
            st.image(posters[5])

        with col7:
            st.markdown(names[6])
            st.image(posters[6])

        with col8:
            st.markdown(names[7])
            st.image(posters[7])

        with col9:
            st.markdown(names[8])
            st.image(posters[8])

        with col10:
            st.markdown(names[9])
            st.image(posters[9])

    st.subheader("Here is your Top 10 recommended movies")

