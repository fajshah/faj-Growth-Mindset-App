import streamlit as st
import random


# List of motivational messages and tips
messages = [
    "Believe in yourself — every failure is a step closer to success.",
    "Growth happens outside of your comfort zone. Keep pushing!",
    "Success is not final, failure is not fatal: it’s the courage to continue that counts.",
    "Be patient with progress. Small steps lead to big changes.",
    "Learn from criticism — feedback is fuel for growth.",
    "Surround yourself with positivity and people who inspire you.",
    "Every day is a chance to become a better version of yourself.",
    "Embrace mistakes — they are proof that you’re learning."
]

# Streamlit UI
st.title("🌟 Growth Mindset App")
st.markdown("---")
st.image("https://www.w3schools.com/w3images/lights.jpg", caption="Unlock Your Potential 🚀")


st.markdown("---")


st.write("Welcome to your personal growth mindset coach! Click the button to receive motivation and actionable growth tips.")

if st.button("Get Inspired!"):
    message = random.choice(messages)
    st.success(f"💬 **{message}**")
    
    st.subheader("Action Steps for Growth")
    st.write("- Reflect on a recent challenge and write down what you learned.")
    st.write("- Set one small, achievable goal for today.")
    st.write("- Practice gratitude by listing three things you’re thankful for.")
    st.write("- Take a break and do something that sparks creativity (like journaling or drawing).")

st.markdown("---")
st.markdown(
    "<div style='text-align: center; padding: 10px; color: #FF0000;'>Developed by <strong>S.Farzana Shah</strong> | 🚀 Keep growing!</div>",
    unsafe_allow_html=True
)


st.write("Remember: Growth is a continuous process, and every step counts. 🚀")

# Let me know if you want me to add more features, like journaling or daily affirmations! ✨
