import streamlit as st

def main():
    st.set_page_config(layout="wide")
    st.title("About Us")
    
    # Create a layout with two columns for the About Us section
    col1, col2 = st.columns(2)
    
    # Information about the 3rd year AIML student
    with col1:
        st.subheader("Team Leader")
        col3, col4 = st.columns(2)
        with col3:
            st.image("najeeb1.jpg", caption="Najeeb Fariduddin Saiyed",width=200, use_column_width=True)
        with col4:
            st.write("Hi there! I'm a 3rd year engineering student specializing in Artificial Intelligence and Machine Learning. With a passion for data analysis and AI-driven solutions, I contribute to our platform's advanced technology.")
    
    # Information about the 1st year student
    with col2:
        st.subheader("Team Member")
        col5, col6 = st.columns(2)
        with col5:
            
            st.image("k1.jpg", caption="Karthik Reddy", use_column_width=True)
            
        with col6:
            st.write("Greetings! I'm a 1st year engineering student eager to learn and innovate. While I'm just beginning my journey, I bring fresh perspectives and a willingness to contribute to our platform's growth.")
        
if __name__ == "__main__":
    main()

st.sidebar.markdown('''
Created with 💜 by [Najeeb](https://www.instagram.com/thiscloudbook/) And [Karthik](https://www.instagram.com/_mr_thop/).
''')

