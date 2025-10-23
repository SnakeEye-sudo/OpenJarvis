#!/usr/bin/env python3
"""
OpenAI Chat Demo - Basic Integration Example

This script demonstrates how to connect to OpenAI's API to generate
LLM responses based on user input.

=== SETUP INSTRUCTIONS ===

1. Install Required Dependencies:
   pip install openai python-dotenv

   OR use the requirements file if available:
   pip install -r requirements.txt

2. Set Up Your API Key:
   
   Option A - Using Environment Variable (Recommended):
   - Create a .env file in this directory:
     OPENAI_API_KEY=your-api-key-here
   
   Option B - Using System Environment Variable:
   - Export the key in your shell:
     export OPENAI_API_KEY="your-api-key-here"
   
   Option C - Direct Assignment (NOT RECOMMENDED for production):
   - Uncomment line 46 and add your key directly (never commit this!)

3. Get an OpenAI API Key:
   - Sign up at https://platform.openai.com/
   - Navigate to API Keys section
   - Create a new secret key
   - Copy the key (you won't be able to see it again)

=== USAGE ===

   python openai_chat_demo.py

   Then enter your prompt when asked.

=== SECURITY WARNING ===

⚠️  NEVER commit your API key to version control!
⚠️  Add .env to your .gitignore file
⚠️  API keys should be kept secret and rotated regularly
⚠️  Monitor your OpenAI usage to avoid unexpected charges

"""

import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
# The API key will be automatically loaded from OPENAI_API_KEY environment variable
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
    # api_key="your-api-key-here"  # UNSAFE: Only use for testing, never commit!
)


def chat_with_openai(user_prompt, model="gpt-3.5-turbo", temperature=0.7):
    """
    Send a prompt to OpenAI and return the response.
    
    Args:
        user_prompt (str): The user's input message
        model (str): OpenAI model to use (default: gpt-3.5-turbo)
        temperature (float): Controls randomness (0.0-2.0, default: 0.7)
    
    Returns:
        str: The LLM-generated response
    """
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_prompt}
            ],
            temperature=temperature,
            max_tokens=500  # Limit response length to control costs
        )
        
        return response.choices[0].message.content
    
    except Exception as e:
        return f"Error: {str(e)}"


def main():
    """
    Main function to run the interactive chat demo.
    """
    print("="*60)
    print("OpenAI Chat Demo")
    print("="*60)
    print("\nThis demo connects to OpenAI's API to generate responses.")
    print("Make sure you have set your OPENAI_API_KEY environment variable.\n")
    
    # Verify API key is set
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ ERROR: OPENAI_API_KEY not found!")
        print("\nPlease set your API key using one of these methods:")
        print("  1. Create a .env file with: OPENAI_API_KEY=your-key-here")
        print("  2. Export in shell: export OPENAI_API_KEY='your-key-here'")
        print("\nGet your API key from: https://platform.openai.com/api-keys")
        return
    
    print("✓ API key found!\n")
    
    # Get user input
    user_prompt = input("Enter your prompt: ").strip()
    
    if not user_prompt:
        print("No prompt provided. Exiting.")
        return
    
    print("\n🤖 Generating response...\n")
    
    # Get response from OpenAI
    response = chat_with_openai(user_prompt)
    
    # Print the response
    print("-" * 60)
    print("Response:")
    print("-" * 60)
    print(response)
    print("-" * 60)


if __name__ == "__main__":
    main()
