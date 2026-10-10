import os
from google import genai
from dotenv import load_dotenv
from PIL import Image

# 1. Carica le variabili nascoste
load_dotenv()
chiave_api = os.getenv("GEMINI_API_KEY")

if not chiave_api:
    raise ValueError("Chiave API non trovata! Controlla il file .env")

# 2. Inizializza il nuovo Client (Sintassi SDK aggiornata)
client = genai.Client(api_key=chiave_api)

# 3. Cerchiamo il frame
cartella_output = "replay_frames"
frame_test = None

if os.path.exists(cartella_output):
    for file in sorted(os.listdir(cartella_output)):
        if file.endswith(".png"):
            frame_test = os.path.join(cartella_output, file)
            break

if frame_test:
    print(f"Frame trovato: {frame_test}. Invio al modello PRO in corso...")
    
    img = Image.open(frame_test)
    
    prompt = """
    Sei un coach professionista di Fortnite (stile MykeTV). 
    Analizza questa schermata di gioco in modo crudo e diretto.
    Dimmi cosa vedi riguardo a: salute/scudo, materiali rimasti, armi nell'inventario e zona (se visibile).
    Sii conciso e usa il gergo di Fortnite.
    """
    
   # 4. Nuova struttura per generare il contenuto
    response = client.models.generate_content(
        model='gemini-3.1-pro-preview',
        contents=[img, prompt]
    )
    
    print("\n--- RISPOSTA DEL COACH ---")
    print(response.text)
else:
    print("Nessun frame trovato. Avvia prima 'cattura.py'!")