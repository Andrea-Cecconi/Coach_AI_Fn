import os
import google.generativeai as genai
from dotenv import load_dotenv
from PIL import Image

# 1. Carica le variabili nascoste dal file .env
load_dotenv()
chiave_api = os.getenv("GEMINI_API_KEY")

if not chiave_api:
    raise ValueError("Chiave API non trovata! Controlla il file .env")

# 2. Configura l'SDK e scegli il modello (Flash è veloce e gratuito)
genai.configure(api_key=chiave_api)
model = genai.GenerativeModel('gemini-1.5-flash')

# 3. Cerchiamo il primo frame disponibile nella cartella
cartella_output = "replay_frames"
frame_test = None

if os.path.exists(cartella_output):
    for file in sorted(os.listdir(cartella_output)):
        if file.endswith(".png"):
            frame_test = os.path.join(cartella_output, file)
            break

if frame_test:
    print(f"Frame trovato: {frame_test}. Invio all'AI in corso...")
    
    # Apriamo l'immagine
    img = Image.open(frame_test)
    
    # Il primo vero "System Prompt" del nostro coach
    prompt = """
    Sei un coach professionista di Fortnite (stile MykeTV). 
    Analizza questa schermata di gioco in modo crudo e diretto.
    Dimmi cosa vedi riguardo a: salute/scudo, materiali rimasti, armi nell'inventario e zona (se visibile).
    Sii conciso e usa il gergo di Fortnite.
    """
    
    # Invia immagine e testo al modello
    response = model.generate_content([prompt, img])
    
    print("\n--- RISPOSTA DEL COACH ---")
    print(response.text)
else:
    print("Nessun frame trovato. Avvia prima 'cattura.py', premi F9 per scattare una foto e poi riprova!")