# Triaging_Assignment
Test Assignment — Healthcare Agent System Mini Project

# Healthcare Triage API

This project provides an API to analyze symptoms and recommend a suitable medical specialist using Google Gemini AI.

## Setup Instructions

### Prerequisites
- Python 3.8+
- A valid API key for Google Generative AI

### Installation
1. Clone the repository:
   ```bash
    https://github.com/SantoshKumarGupta-iisc/Triaging_Assignment.git
    cd Triaging_Assignment
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the API key in chatbot.py and main.py:
    replace "api-key" with your actual API key in chatbot.py and main.py first line
    ```python
    GEMINI_API_KEY = "api-key"
    ```

### Testing the API
You can test using `curl`:
```bash
curl -X POST "http://127.0.0.1:8000/triage" -H "Content-Type: application/json" -d '{"symptom_description": "I have chest pain."}'
```

Or use Postman / any API testing tool.

### Notes
- Ensure your API key is set correctly to avoid authentication issues.
- Logs are stored in `agent.log` for debugging purposes.

## License
MIT