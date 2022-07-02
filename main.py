import pickle
import streamlit as st
from PIL import Image

loaded_model = pickle.load(open('moviemodel.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

#print(movies.head())

# finding the close match for the movie name given by the user
def recommend (movie_name,similarity,movie_list):
    movie_name = movie_name.lower()
    if movie_name in movie_list:
        index = list(movie_list).index(movie_name)
        
    similarity = list(enumerate(similarity[index]))
    sorted_similar_movies = sorted(similarity, key = lambda x:x[1], reverse = True) 

    recommended_movie_names = []
    for i in sorted_similar_movies[1:11]:
        recommended_movie_names.append(list(movie_list)[i[0]])
    return recommended_movie_names
             

img1 = Image.open('geu.png')
img1 = img1.resize((650,145))
st.image(img1,use_column_width=False)
st.header('Movie Recommendation System')


#selected_movie = st.text_input('Enter movie name')
movie_list = loaded_model['title'].values()
selected_movie = st.selectbox(
   "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names = recommend(selected_movie,similarity=similarity,movie_list=movie_list)
    row1,row2=st.columns([5,1])
    with row1:
        st.text(recommended_movie_names[0])
        #st.text('hello')
        st.text(recommended_movie_names[1])
        st.text(recommended_movie_names[2])
        st.text(recommended_movie_names[3])
        st.text(recommended_movie_names[4])
        st.text(recommended_movie_names[5])
        st.text(recommended_movie_names[6])
        st.text(recommended_movie_names[7])
        st.text(recommended_movie_names[8])
        st.text(recommended_movie_names[9])

        
