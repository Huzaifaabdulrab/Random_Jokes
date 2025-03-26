import streamlit as st
import requests


def random_jokes():
    """Fetch a random joke from the API"""
    try:
        # Attempt to fetch a random joke from the API
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        
        # If the response status is 200, extract joke data
        if response.status_code == 200:
            joke_data = response.json()
            return f"{joke_data['setup']} \n \n {joke_data['punchline']}"
        else:
            return "Failed to fetch a joke, please try again later."
    except:
        # If the API call fails, display this message
        return "You are not a programmer 😂😂😂 _____________ "


def main():
    """Main function for the Streamlit app"""
    st.title("Random Joke Generator")  # Set the app title
    st.subheader("Click the button below to generate a random joke")  # Show a subheading

    if st.button("Generate Joke"):  # If the button is clicked
        joke = random_jokes()  # Fetch a joke
        st.success(joke)  # Display the joke


if __name__ == "__main__":
    main()  # Run the app

