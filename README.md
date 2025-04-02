# Triaging_Assignment
Test Assignment — Healthcare Agent System Mini Project

# Healthcare Triage API

This project provides an API to analyze symptoms and recommend a suitable medical specialist using Google Gemini AI.

## Setup Instructions

### Prerequisites
- Python 3.8+
- pip
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

### Description of the Custom Tool Implementation
The custom tool is implemented as a FastAPI that interacts with the Google Gemini LLM to provide healthcare triage recommendations. The API accepts a symptom description as input, processes it using the agent, and returns the most suitable medical specialist. Key features include:
- **Agent Design**: The agent is responsible for interpreting user input and mapping symptoms to predefined medical specialties.
- **Prompt Design**: The prompt is carefully structured to guide the LLM in making accurate and context-aware recommendations.
- **Logging**: Comprehensive logging is implemented to track API requests, responses, and the agent's decision-making process for debugging and auditing purposes.

### Bonus Tasks
1. **Enhanced Logging**: Added detailed logs to capture the full interaction flow, including input symptoms, LLM responses, and final recommendations.
2. **Error Handling**: Implemented robust error handling to manage invalid inputs, API key issues, and LLM service downtime gracefully.
3. **Scalability**: Designed the API to be lightweight and scalable, ensuring it can handle multiple concurrent requests efficiently.
4. **Documentation**: Provided clear and concise documentation for setup, usage, and testing to improve developer experience.


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