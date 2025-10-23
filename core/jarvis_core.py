"""
Jarvis Core Orchestrator
- Routes: STT -> NLU -> LLM -> Actions -> TTS
- Manages plugins, memory, context, and event bus.
This is a stub for architecture and extensibility notes.
"""

class JarvisCore:
    def __init__(self):
        # TODO: load config, initialize modules, plugin manager, and bus
        pass

    def handle_voice_request(self, audio_chunk):
        """Pipeline entry: audio -> text -> intent -> actions -> speech"""
        pass
