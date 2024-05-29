# Resume Analysis with LlamaIndex and Ollama

This project extracts and analyzes the achievements section from resumes in PDF format, breaking down each achievement into action verbs, tasks/projects, and results/metrics.

## Prerequisites

1. Python 3.7 or higher
2. [pip](https://pip.pypa.io/en/stable/installation/) (Python package installer)

## Installation Steps

### 1. Install Required Python Packages

Install the necessary Python packages using pip:

```
pip install llama-index ollama python-dotenv
```
### 2. Install the Phi3 Model using Ollama
Ensure you have Ollama installed and set up. Follow the installation instructions for Ollama from their official documentation.

Once installed, install Phi3 model to Ollama:
```
ollama run phi3
```
#### 3. Project Structure
Create a folder structure as follows:

```
resume-analysis/
│
├── resume/
│   └── your_resume.pdf
├── .env
├── main.py
└── README.md
```
#### Place your resume PDFs inside the resume folder.

### 4. Set Up Environment Variables
Create a .env file in the project root directory and add your llama cloud api key from the llama cloud website.
```LLAMA_CLOUD_API_KEY=""```

### 5. Script Execution
Make sure you have the main.py as in the repo.

### 6. Run the Script
Execute the script:

```
python main.py
```
The script will process the PDFs in the resume folder, extract the achievements section, and print each achievement divided into action verbs, tasks/projects, and results/metrics.

Notes
Ensure the achievements section in the PDF resumes is clearly labeled for accurate extraction.
Modify the query in the script if the section titles differ in your resumes.
