import streamlit as st
import function

todos = function.get_todos()

def add_todo():
    todo = st.session_state["add"] + "\n"
    function.write_todos(todo)

st.title("My Todo App")
st.subheader("hi")
st.write("hello")

for index, i in enumerate(todos):
    checkbox = st.checkbox(i, key=i)
    if checkbox:
        function.delete_todo(i)
        del st.session_state[i]
        st.rerun()

st.text_input(label='', placeholder="Add todo...",
              on_change=add_todo, key="add")
