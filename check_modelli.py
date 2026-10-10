import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
chiave = os.getenv("GEMINI_API_KEY")

if not chiave:
    print("Errore: Chiave API non trovata nel file .env")
    exit()

client = genai.Client(api_key=chiave)

print("Interrogo i server di Google...\nI modelli disponibili per te sono:\n")
try:
    # Chiediamo a Google la lista aggiornata
    for m in client.models.list():
        # Filtriamo e stampiamo il nome tecnico esatto
        print(m.name)
except Exception as e:
    print("Errore di connessione:", e)