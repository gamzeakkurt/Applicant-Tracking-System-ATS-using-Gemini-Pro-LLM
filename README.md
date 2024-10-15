# Applicant Tracking System (ATS) using Gemini Pro LLM (Resume Analysis)


The **Applicant Tracking System (ATS)** is an intelligent tool designed to enhance resume analysis by leveraging Google's **Generative AI (Gemini)**. This system allows users to submit resumes in **PDF format** and match them against job descriptions. It provides feedback on strengths and weaknesses, identifies missing keywords, and suggests skill improvements to increase alignment with the job.

The application is built using **Streamlit** for an interactive web interface and incorporates tools such as **PyPDF2** for PDF processing and **Google Generative AI** for content generation.

## Key Features

- Upload resumes in **PDF** format.
- Get feedback on your resume's alignment with a job description.
- Identify missing keywords.
- Receive suggestions for improving skills.
- Calculate a percentage match between your resume and the job description.
- Clear all information

## Built With

- **Streamlit** - Frontend framework for web applications.
- **PyPDF2** - PDF content extraction.
- **Google Generative AI** - AI-powered resume analysis.
- **Python-dotenv** - Manage API keys and environment variables.

## Installation

Follow these steps to set up the project locally:

### Prerequisites

- Python 3.10
- Streamlit
- Google Generative AI API key

### Installation Steps

1. **Clone the Repository**  
   Open your terminal and clone the project from GitHub:
   ```bash
   git clone https://github.com/gamzeakkurt/Applicant-Tracking-System-ATS-using-Gemini-Pro-LLM.git
   ```

2. **Create a Virtual Environment** (Optional but recommended):
   ```bash
   conda create -p <Environment_Name> python==<python_version> -y
   conda activate <Environment_Name>
   ```

3. **Install Dependencies**  
   Navigate to the project directory and install the required dependencies:
   ```bash
   cd [project_directory]
   pip install -r requirements.txt
   ```

4. **Set Up API Key**  
   Create a `.env` file in the project root and add your Google Generative AI API key:
   ```bash
   GOOGLE_API_KEY=your_api_key_here
   ```
   **A small warning**: Do not share your Google API key with anyone.

5. **Run the Application**  
   Start the Streamlit app by running:
   ```bash
   streamlit run app.py
   ```

6. **Access the App**  
   Open a web browser and navigate to the provided Streamlit URL to use the ATS.

## API Key Setup

To use the Google Generative AI services, you need an API key. Here's how to get it:

1. Visit [Google Gemini API](https://ai.google.dev/#gemini-api) to create an account and obtain your API key.
2. Add the key to a `.env` file in the project directory as shown above.

## How It Works

- **Resume Upload**: Users can upload resumes in PDF format, and the system extracts content using **pdf2image**.
- **Job Description Input**: The job description is entered into a text area, which helps generate a tailored response.
- **Generative AI Processing**: Google’s **Gemini AI** analyzes the resume and job description to provide feedback.
- **Results**: The system displays the evaluation, missing keywords, and suggestions for improvement.

## Contributing

We welcome contributions to enhance the project!

- **Report Bugs**: Open an issue to report bugs.
- **Contribute Code**: Fork the repository, make your changes, and open a pull request.
- **Suggestions**: Have ideas? Open an issue to share your suggestions.

## License

Distributed under the MIT License. See `LICENSE` for more information.

---

Let me know if you need any further adjustments or additions!
