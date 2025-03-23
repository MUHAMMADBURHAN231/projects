import streamlit as st
import random

# Set page config
st.set_page_config(
    page_title="Mad Libs Game",
    page_icon="📚",
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
    .story-box {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        border: 2px solid #ddd;
        margin: 20px 0;
        font-size: 18px;
        line-height: 1.6;
    }
    </style>
    """, unsafe_allow_html=True)

# Story templates
STORIES = {
    "The Silly Zoo": {
        "template": "Yesterday, I went to the zoo with my {adjective} {noun}. We saw a {adjective} {animal} {verb}ing in its cage. The zookeeper was {verb}ing {adverb} while feeding the {animal}. Suddenly, a {adjective} {animal} started {verb}ing {adverb} and made everyone {verb}! It was a {adjective} day at the zoo!",
        "blanks": ["adjective", "noun", "adjective", "animal", "verb", "verb", "adverb", "animal", "adjective", "animal", "verb", "adverb", "verb", "adjective"]
    },
    "The Crazy Restaurant": {
        "template": "Last night, I went to a {adjective} restaurant called '{noun}'. The waiter was {verb}ing {adverb} while taking our order. I ordered a {adjective} {food} with {adjective} {food} on the side. The chef was {verb}ing {adverb} in the kitchen. When the food arrived, it was {adjective} and tasted {adverb} {adjective}!",
        "blanks": ["adjective", "noun", "verb", "adverb", "adjective", "food", "adjective", "food", "verb", "adverb", "adjective", "adverb", "adjective"]
    },
    "The Magical Adventure": {
        "template": "In a {adjective} land far away, there lived a {adjective} {noun} who loved to {verb}. One day, while {verb}ing {adverb}, they found a {adjective} {noun}. The {noun} was {verb}ing {adverb} and glowing with {adjective} light. Suddenly, a {adjective} {noun} appeared and said, '{exclamation}! You have found the {adjective} {noun}!'",
        "blanks": ["adjective", "adjective", "noun", "verb", "verb", "adverb", "adjective", "noun", "noun", "verb", "adverb", "adjective", "adjective", "noun", "exclamation", "adjective", "noun"]
    }
}

# Word type descriptions
WORD_TYPES = {
    "noun": "a person, place, thing, or idea",
    "verb": "an action word",
    "adjective": "a word that describes a noun",
    "adverb": "a word that describes a verb",
    "exclamation": "a word that shows strong emotion",
    "food": "a type of food or drink",
    "animal": "a type of animal"
}

# Initialize session state
if 'story_name' not in st.session_state:
    st.session_state.story_name = ""
if 'user_inputs' not in st.session_state:
    st.session_state.user_inputs = {}
if 'story_completed' not in st.session_state:
    st.session_state.story_completed = False

# Title and description
st.title("📚 Mad Libs Game")
st.markdown("### Fill in the blanks to create your own funny story!")

# Story selection
if not st.session_state.story_name:
    st.session_state.story_name = st.selectbox("Select a story:", list(STORIES.keys()))
    st.session_state.user_inputs = {}
    st.session_state.story_completed = False

# Display story description
st.markdown(f"**Selected Story:** {st.session_state.story_name}")

# Get unique word types needed for this story
needed_word_types = list(set(STORIES[st.session_state.story_name]["blanks"]))

# Create input fields for each word type
if not st.session_state.story_completed:
    st.markdown("### Fill in the blanks:")
    for word_type in needed_word_types:
        if word_type not in st.session_state.user_inputs:
            st.markdown(f"**{word_type.title()}** ({WORD_TYPES[word_type]})")
            st.session_state.user_inputs[word_type] = st.text_input(f"Enter a {word_type}:", key=word_type)

    # Generate story button
    if st.button("Generate Story"):
        if all(st.session_state.user_inputs.values()):
            st.session_state.story_completed = True
        else:
            st.error("Please fill in all the blanks!")

# Display the completed story
if st.session_state.story_completed:
    story = STORIES[st.session_state.story_name]["template"]
    for word_type in st.session_state.user_inputs:
        story = story.replace("{" + word_type + "}", st.session_state.user_inputs[word_type])
    
    st.markdown("### Your Story:")
    st.markdown('<div class="story-box">' + story + '</div>', unsafe_allow_html=True)
    
    # New story button
    if st.button("Create New Story"):
        st.session_state.story_name = ""
        st.experimental_rerun()

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit") 