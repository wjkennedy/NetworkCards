import streamlit as st
import qrcode
import io
import base64

# Function to generate NFC data payload
def generate_nfc_payload(name, company, phone, email, linkedin, website):
    payload = f"Name: {name}\nCompany: {company}\nPhone: {phone}\nEmail: {email}\nLinkedIn: {linkedin}\nWebsite: {website}"
    return payload

# Function to create and encode a QR code
def generate_qr_code(data):
    qr = qrcode.make(data)
    img_bytes = io.BytesIO()
    qr.save(img_bytes, format="PNG")
    return img_bytes.getvalue()

# Streamlit App Interface
st.title("A9 NFC Digital Networking Cards")
st.markdown("""
**Why use NFC for Networking?**  
Traditional business cards get lost or discarded, but NFC-powered digital business cards provide instant, tap-to-share interactions.  
With this app, you can create NFC business cards and export them for use with **Chameleon Ultra**.
""")

st.subheader("📝 Enter Your Networking Details")

# User Input Form
with st.form("nfc_form"):
    name = st.text_input("Full Name", placeholder="Your Name")
    company = st.text_input("Company", placeholder="A9 Group, Inc.")
    phone = st.text_input("Phone Number", placeholder="+1 234 567 8901")
    email = st.text_input("Email", placeholder="yourname@email.com")
    linkedin = st.text_input("LinkedIn URL", placeholder="https://linkedin.com/in/your-name")
    website = st.text_input("Website (optional)", placeholder="https://yoursite.com")

    submitted = st.form_submit_button("Generate NFC Card")

# Processing after user submission
if submitted:
    if not (name and company and phone and email and linkedin):
        st.error("Please fill in all required fields.")
    else:
        nfc_data = generate_nfc_payload(name, company, phone, email, linkedin, website)

        # Display NFC text payload
        st.subheader("NFC Data Generated")
        st.code(nfc_data, language="text")

        # Create QR code
        qr_code = generate_qr_code(nfc_data)
        st.subheader("📌 QR Code for Networking")
        st.image(qr_code, caption="Scan to access networking info")

        # Download NFC data as a text file
        st.download_button(
            label="Download NFC Data (for Chameleon Ultra or other NFC writer)",
            data=nfc_data.encode(),
            file_name="nfc_card.txt",
            mime="text/plain",
        )

st.info("Now you can tap an NFC-enabled device or scan the QR code to instantly share your details!")


