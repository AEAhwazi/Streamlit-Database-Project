import streamlit as st
import sqlite3
import app_db as app_db

DBNAME = 'MoviesData.db'

st.title("STREAMLIT DATABASE UI")

option = st.sidebar.selectbox('Select Your Option:',
                                ('View All Records',
                                 'Insert New Record',
                                 'Update Record By ID',
                                 'Update Record By Title',
                                 'Delete Record By ID',
                                 'Delete Record By Title'))
#=================================================

if option == 'View All Records':
    if st.button('Show Data'):
        result = app_db.select_all_record()
        st.table(result)
        
#=================================================

if option == 'Insert New Record':
    st.success("Enter new record:")

    cols = st.columns(2)
    with cols[0]:
        movie_id = st.number_input("Movie id: ", value=None, step=1, width=100)

    with cols[1]:
        title = st.text_input("Title: ")

    cols = st.columns(3)
    with cols[0]:
        year = st.number_input("Year: ", value=None, step=1, width=100)

    with cols[1]:
        country = st.text_input("Country: ", width=200)

    with cols[2]:
        imdb_rating = st.number_input("Imdb_rating: ", value=None, width=100)

    my_select = st.button('Save Record!')
    if my_select:
        result = app_db.insert_record(movie_id, title, year, country, imdb_rating)

        st.success("Record Saved!")
#=================================================

if option == 'Update Record By ID':
    st.success("Enter id to update record:")

    cols = st.columns(3)
    with cols[0]:
        old_movie_id = st.number_input("Old movie id: ", value=None, step=1, width=100)

    with cols[1]:
        new_movie_id = st.number_input("New movie id: ", value=None, step=1, width=100)

    with cols[2]:
       title = st.text_input("Title: ")

    cols = st.columns(3)
    with cols[0]:
        year = st.number_input("Year: ", value=None, width=100)

    with cols[1]:
        country = st.text_input("Country: ", width=200)

    with cols[2]:
        imdb_rating = st.number_input("Imdb_rating: ", value=None, width=100)

    my_select = st.button('Update Record!')
    if my_select:
        result = app_db.update_record_by_id(old_movie_id, new_movie_id, title, year, country, imdb_rating)

        if result:
            st.success("Record Updated!")

        else:
            st.success("Record Not Found!")        
#=================================================

if option == 'Update Record By Title':
    st.success("Enter title to update record:")

    cols = st.columns(3)
    with cols[0]:
        movie_id = st.number_input("Movie id: ", value=None, step=1, width=100)

    with cols[1]:
        old_title = st.text_input("Old title: ", value=None, width=100)

    with cols[2]:
        new_title = st.text_input("New Title: ")

    cols = st.columns(3)
    with cols[0]:
        year = st.number_input("Year: ", value=None, width=100)

    with cols[1]:
        country = st.text_input("Country: ", width=200)

    with cols[2]:
        imdb_rating = st.number_input("Imdb_rating: ", value=None, width=100)

    my_select = st.button('Update Record!')
    if my_select:
        result = app_db.update_record_by_title(movie_id, old_title, new_title, year, country, imdb_rating)

        if result:
            st.success("Record Updated!")

        else:
            st.success("Record Not Found!")

#=================================================

if option == 'Delete Record By ID':
    movie_id = st.number_input("Enter movie id for delete:", value=None ,step=1 ,min_value=1)

    if st.button("Delete Record?"):
        result = app_db.delete_record_by_id(movie_id)
        if result:
            st.success("Record Deleted!")

        else:
            st.success("Record Not Found!")

#=================================================

if option == 'Delete Record By Title':
    title = st.text_input("Enter title movie for delete:")

    if st.button("Delete Record?"):
        result = app_db.delete_record_by_title(title)
        if result:
            st.success("Record Deleted!")

        else:
            st.success("Record Not Found!")

#=================================================


#END PROGRAM.