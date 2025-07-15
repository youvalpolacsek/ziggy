from core.voice import start_listening
from core.memory import load_memory
from core.telegram import start_telegram_bot

if __name__ == "__main__":
    load_memory()
    start_listening()
    start_telegram_bot()
