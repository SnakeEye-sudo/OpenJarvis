#!/usr/bin/env python3
"""
OpenJarvis Voice Assistant Starter
A simple hello-world implementation demonstrating basic speech recognition and text-to-speech.

Dependencies:
    pip install SpeechRecognition pyttsx3 pyaudio

Note: On Linux, you may also need to install:
    sudo apt-get install portaudio19-dev python3-pyaudio
"""

import speech_recognition as sr
import pyttsx3
import sys


class VoiceAssistant:
    """Basic voice assistant with speech recognition and text-to-speech capabilities."""
    
    def __init__(self):
        """Initialize the voice assistant with speech recognizer and TTS engine."""
        # Initialize speech recognizer
        self.recognizer = sr.Recognizer()
        
        # Initialize text-to-speech engine
        self.tts_engine = pyttsx3.init()
        
        # Configure TTS properties
        self.tts_engine.setProperty('rate', 150)    # Speed of speech
        self.tts_engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)
        
        # Get available voices and set a default
        voices = self.tts_engine.getProperty('voices')
        if voices:
            # You can change the voice by selecting a different index
            self.tts_engine.setProperty('voice', voices[0].id)
    
    def speak(self, text):
        """Convert text to speech.
        
        Args:
            text (str): The text to speak
        """
        print(f"Assistant: {text}")
        self.tts_engine.say(text)
        self.tts_engine.runAndWait()
    
    def listen(self, timeout=5, phrase_time_limit=5):
        """Listen for voice input and convert to text.
        
        Args:
            timeout (int): Seconds to wait for speech to start
            phrase_time_limit (int): Maximum seconds for the phrase
            
        Returns:
            str: Recognized text, or None if recognition failed
        """
        with sr.Microphone() as source:
            print("Listening...")
            
            # Adjust for ambient noise
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
            
            try:
                # Listen for audio
                audio = self.recognizer.listen(
                    source, 
                    timeout=timeout, 
                    phrase_time_limit=phrase_time_limit
                )
                
                print("Processing...")
                
                # Recognize speech using Google Speech Recognition
                text = self.recognizer.recognize_google(audio)
                print(f"You said: {text}")
                return text.lower()
                
            except sr.WaitTimeoutError:
                print("Listening timeout - no speech detected")
                return None
            except sr.UnknownValueError:
                print("Could not understand audio")
                return None
            except sr.RequestError as e:
                print(f"Could not request results from speech recognition service; {e}")
                return None
    
    def process_command(self, command):
        """Process voice commands and generate appropriate responses.
        
        Args:
            command (str): The command text to process
            
        Returns:
            bool: False if exit command received, True otherwise
        """
        if command is None:
            return True
        
        # Exit commands
        if any(word in command for word in ['exit', 'quit', 'goodbye', 'bye']):
            self.speak("Goodbye! Have a great day!")
            return False
        
        # Greeting commands
        elif any(word in command for word in ['hello', 'hi', 'hey']):
            self.speak("Hello! How can I help you today?")
        
        # Introduction
        elif 'your name' in command or 'who are you' in command:
            self.speak("I am Jarvis, your personal AI voice assistant. I'm still learning, but I'm here to help!")
        
        # Help command
        elif 'help' in command:
            self.speak("I can respond to greetings, tell you about myself, and answer simple questions. Try saying hello, or ask me who I am!")
        
        # Time query (example - requires datetime import)
        elif 'time' in command:
            from datetime import datetime
            current_time = datetime.now().strftime("%I:%M %p")
            self.speak(f"The current time is {current_time}")
        
        # Date query
        elif 'date' in command or 'today' in command:
            from datetime import datetime
            current_date = datetime.now().strftime("%B %d, %Y")
            self.speak(f"Today is {current_date}")
        
        # How are you
        elif 'how are you' in command:
            self.speak("I'm doing great, thank you for asking! How can I assist you?")
        
        # Thank you
        elif 'thank you' in command or 'thanks' in command:
            self.speak("You're welcome! Happy to help!")
        
        # Default response for unrecognized commands
        else:
            self.speak("I'm not sure how to respond to that yet. I'm still learning! Try asking for help to see what I can do.")
        
        return True
    
    def run(self):
        """Main loop for the voice assistant."""
        self.speak("Hello! I am Jarvis, your voice assistant. How can I help you today?")
        self.speak("Say 'help' to learn what I can do, or 'exit' to quit.")
        
        while True:
            # Listen for command
            command = self.listen()
            
            # Process command
            if not self.process_command(command):
                break


def main():
    """Main entry point for the voice assistant."""
    print("="*50)
    print("OpenJarvis Voice Assistant - Starter Version")
    print("="*50)
    print("\nMake sure your microphone is connected and working.")
    print("Speak clearly when prompted.\n")
    
    try:
        assistant = VoiceAssistant()
        assistant.run()
    except KeyboardInterrupt:
        print("\n\nInterrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\nError: {e}")
        print("\nMake sure you have installed all dependencies:")
        print("  pip install SpeechRecognition pyttsx3 pyaudio")
        sys.exit(1)


if __name__ == "__main__":
    main()
