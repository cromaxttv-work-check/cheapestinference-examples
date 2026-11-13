# CheapestInference API Examples

Esempi pronti all'uso per chiamare le API di [CheapestInference](https://cheapestinference.com) (API illimitata a prezzo fisso mensile, compatibile OpenAI e Anthropic).

## Requisiti

1. Crea un account su [cheapestinference.com](https://cheapestinference.com)
2. Abbonati a un **pool** (Core / Frontier / Flagship) e prenota le fasce orarie
3. Crea una API Key dalla dashboard
4. Copia la key e mettila nel file `.env` (vedi sotto)

## Setup rapido

```bash
# Clona il repo
git clone https://github.com/cromaxttv-work-check/cheapestinference-examples.git
cd cheapestinference-examples

# Copia il file di esempio e inserisci la tua API key
cp .env.example .env
# poi modifica .env e metti la tua key

# (opzionale) installa le dipendenze Python
pip install -r requirements.txt
```

## File presenti

| File | Descrizione |
|------|-------------|
| `python_openai.py` | Esempio completo con OpenAI SDK (Python) |
| `python_anthropic.py` | Esempio con Anthropic SDK (Python) |
| `node_openai.js` | Esempio con OpenAI SDK (Node.js) |
| `curl_examples.sh` | Comandi curl pronti |
| `.env.example` | Template per la API key |
| `requirements.txt` | Dipendenze Python |

## Model ID disponibili (esempi)

- **Frontier Pool**: `glm-5.3`, `minimax-m3`
- **Core Pool**: `deepseek-v4.1-flash`, `mimo-v2.6-flash`
- **Flagship Pool**: `kimi-k3.1-pro`, `qwen3.8-max`

> Controlla sempre la lista aggiornata con:
> ```bash
> curl https://api.cheapestinference.com/v1/models -H "Authorization: Bearer $CHEAPESTINFERENCE_API_KEY"
> ```

## Base URL

- OpenAI-compatible: `https://api.cheapestinference.com/v1`
- Anthropic-compatible: `https://api.cheapestinference.com/anthropic`

## Note importanti

- Durante le ore prenotate hai **utilizzo illimitato** (niente conteggio token)
- Ogni API key gestisce **una richiesta alla volta**
- Fuori dalle fasce orarie le richieste vengono rifiutate

Documentazione ufficiale: https://cheapestinference.com/docs
