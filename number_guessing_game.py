import streamlit as st
import random

# Set page config
st.set_page_config(
    page_title="Number Guessing Game",
    page_icon="🎲",
    layout="centered"
)

# Add custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        width: 100%;
        margin: 5px 0;
        padding: 10px;
        border-radius: 5px;
        background-color: #4CAF50;
        color: white;
        border: none;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stTextInput>div>div>input {
        background-color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and description
st.title("🎲 Number Guessing Game")
st.markdown("### Can you guess the number I'm thinking of?")

# Initialize session state
if 'target_number' not in st.session_state:
    st.session_state.target_number = random.randint(1, 100)
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'game_over' not in st.session_state:
    st.session_state.game_over = False
if 'guesses' not in st.session_state:
    st.session_state.guesses = []

# Game settings
st.sidebar.title("Game Settings")
difficulty = st.sidebar.selectbox(
    "Select Difficulty",
    ["Easy (1-50)", "Medium (1-100)", "Hard (1-200)"]
)

# Update target number based on difficulty
if difficulty == "Easy (1-50)":
    max_number = 50
elif difficulty == "Medium (1-100)":
    max_number = 100
else:
    max_number = 200

# Main game interface
st.markdown(f"### I'm thinking of a number between 1 and {max_number}")

# Input for player's guess
player_guess = st.number_input(
    "Enter your guess:",
    min_value=1,
    max_value=max_number,
    value=1,
    step=1
)

# Play button
if st.button("Make Guess!"):
    st.session_state.attempts += 1
    
    # Add guess to history
    st.session_state.guesses.append(player_guess)
    
    # Check the guess
    if player_guess == st.session_state.target_number:
        st.session_state.game_over = True
        st.balloons()
        st.success(f"🎉 Congratulations! You found the number in {st.session_state.attempts} attempts!")
    elif player_guess < st.session_state.target_number:
        st.warning("Too low! Try a higher number.")
    else:
        st.warning("Too high! Try a lower number.")
    
    # Display guess history
    st.markdown("### Your Guesses:")
    for i, guess in enumerate(st.session_state.guesses, 1):
        if guess == st.session_state.target_number:
            st.markdown(f"Guess {i}: {guess} ✅")
        else:
            st.markdown(f"Guess {i}: {guess} {'⬆️' if guess > st.session_state.target_number else '⬇️'}")

# New game button
if st.button("New Game"):
    st.session_state.target_number = random.randint(1, max_number)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.session_state.guesses = []
    st.experimental_rerun()

# Display attempts
st.markdown(f"### Attempts: {st.session_state.attempts}")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit") 