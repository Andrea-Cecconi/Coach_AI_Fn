# 🎮 Fortnite AI Coach 🤖

![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)
![Status](https://img.shields.io/badge/Status-In_Sviluppo-orange.svg)

Un progetto in Python per sviluppare un assistente basato su Intelligenza Artificiale multimodale, in grado di analizzare i replay di Fortnite e fornire un feedback tecnico/tattico di alto livello (macro-game, rotazioni, gestione risorse), simulando l'analisi di un vero coach professionista.

> **⚠️ Epic Games ToS Compliance:** Questo strumento è progettato **esclusivamente per l'analisi dei Replay (VOD Review)**. Non legge la memoria del gioco e non si inietta nei file di gioco. L'analisi esterna post-partita rispetta i Termini di Servizio competitivi.

## 🚀 Obiettivi del Progetto

Il progetto si divide in due fasi principali:
1. **Motore di Acquisizione (Attuale):** Uno script ultra-leggero e a bassa latenza che cattura i frame di gioco senza impattare sugli FPS o sulle prestazioni della CPU/GPU.
2. **Motore di Analisi AI (In sviluppo):** Integrazione con un'API multimodale (Vision) per interpretare l'HUD (materiali, salute, tempesta, loadout) e l'azione a schermo, generando feedback costruttivi per il giocatore.

## ✨ Funzionalità Attuali

- **Cattura a Basso Impatto:** Utilizza la libreria `mss` per l'accesso diretto ai dati del monitor, garantendo velocità ed efficienza.
- **Global Hotkey:** Sistema di toggle (start/stop) azionabile tramite la pressione del tasto `F9` (mappabile sui paddle del controller) tramite la libreria `keyboard`, anche quando il gioco è a schermo intero.
- **Auto-Pulizia Cache:** Alla chiusura del programma (`ESC`), lo script elimina automaticamente la directory temporanea delle immagini per non saturare l'hard disk.
- **Estrazione Dati Cache-Based**: Sistema di screen-capture con gestione autonoma e pulita della I/O directory (`replay_frames`), senza conflitti con Windows o Cloud.
- **Analisi Sequenziale (VOD Review)**: Il bot non legge solo foto singole, ma elabora interi blocchi di frame consecutivi per valutare macro-game, rotazioni e crosshair placement nel tempo.
- **HUD Parsing Avanzato**: Prompt engineering con "ancoraggio visivo" cromatico per eliminare le allucinazioni dell'AI e garantire una lettura impeccabile di Salute (verde) e Scudo (blu).
- **Motore Logico**: Alimentato dall'ultimissimo modello `gemini-3.8-flash` tramite l'SDK ufficiale `google-genai`.

## 🛠️ Installazione e Utilizzo

### Prerequisiti
- Python 3.12 o superiore.
- Sistema operativo Windows.

### Setup rapido

1. Clona il repository:
   ```bash
   git clone https://github.com/Andrea-Cecconi/Coach_AI_Fn.git
   cd Coach_AI_Fn
   ```

2. Crea e attiva un ambiente virtuale (consigliato):
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate
   ```

3. Installa le dipendenze:
   ```bash
   pip install mss keyboard google-genai python-dotenv pillow
   ```

4. Configura le chiavi API:
   - Crea un file `.env` nella cartella principale.
   - Inserisci la tua chiave di Google AI Studio in questo formato: `GEMINI_API_KEY=la_tua_chiave_qui`

### Come avviare la cattura

Avvia lo script principale:
```bash
python cattura.py
```
- Vai su Fortnite e apri un **Replay**.
- Premi `F9` per iniziare la registrazione dei frame.
- Premi di nuovo `F9` per mettere in pausa la registrazione.
- Premi `ESC` per chiudere il programma e pulire automaticamente i frame salvati.

## 🗺️ Roadmap e Sviluppi Futuri

- [x] Modulo di screen capture a bassa latenza (mss + keyboard).
- [x] Gestione intelligente dello storage locale (autoclean).
- [x] Connessione a un'API Multimodale (Google Gemini 3.8 Flash).
- [x] Creazione del System Prompt specializzato nel meta competitivo di Fortnite.
- [ ] Modulo di profilazione utente per consigli sull'ottimizzazione del PC e degli input (Curve Esponenziali/Lineari, Deadzone).
- [ ] Generazione vocale del feedback del coach in tempo reale tramite Text-to-Speech (TTS).

---
*Progetto sviluppato per esplorare le architetture multimodali e l'AI engineering in ambito e-sports.*