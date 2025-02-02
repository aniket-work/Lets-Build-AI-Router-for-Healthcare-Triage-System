import streamlit as st
import json
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from utils import load_settings, get_formatted_datetime
from ai_router import decide_model_from_prompt, prompt_ai
from constants import UI


def initialize_session():
    """Initialize the session state and system message"""
    settings = load_settings()

    if "messages" not in st.session_state:
        system_message = settings['prompts']['system_message']
        system_message += f"\nCurrent date and time: {get_formatted_datetime(settings['timezone'])}"
        st.session_state.messages = [SystemMessage(content=system_message)]


def display_chat_history():
    """Display the chat message history"""
    for message in st.session_state.messages:
        message_json = json.loads(message.model_dump_json())
        message_type = message_json["type"]
        if message_type in ["human", "ai", "system"]:
            with st.chat_message(message_type):
                st.markdown(message_json["content"])


def main():
    """Main application function"""
    st.title(UI.TITLE)

    # Initialize session
    initialize_session()

    # Display chat history
    display_chat_history()

    # Show disclaimer
    st.sidebar.warning(UI.DISCLAIMER)

    # Handle user input
    if prompt := st.chat_input("Please describe your medical concern or request"):
        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append(HumanMessage(content=prompt))

        with st.chat_message("assistant"):
            # Determine which model to use
            model_choice = decide_model_from_prompt(st.session_state.messages)

            # Show debug info in development
            if os.getenv('ENVIRONMENT') == 'development':
                with st.expander("Debug Info"):
                    st.write(f"Using model: {'Ollama' if model_choice.lower() == 'cheap' else 'Groq'}")

            # Process the response
            response_text = ""
            for chunk in prompt_ai(st.session_state.messages, model_choice):
                response_text += str(chunk)
                st.write(chunk)

            # Save the assistant's response
            st.session_state.messages.append(AIMessage(content=response_text))


if __name__ == "__main__":
    main()