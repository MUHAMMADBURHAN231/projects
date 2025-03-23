import streamlit as st
import random

# Set page config
st.set_page_config(
    page_title="Hangman Game",
    page_icon="🎮",
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
    .word-display {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        border: 2px solid #ddd;
        margin: 20px 0;
        text-align: center;
        font-family: monospace;
        font-size: 24px;
        letter-spacing: 5px;
    }
    .hangman-display {
        text-align: center;
        font-family: monospace;
        white-space: pre;
        margin: 20px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Word categories and their words
WORDS = {
    "Animals": ["elephant", "giraffe", "penguin", "kangaroo", "dolphin", "lion", "tiger", "zebra"],
    "Countries": ["france", "japan", "australia", "brazil", "egypt", "india", "canada", "mexico"],
    "Food": ["pizza", "sushi", "chocolate", "sandwich", "icecream", "hamburger", "pancake", "spaghetti"],
    "Sports": ["football", "basketball", "tennis", "volleyball", "cricket", "hockey", "rugby", "baseball"]
}

# Hangman ASCII art
HANGMAN_STATES = [
    '''
       -----
       |   |
           |
           |
           |
           |
    =========''',
    '''
       -----
       |   |
       O   |
           |
           |
           |
    =========''',
    '''
       -----
       |   |
       O   |
       |   |
           |
           |
    =========''',
    '''
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========''',
    '''
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========''',
    '''
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========''',
    '''
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    ========='''
]

# Initialize session state
if 'word' not in st.session_state:
    st.session_state.word = ""
if 'guessed_letters' not in st.session_state:
    st.session_state.guessed_letters = set()
if 'wrong_guesses' not in st.session_state:
    st.session_state.wrong_guesses = 0
if 'game_over' not in st.session_state:
    st.session_state.game_over = False
if 'category' not in st.session_state:
    st.session_state.category = ""

# Title and description
st.title("🎮 Hangman Game")
st.markdown("### Try to guess the word before the hangman is complete!")

# Category selection
if not st.session_state.category:
    st.session_state.category = st.selectbox("Select a category:", list(WORDS.keys()))
    st.session_state.word = random.choice(WORDS[st.session_state.category])
    st.session_state.guessed_letters = set()
    st.session_state.wrong_guesses = 0
    st.session_state.game_over = False

# Display category
st.markdown(f"**Category:** {st.session_state.category}")

# Display hangman
st.markdown('<div class="hangman-display">' + HANGMAN_STATES[st.session_state.wrong_guesses] + '</div>', unsafe_allow_html=True)

# Display word with guessed letters
display_word = ""
for letter in st.session_state.word:
    if letter in st.session_state.guessed_letters:
        display_word += letter + " "
    else:
        display_word += "_ "
st.markdown('<div class="word-display">' + display_word.strip() + '</div>', unsafe_allow_html=True)

# Display guessed letters
st.markdown("**Guessed Letters:** " + ", ".join(sorted(st.session_state.guessed_letters)) if st.session_state.guessed_letters else "**Guessed Letters:** None")

# Game logic
if not st.session_state.game_over:
    # Letter input
    guess = st.text_input("Enter a letter:", max_chars=1).lower()
    
    if guess and guess.isalpha():
        if guess in st.session_state.guessed_letters:
            st.warning("You've already guessed that letter!")
        else:
            st.session_state.guessed_letters.add(guess)
            if guess not in st.session_state.word:
                st.session_state.wrong_guesses += 1
                st.error("Wrong guess!")
            else:
                st.success("Correct guess!")
            
            # Check if game is over
            if st.session_state.wrong_guesses >= 6:
                st.session_state.game_over = True
                st.error("Game Over! You lost!")
            elif all(letter in st.session_state.guessed_letters for letter in st.session_state.word):
                st.session_state.game_over = True
                st.success("Congratulations! You won!")
    
    # Display remaining guesses
    st.markdown(f"**Remaining Guesses:** {6 - st.session_state.wrong_guesses}")

# New game button
if st.button("New Game"):
    st.session_state.category = ""
    st.experimental_rerun()

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit") 