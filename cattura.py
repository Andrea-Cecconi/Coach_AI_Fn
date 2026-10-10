import mss
import mss.tools
import keyboard
import time
import os
import shutil  # 1. Aggiungi questa libreria

# 1. Creiamo una cartella dove salvare temporaneamente i frame del replay
cartella_output = "replay_frames"
if not os.path.exists(cartella_output):
    os.makedirs(cartella_output)

# Variabili globali per gestire lo stato
is_recording = False
frame_count = 0

# 2. Funzione che fa da interruttore (Start/Stop)
def toggle_recording():
    global is_recording
    is_recording = not is_recording
    stato = "INIZIATA" if is_recording else "IN PAUSA"
    print(f"\n--- Registrazione {stato} ---")

# 3. Mappiamo il tasto (che puoi attivare dal paddle del controller)
tasto_attivazione = 'f9'
keyboard.add_hotkey(tasto_attivazione, toggle_recording)

print(f"Premi '{tasto_attivazione}' per avviare/fermare la cattura.")
print("Premi 'ESC' per chiudere il programma.")

# 4. Avviamo il motore di cattura mss
with mss.MSS() as sct:
    # Seleziona il monitor principale (1). Lo 0 li cattura tutti se ne hai più di uno.
    monitor = sct.monitors[1] 
    
    while True:
        # Tasto di sicurezza per chiudere tutto
        if keyboard.is_pressed('esc'):
            print("Uscita dal coach...")
            break
            
        if is_recording:
            # Cattura i pixel dello schermo
            sct_img = sct.grab(monitor)
            
            # Salva l'immagine nella cartella
            filename = f"{cartella_output}/frame_{frame_count:04d}.png"
            mss.tools.to_png(sct_img.rgb, sct_img.size, output=filename)
            
            print(f"Screenshot salvato: {filename}")
            frame_count += 1
            
            # Aspetta 2 secondi prima del prossimo screen 
            # (ideale per dare tempo all'AI di analizzare senza intasarla di dati)
            time.sleep(2)
        else:
            # Una piccolissima pausa per non mandare la CPU al 100% mentre il ciclo While gira a vuoto
            time.sleep(0.1)

# 2. Questo blocco viene eseguito solo DOPO che il "break" ha rotto il ciclo While
print("Pulizia dei frame temporanei in corso...")
if os.path.exists(cartella_output):
    shutil.rmtree(cartella_output)  # Elimina la cartella e tutto il suo contenuto
print("Pulizia completata. Sessione chiusa.")