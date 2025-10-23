# OpenJarvis: Personal AI Voice Assistant

Personal AI Voice Assistant with voice command recognition, TTS, AI chatbot, automation, and scheduler capabilities.

## Project Goals

OpenJarvis aims to create a powerful, extensible, and privacy-focused personal AI voice assistant that can:
- Understand and respond to natural voice commands
- Provide intelligent conversational interactions using AI chatbot capabilities
- Automate routine tasks and workflows
- Schedule reminders and manage calendar events
- Operate with hotword detection for hands-free activation
- Maintain user privacy by supporting local processing where possible

## Core Features

### 1. Voice Command Recognition
- Real-time speech-to-text conversion
- Natural language understanding for command parsing
- Support for custom command creation and shortcuts

### 2. Text-to-Speech (TTS)
- Natural-sounding voice synthesis
- Multiple voice options and customization
- Adjustable speech rate and volume

### 3. AI Chatbot Q&A
- Integration with large language models (LLMs)
- Context-aware conversations
- Knowledge base integration
- Multi-turn dialogue support

### 4. Automation
- Execute system commands via voice
- Control smart home devices
- File and application management
- Web scraping and data retrieval
- Custom automation scripts

### 5. Scheduler
- Voice-activated reminders and alarms
- Calendar event management
- Recurring task support
- Integration with popular calendar services

### 6. Hotword Detection
- Always-listening wake word (e.g., "Hey Jarvis")
- Low-power background monitoring
- Customizable activation phrases
- Privacy-focused local processing

## Suggested Tech Stack

### Speech Recognition & TTS
- **Speech Recognition**: 
  - `SpeechRecognition` library (supports multiple engines)
  - Google Speech Recognition API
  - Vosk (offline alternative)
  - Whisper by OpenAI
- **Text-to-Speech**:
  - `pyttsx3` (offline TTS)
  - Google Text-to-Speech (`gTTS`)
  - Coqui TTS (open-source neural TTS)

### AI/NLP
- **LLM Integration**:
  - OpenAI API (GPT-4/GPT-3.5)
  - Anthropic Claude
  - Local LLMs via Ollama or LM Studio
- **NLP Processing**:
  - spaCy
  - NLTK
  - Transformers (Hugging Face)

### Hotword Detection
- Porcupine (Picovoice)
- Snowboy (legacy but still useful)
- Precise (Mycroft AI)

### Automation & Scheduling
- `schedule` library
- `APScheduler`
- `pyautogui` for GUI automation
- `requests` for web APIs

### Core Framework
- Python 3.8+
- `asyncio` for concurrent operations
- `threading` for background tasks

## Example Repo Structure

```
OpenJarvis/
│
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
├── config.yaml              # Configuration file
├── .env                     # Environment variables (API keys)
├── .gitignore              # Git ignore rules
│
├── main.py                  # Entry point
├── jarvis.py               # Main assistant class
│
├── core/
│   ├── __init__.py
│   ├── speech_recognition.py   # STT module
│   ├── text_to_speech.py       # TTS module
│   ├── hotword_detector.py     # Wake word detection
│   └── command_processor.py    # Command parsing logic
│
├── ai/
│   ├── __init__.py
│   ├── chatbot.py             # LLM integration
│   └── nlp_utils.py           # NLP helper functions
│
├── automation/
│   ├── __init__.py
│   ├── system_control.py      # System operations
│   ├── smart_home.py          # Smart device control
│   └── custom_scripts.py      # User-defined automation
│
├── scheduler/
│   ├── __init__.py
│   ├── task_scheduler.py      # Task scheduling logic
│   └── reminders.py           # Reminder management
│
├── utils/
│   ├── __init__.py
│   ├── config_loader.py       # Config file parser
│   ├── logger.py              # Logging utilities
│   └── helpers.py             # Misc helper functions
│
└── tests/
    ├── __init__.py
    ├── test_speech.py
    ├── test_chatbot.py
    └── test_automation.py
```

## Sample Task Flow

### Example 1: Simple Query
1. **User**: "Hey Jarvis" (hotword detected)
2. **System**: *Activation sound* "Yes?"
3. **User**: "What's the weather today?"
4. **Process**: 
   - Speech-to-text conversion
   - NLP parsing identifies weather query
   - Fetch weather data from API
   - Generate response using LLM
5. **System**: "The weather today is sunny with a high of 75°F and a low of 58°F."

### Example 2: Task Automation
1. **User**: "Hey Jarvis, remind me to call John at 3 PM"
2. **Process**:
   - Command recognized as reminder task
   - Extract: task="call John", time="3 PM"
   - Add to scheduler
3. **System**: "Reminder set for 3 PM to call John."
4. **At 3 PM**:
   - **System**: *Notification sound* "Reminder: Call John"

### Example 3: Multi-turn Conversation
1. **User**: "Hey Jarvis, tell me about quantum computing"
2. **System**: *Provides explanation using LLM*
3. **User**: "Can you explain quantum entanglement?"
4. **Process**: Context maintained from previous question
5. **System**: *Provides detailed explanation maintaining conversational context*

### Example 4: System Automation
1. **User**: "Hey Jarvis, open Spotify and play my workout playlist"
2. **Process**:
   - Parse multi-step command
   - Launch Spotify application
   - Navigate to playlist
   - Begin playback
3. **System**: "Playing your workout playlist on Spotify."

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Microphone and speakers
- Internet connection (for cloud-based features)

### Installation

```bash
# Clone the repository
git clone https://github.com/SnakeEye-sudo/OpenJarvis.git
cd OpenJarvis

# Install dependencies
pip install -r requirements.txt

# Set up configuration
cp config.example.yaml config.yaml
# Edit config.yaml with your preferences

# Set up environment variables (API keys)
cp .env.example .env
# Add your API keys to .env
```

### Quick Start

```bash
# Run the basic starter code
python voice_assistant_starter.py
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Roadmap

- [ ] Basic voice recognition and TTS
- [ ] Hotword detection integration
- [ ] OpenAI API integration for chatbot
- [ ] Task scheduler implementation
- [ ] Smart home device control
- [ ] GUI dashboard
- [ ] Mobile app companion
- [ ] Plugin system for extensibility

## Acknowledgments

- Inspired by JARVIS from Iron Man
- Built with open-source tools and libraries
- Community contributions and feedback
