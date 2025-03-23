import streamlit as st
import random

# Set page config
st.set_page_config(
    page_title="Rock Paper Scissors",
    page_icon="✂️",
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
    </style>
    """, unsafe_allow_html=True)

# Title and description
st.title("🎮 Rock Paper Scissors")
st.markdown("### Choose your weapon and challenge the computer!")

# Initialize session state for score
if 'score' not in st.session_state:
    st.session_state.score = {'player': 0, 'computer': 0}

# Game options
options = ['Rock', 'Paper', 'Scissors']

# Create columns for the game interface
col1, col2 = st.columns(2)

with col1:
    st.subheader("Your Choice")
    player_choice = st.selectbox("Select your weapon:", options)

with col2:
    st.subheader("Computer's Choice")
    computer_choice = random.choice(options)
    st.write(f"Computer chose: {computer_choice}")

# Game logic
def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == 'Rock' and computer == 'Scissors') or \
         (player == 'Paper' and computer == 'Rock') or \
         (player == 'Scissors' and computer == 'Paper'):
        st.session_state.score['player'] += 1
        return "You win! 🎉"
    else:
        st.session_state.score['computer'] += 1
        return "Computer wins! 😢"

# Play button
if st.button("Play!"):
    result = determine_winner(player_choice, computer_choice)
    st.markdown(f"### {result}")
    
    # Display score
    st.markdown("### Score")
    st.markdown(f"""
    - You: {st.session_state.score['player']} 
    - Computer: {st.session_state.score['computer']}
    """)

# Add a reset button
if st.button("Reset Score"):
    st.session_state.score = {'player': 0, 'computer': 0}
    st.experimental_rerun()

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit") 