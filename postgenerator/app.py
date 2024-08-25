# app.py
import streamlit as st
from gpt import generate_post

def main():
    st.title("Social Media Post Generator")
    
    # Sidebar for API Key Input
    st.sidebar.title("Configuration")
    api_key = st.sidebar.text_input("Enter your OpenAI API key:", type="password")
    
    if api_key:
        # User Inputs for post generation
        topic = st.text_input("What is your post for?")

        platform = st.selectbox("Platform:", ["Facebook", "Instagram", "Twitter", "LinkedIn"])
        
        # Temperature slider to control the creativity of the post
        temperature = st.slider("Creativity Level (temperature):", min_value=0.0, max_value=1.0, value=0.5, step=0.1)
        
        length = st.selectbox("Choose the length:", ["Short", "Medium", "Long"])
        
        use_hashtags = st.radio("Include hashtags?", ("Yes", "No"))
        use_emojis = st.radio("Include emojis?", ("Yes", "No"))
        
        # Convert radio button input to boolean
        use_hashtags = use_hashtags == "Yes"
        use_emojis = use_emojis == "Yes"
        
        # Generate Post Button
        if st.button("Generate Post"):
            if topic:
                post = generate_post(api_key, platform, topic, temperature, length, use_hashtags, use_emojis)
                st.success("Generated Post:")
                st.write(post)
            else:
                st.warning("Please enter a topic!")
    else:
        st.warning("Please enter your OpenAI API key in the sidebar to generate a post.")

if __name__ == "__main__":
    main()
