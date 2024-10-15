from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import pdf2image
import google.generativeai as genai
import io
import base64

# Load environment variables
load_dotenv()

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get response from the Gemini API
def get_gemini_response(input_text, pdf_content, prompt):
    try:
        model = genai.GenerativeModel('gemini-pro-vision')
        response = model.generate_content([input_text, pdf_content[0], prompt])
        return response.text
    except Exception as e:
        st.error(f"Error with API request: {str(e)}")
        return None

# Function to extract PDF content as images and base64 encoded
def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        try:
            images = pdf2image.convert_from_bytes(uploaded_file.read())
            first_page = images[0]

            # Convert the first page to bytes
            img_byte_arr = io.BytesIO()
            first_page.save(img_byte_arr, format='JPEG')
            img_byte_arr = img_byte_arr.getvalue()

            # Encode as base64
            pdf_parts = [
                {
                    "mime_type": "image/jpeg",
                    "data": base64.b64encode(img_byte_arr).decode()  # to encode to base64
                }
            ]

            return pdf_parts
        except Exception as e:
            st.error(f"Error processing the PDF: {str(e)}")
            return None
    else:
        st.error("No file uploaded")
        return None

# Inject custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #EBD3F8;
            text-align: left; /* Change the background color */
        }

        .ribbon-container {
            text-align: center;
            position: relative;
            margin-bottom: 20px;
        }

        .ribbon {
            background: #8EACCD;
            color: #333;
            padding: 20px 40px;
            font-size: 24px;
            font-family: 'Open Sans', sans-serif;
            font-weight: bold;
            text-align: center;
            letter-spacing: 2px;
            display: inline-block;
            position: relative;
            z-index: 1;
            margin: 20px auto;
        }

        /* Style for input area */
        textarea {
            font-size: 16pt; /* Set font size to 16 point */
            font-style: italic; /* Make font italic */
            width: 100%; /* Full width */
            height: 150px; /* Set height for better visibility */
            padding: 10px; /* Add padding for better usability */
            border: 1px solid #ccc; /* Optional border */
            border-radius: 5px; /* Optional rounded corners */
        }

        /* Style for the label */
        .job-description-label {
            font-size: 16pt; /* Set font size for label */
            font-style: italic; /* Make label italic */
            font-weight: bold; /* Optional: make the label bold */
        }

        /* Button styling */
        .stButton > button {
            background-color: #8EACCD; /* Green background */
            border: none;
            color: white;
            padding: 15px 32px;
            text-align: center;
            font-size: 16px;
            margin: 4px 2px;
            border-radius: 12px; /* Rounded corners */
            transition-duration: 0.4s; /* Animation */
        }
        
        .stButton > button:hover {
            background-color: #DEE5D4; 
            color: black; 
            border: 2px solid #DEE5D4; /* Hover effect */
        }
    </style>
""", unsafe_allow_html=True)

# Display the ribbon header
st.markdown("""
    <div class="ribbon-container">
        <div class="ribbon">
            <em>Applicant Tracking System - 
                Resume Analysis</em>
        </div>
        <div class="ribbon-shadow"></div>
    </div>
""", unsafe_allow_html=True)

# Initialize session state before widgets
if 'clear_triggered' not in st.session_state:
    st.session_state.clear_triggered = False
if 'input' not in st.session_state:
    st.session_state.input = ""

# Function to clear the input text and reset everything (except file_uploader widget)
def clear_input():
    st.session_state.input = ""  # Clear the text input
    st.session_state.clear_triggered = True  # Trigger clearing state
    st.success("Successfully cleared all inputs!")  # Success message

# Display the text area with a styled label
st.markdown("""
        <div class="body">
            <label class="job-description-label">Enter the Job Description:</label>
        </div> 
""", unsafe_allow_html=True)
input_text = st.text_area("", value=st.session_state.input, key="input")

st.markdown("""
        <div class="body">
            <label class="job-description-label">Upload your Resume (PDF only):</label>
        </div>
""", unsafe_allow_html=True)

# File uploader for the resume in PDF format
uploaded_file = st.file_uploader("", type=["pdf"])

if uploaded_file and not st.session_state.clear_triggered:
    st.success("PDF Uploaded Successfully")

# Create buttons with icons for different actions
submit1 = st.button("✅ Tell Me About the Resume")
submit2 = st.button("⚙️ How Can I Improve My Skills?")
submit3 = st.button("🔍 What Keywords Are Missing?")
submit4 = st.button("📊 Check Percentage Match")
clear = st.button("Clear", on_click=clear_input)

# Define prompts
input_prompt1 = """
You are an experienced Technical Human Resource Manager. Your task is to review the provided resume against the job description. 
Please provide a professional evaluation on whether the candidate's profile aligns with the role. 
Highlight the strengths and weaknesses of the applicant concerning the job requirements.
"""

input_prompt2 = """
You are a career advisor with extensive experience. Your task is to suggest specific skills the applicant can develop 
or improve to enhance their suitability for the job described in the job description and resume.
"""

input_prompt3 = """
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of how ATS works. 
Evaluate the resume against the provided job description and provide a percentage match. 
List missing keywords and give your final thoughts.
"""

# Define function to display output based on user actions
def process_request(prompt):
    if uploaded_file and not st.session_state.clear_triggered:
        pdf_content = input_pdf_setup(uploaded_file)
        if pdf_content:
            with st.spinner('Processing...'):
                response = get_gemini_response(input_text, pdf_content, prompt)
                if response:
                    st.subheader("The Response is:")
                    st.write(response)
                else:
                    st.error("No response received from the API.")
        else:
            st.error("Error in extracting content from PDF.")
    else:
        st.error("Please upload your resume in PDF format.")

# Handle button actions
if submit1:
    process_request(input_prompt1)
elif submit2:
    process_request(input_prompt2)
elif submit3:
    process_request(input_prompt3)
elif submit4:
    process_request(input_prompt3)  # Reusing prompt 3 for percentage match

# Reset the clear trigger after processing
if st.session_state.clear_triggered:
    st.session_state.clear_triggered = False  # Reset the clearing state after one run
