#!/usr/bin/env node
/**
 * Esempio CheapestInference con OpenAI SDK (Node.js)
 *
 * Installazione:
 *   npm install openai dotenv
 */

import OpenAI from "openai";
import dotenv from "dotenv";

dotenv.config();

const apiKey = process.env.CHEAPESTINFERENCE_API_KEY;
if (!apiKey) {
  throw new Error("Imposta CHEAPESTINFERENCE_API_KEY nel file .env");
}

const client = new OpenAI({
  apiKey,
  baseURL: "https://api.cheapestinference.com/v1",
});

async function chat(prompt, model = "glm-5.3") {
  const response = await client.chat.completions.create({
    model,
    messages: [
      { role: "system", content: "Sei un assistente utile e conciso." },
      { role: "user", content: prompt },
    ],
    temperature: 0.7,
  });
  return response.choices[0].message.content;
}

async function main() {
  console.log("=== CheapestInference - OpenAI SDK (Node) ===\n");

  const risposta = await chat("Spiega in due frasi cos'è un LLM.");
  console.log("Risposta:");
  console.log(risposta);
}

main().catch(console.error);
