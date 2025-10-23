# STT Engines (Stub)

This folder will host multiple Speech-to-Text backends:
- whisper: local/CPU/GPU
- google: cloud STT
- azure: cognitive services

Each engine exposes a common interface: transcribe(audio_bytes, language) -> text
