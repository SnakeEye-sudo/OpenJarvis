# LLM Integration

This directory contains connectors and demo code for integrating various Large Language Models (LLMs) into OpenJarvis.

## Planned Connectors

- OpenAI
- Anthropic
- Azure OpenAI
- Ollama (local)
- Hugging Face Inference

## Standard Interface

All LLM connectors will implement a common interface:

- `generate(prompt, context) -> text`
- `stream_generate(prompt, context) -> tokens`

## Demo Files

### OpenAI Chat Demo

File: `openai_chat_demo.py`

A basic example demonstrating how to connect to OpenAI's API and generate responses.

**Quick Start:**

```bash
# Install dependencies
pip install openai python-dotenv

# Set your API key
export OPENAI_API_KEY="your-api-key-here"

# Run the demo
python openai_chat_demo.py
```

**Example Usage:**

```python
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, how are you?"}
    ]
)

print(response.choices[0].message.content)
```

## ⚠️ Security & API Key Management

**IMPORTANT WARNINGS:**

1. **Never commit API keys to version control**
   - Always use environment variables or `.env` files
   - Add `.env` to your `.gitignore` file immediately

2. **Protect your API keys**
   - Treat them like passwords
   - Rotate keys regularly
   - Use different keys for development and production

3. **Monitor usage and costs**
   - Set up billing alerts on your LLM provider dashboard
   - Implement rate limiting in production code
   - Use `max_tokens` parameter to control response costs

4. **API Key Setup Methods (in order of preference):**
   - **Best**: Use `.env` file with `python-dotenv` (never commit this file)
   - **Good**: System environment variables
   - **Avoid**: Hardcoding keys in source code

**Example `.env` file:**

```
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxxx
ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxxxxxxxxxx
```

## Implementation Notes

- **Rate Limiting**: All connectors should implement exponential backoff for API rate limits
- **Retries**: Handle transient errors with configurable retry logic
- **Safety Filters**: Respect content moderation APIs where available
- **Error Handling**: Gracefully handle API errors and provide meaningful error messages
- **Timeouts**: Set reasonable timeouts to prevent hanging requests

## Getting API Keys

- **OpenAI**: https://platform.openai.com/api-keys
- **Anthropic**: https://console.anthropic.com/settings/keys
- **Azure OpenAI**: https://portal.azure.com/
- **Hugging Face**: https://huggingface.co/settings/tokens

## Contributing

When adding new LLM connectors:

1. Follow the standard interface pattern
2. Include comprehensive error handling
3. Add demo/example code
4. Document API key requirements
5. Include unit tests
6. Update this README with your connector

---

🔒 Remember: Security is not optional. Always protect your API keys!
