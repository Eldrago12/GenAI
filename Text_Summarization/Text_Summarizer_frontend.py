import streamlit as st
import requests

def summarize_text(text):
    endpoint = 'MODEL_ENDPOINT'
    payload = {'text': text}
    response = requests.post(endpoint, json=payload)
    
    return response.json()['summary']

# Streamlit App
def main():
    st.title("Text Summarization App")
    st.write("Enter text to summarize:")

    input_text = st.text_area("Input Text", "")

    if st.button("Summarize"):
        if input_text:
            summary = summarize_text(input_text)
            st.subheader("Summary:")
            st.write(summary)
        else:
            st.warning("Please enter some text.")

if __name__ == "__main__":
    main()
