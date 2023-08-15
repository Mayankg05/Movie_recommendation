import pickle
import streamlit
import requests



streamlit.header('Movie Recommender System Using Machine Learning')
movies = pickle.load(open('artificates/movie_list.pkl','rb'))
similarity = pickle.load(open('artificates/similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = streamlit.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)




