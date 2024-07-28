import streamlit as st
from transformers import pipeline
import datetime

def generate_cover_letter(prompt, name, address, city_state_zip, email, phone, hiring_manager_name, company_name, company_address):
    text_generator = pipeline("text-generation", model="gpt2")
    
    title_prompt = f"write subject for skills {prompt}"
    title = text_generator(title_prompt, max_length=10)[0]['generated_text']

    script_prompt = f"Write a letter '{title}'"
    script = text_generator(script_prompt, max_length=300)[0]['generated_text']

    header = f"{name}\n\n{address}\n\n{city_state_zip}\n\n{email}\n\n{phone}\n\n{datetime.datetime.now().strftime('%B %d, %Y')}\n\n{hiring_manager_name}\n\n{company_name}\n\n{company_address}\n\nDear {hiring_manager_name},\n\n"

    footer = f"\n\nWarm regards,\n\n{name}"

    cover_letter = header + script + footer
    
    return cover_letter

st.title('Cover letter generator📃 ~ Nakshatra')
prompt = st.text_input('Input your skills here')

if prompt:
    name = st.text_input("Your Name")
    address = st.text_input("Your Address")
    city_state_zip = st.text_input("City, State, Zip Code")
    email = st.text_input("Your Email Address")
    phone = st.text_input("Your Phone Number")
    hiring_manager_name = st.text_input("Hiring Manager's Name")
    company_name = st.text_input("Company Name")
    company_address = st.text_input("Company Address")

    if st.button('Submit'):
        if name and address and city_state_zip and email and phone and hiring_manager_name and company_name and company_address:
            cover_letter = generate_cover_letter(prompt, name, address, city_state_zip, email, phone, hiring_manager_name, company_name, company_address)

            st.write(cover_letter)
        else:
            st.warning("Please fill in all the required fields.")
