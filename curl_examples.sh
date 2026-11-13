#!/bin/bash
# Esempi curl per CheapestInference
# Uso: esporta prima la key
#   export CHEAPESTINFERENCE_API_KEY=sk-xxxxxxxx

set -e

if [ -z "$CHEAPESTINFERENCE_API_KEY" ]; then
  echo "Errore: imposta la variabile CHEAPESTINFERENCE_API_KEY"
  exit 1
fi

BASE_URL="https://api.cheapestinference.com/v1"

echo "=== Lista modelli ==="
curl -s "$BASE_URL/models" \
  -H "Authorization: Bearer $CHEAPESTINFERENCE_API_KEY" | jq .

echo -e "\n=== Chat completion ==="
curl -s "$BASE_URL/chat/completions" \
  -H "Authorization: Bearer $CHEAPESTINFERENCE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "glm-5.3",
    "messages": [
      {"role": "user", "content": "Ciao! Dimmi una curiosità sul cielo."}
    ]
  }' | jq .
