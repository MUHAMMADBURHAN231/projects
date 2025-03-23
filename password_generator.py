import streamlit as st
import random
import string
import pyperclip
import re

# Set page config
st.set_page_config(
    page_title="Password Generator",
    page_icon="🔑",
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
    .password-box {
        background-color: white;
        padding: 15px;
        border-radius: 5px;
        border: 1px solid #ddd;
        margin: 10px 0;
        font-family: monospace;
        font-size: 18px;
        text-align: center;
    }
    .strength-bar {
        height: 20px;
        border-radius: 10px;
        margin: 10px 0;
        transition: all 0.3s ease;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and description
st.title("🔑 Password Generator")
st.markdown("### Generate secure passwords with customizable options")

# Password options
st.sidebar.title("Password Options")

# Password length
password_length = st.sidebar.slider(
    "Password Length",
    min_value=8,
    max_value=32,
    value=12,
    step=1
)

# Character options
st.sidebar.subheader("Character Types")
use_uppercase = st.sidebar.checkbox("Uppercase Letters (A-Z)", value=True)
use_lowercase = st.sidebar.checkbox("Lowercase Letters (a-z)", value=True)
use_numbers = st.sidebar.checkbox("Numbers (0-9)", value=True)
use_special = st.sidebar.checkbox("Special Characters (!@#$%^&*)", value=True)

# Generate password function
def generate_password(length, uppercase, lowercase, numbers, special):
    characters = ""
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if numbers:
        characters += string.digits
    if special:
        characters += string.punctuation
    
    if not characters:
        return "Please select at least one character type"
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Password strength checker
def check_password_strength(password):
    score = 0
    if len(password) >= 12:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"\d", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    
    return score

# Generate button
if st.button("Generate Password"):
    password = generate_password(
        password_length,
        use_uppercase,
        use_lowercase,
        use_numbers,
        use_special
    )
    
    if password != "Please select at least one character type":
        # Display password
        st.markdown('<div class="password-box">' + password + '</div>', unsafe_allow_html=True)
        
        # Copy button
        if st.button("Copy to Clipboard"):
            pyperclip.copy(password)
            st.success("Password copied to clipboard!")
        
        # Password strength indicator
        strength = check_password_strength(password)
        strength_text = ["Very Weak", "Weak", "Medium", "Strong", "Very Strong"]
        strength_color = ["#ff4444", "#ffbb33", "#ffeb3b", "#00C851", "#007E33"]
        
        st.markdown("### Password Strength")
        st.markdown(f"<div class='strength-bar' style='background-color: {strength_color[strength-1]}; width: {strength*20}%;'></div>", unsafe_allow_html=True)
        st.markdown(f"**{strength_text[strength-1]}**")
        
        # Password requirements checklist
        st.markdown("### Password Requirements")
        st.markdown(f"""
        - Length ≥ 12 characters: {'✅' if len(password) >= 12 else '❌'}
        - Contains uppercase letters: {'✅' if re.search(r"[A-Z]", password) else '❌'}
        - Contains lowercase letters: {'✅' if re.search(r"[a-z]", password) else '❌'}
        - Contains numbers: {'✅' if re.search(r"\d", password) else '❌'}
        - Contains special characters: {'✅' if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) else '❌'}
        """)
    else:
        st.error(password)

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit") 