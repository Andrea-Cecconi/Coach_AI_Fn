import os
from google import genai
from dotenv import load_dotenv
from PIL import Image

# 1. Carica le variabili nascoste
load_dotenv()
chiave_api = os.getenv("GEMINI_API_KEY")

if not chiave_api:
    raise ValueError("Chiave API non trovata! Controlla il file .env")

client = genai.Client(api_key=chiave_api)

cartella_output = "replay_frames"
frame_paths = []

# 2. Raccogliamo TUTTI i frame nella cartella (NIENTE PIÙ 'break')
if os.path.exists(cartella_output):
    for file in sorted(os.listdir(cartella_output)):
        if file.endswith(".png"):
            frame_paths.append(os.path.join(cartella_output, file))

if frame_paths:
    print(f"Trovati {len(frame_paths)} frame. Creazione del video-analisi in corso...")
    
    # 3. Apriamo tutte le immagini e le carichiamo in una lista
    immagini = [Image.open(path) for path in frame_paths]
    
    # 4. Prompt aggiornato con ancoraggio visivo e analisi di sequenza
    prompt = """
    Sei un coach professionista di Fortnite a livello competitivo (stile MykeTV). 
    Non fai complimenti inutili e vai dritto al punto.
    
    CONTESTO DEL GIOCATORE:
    Usa un controller Xbox Elite Series 2 con paddle posteriori (salti/build fluidi senza staccare i pollici dagli analogici).
    
    REGOLE DI LETTURA HUD ESTREMA:
    - La barra VERDE è la Salute (HP).
    - La barra BLU è lo Scudo (Shield).
    Non invertire mai questi due valori. Leggili accuratamente.
    
    ANALISI DELLA SEQUENZA:
    Ti sto inviando una sequenza temporale di frame estratti da un VOD. 
    Analizza l'evoluzione dell'azione (chi sta pushando? Il giocatore sta ruotando o fightando?) e restituisci questo report formattato:
    
    ### 📊 STATUS CHECK
    [HP/Shield esatti in base ai colori, Mats economy, Loadout]
    
    ### ⚠️ LETTURA DELL'AZIONE (Macro & Micro)
    [Spiega cosa è successo in questa sequenza temporale. Valuta posizionamento, crosshair placement, esposizione ai nemici e reattività.]
    
    ### 🎯 NEXT PLAY (Azione Immediata)
    [Istruzione imperativa su cosa il giocatore deve fare nel frame immediatamente successivo per salvarsi o vincere il fight.]
    """
    
    # 5. Passiamo TUTTE le immagini più il testo al modello
    response = client.models.generate_content(
        model='gemini-3.8-flash',
        contents=immagini + [prompt]
    )
    
    print("\n--- RISPOSTA DEL COACH ---")
    print(response.text)
else:
    print("Nessun frame trovato. Avvia prima 'cattura.py'!")