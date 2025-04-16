import requests
import streamlit as st



st.set_page_config(page_title="NuveAssist", page_icon=":rocket:")


st.title("NuveAssist")
st.markdown("An AI assistant from the Engineering team to help you with your queries.")
query = st.text_input("Ask a question to our Engineering Bot:")

if query:
    st.write("⏳ Waiting for response...")
    try:
        print(f"Sending query: {query}")
        response = requests.post("http://localhost:8000/ask", json={"question": query})
        print(f"Received response: {response.status_code}")

        if response.status_code == 200:
            result = response.json()
            answer = result.get("answer") or result.get("error", "No answer returned")
            st.write("💬 Answer:", answer)
        else:
            st.error(f"Request failed with status: {response.status_code}")
    except Exception as e:
        print(f"Exception occurred: {e}")
        st.error("Error communicating with backend.")
