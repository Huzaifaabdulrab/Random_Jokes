import streamlit as st
import requests


def random_jokes():
    """Fetch Random Joke From The Api"""
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")

        if response.status_code == 200:
            joke_data = response.json()
            return f"{joke_data['setup']} \n \n {joke_data['punchline']}"
        else:
            return "Feild to fetch a joke please try again latter"
    except:
        return "You are not programmer😂😂😂 _____________ "

def main():
    st.title("Random Joke Generator")
    st.subheader("Click the button below to generate a random joke")

    if st.button("Generate Joke"):
        joke = random_jokes()
        st.success(joke)
    
    st.divider()

    st.markdown(
        """
    <div style='text-align:center;'>
        <p>Joke from Official Joke API</p>
        <p>Build with ❤️ by <a style="color:green ; text-decoration:none;" href='https://github.com/HuzaifaAbdulrab'><span>Huzaifa Abdulrab</span></a> using Streamlit</p>
    </div>
""", 
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()