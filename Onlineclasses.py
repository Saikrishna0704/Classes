import streamlit as st
import time
def main():
    st.sidebar.image("https://play-lh.googleusercontent.com/r1CHZYUHjyTu2iwFhsYb1q5DLD2zmA1nQJssbSNKYAtvJOlEG_-kO4VTjyraLIIs8g", use_column_width=True)
    st.sidebar.write("Online Classes")
    st.title("Magnet Brains")
    name = st.text_input("Enter your name:")
    class_name = st.text_input("Enter your class:")
    subject = st.text_input("Enter the subject:")
    if subject:
          with st.spinner("Loading..."):
            time.sleep(2)
            st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR4F9lch1Lq12oVIdwdV6gDZBlph-maWw6kFK7mZvffI06GBuMVxQE9faROTw&s")
            st.markdown("<h1 style='text-align: center; color: blue;'>Large Text</h1>", unsafe_allow_html=True)
            st.write("Eddie Kareakka C batch bugga")
if __name__ == "__main__":
    main()

