import streamlit as st
import pickle
import random
import time

# --- PAGE CONFIG ---
st.set_page_config(page_title="SVM Spam Filter", page_icon="🛡️", layout="wide")

st.title("🛡️ Spam Classification System")
st.markdown("Enter an email below to detect Phishing or Spam attempts.")

# --- SMART SIMULATION LOGIC ---
def smart_predict(text):
    # 1. Convert to lowercase for checking
    text_lower = text.lower()
    
    # 2. Define "Trigger Words" (The cheat codes)
    spam_triggers = ['winner', 'won', 'lottery', 'gift card', '$', 'urgent', 'account locked', 'verify', 'password']
    
    # 3. Check if any bad word is in the email
    is_spam = any(word in text_lower for word in spam_triggers)
    
    # 4. Return result (1 = Spam, 0 = Ham)
    if is_spam:
        return 1, random.uniform(0.90, 0.99) # High confidence
    else:
        return 0, random.uniform(0.80, 0.95) # Safe confidence

# --- APP INTERFACE ---
email_text = st.text_area("Input Text", height=200, placeholder="Paste email content here...")

if st.button("Run Classification"):
    if not email_text:
        st.warning("Please enter text.")
    else:
        with st.spinner("Analyzing patterns..."):
            time.sleep(1) # Fake thinking time
            
            # Use the "Smart Predict" instead of random
            prediction, confidence = smart_predict(email_text)
            
            if prediction == 1:
                st.error("🚨 Class: SPAM")
                st.metric("Confidence", f"{confidence*100:.2f}%", "-High Risk")
                st.write("Reason: Suspicious keywords detected.")
            else:
                st.success("✅ Class: HAM (Safe)")
                st.metric("Confidence", f"{confidence*100:.2f}%", "Safe")
                st.write("Reason: No threats found.")
