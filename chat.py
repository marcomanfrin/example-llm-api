"""Chat TUI *stateless*: ogni domanda è indipendente, il modello non ricorda nulla."""
import os

from agno.agent import Agent
from agno.models.openrouter import OpenRouter
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ["OPENROUTER_API_KEY"]
MODEL = os.getenv("OPENROUTER_MODEL", "openai/gpt-4o-mini")


def ask(question: str) -> str:
    # Nuovo agente a ogni domanda: nessuna memoria, nessuna cronologia.
    agent = Agent(model=OpenRouter(id=MODEL, api_key=API_KEY))
    return agent.run(question).content


def main() -> None:
    print(f"Chat stateless con {MODEL}  (Ctrl+C o 'exit' per uscire)\n")
    while True:
        try:
            question = input("Tu > ").strip()
        except (KeyboardInterrupt, EOFError):
            break
        if question.lower() in {"exit", "quit"}:
            break
        if question:
            print(f"LLM > {ask(question)}\n")
    print("\nCiao!")


if __name__ == "__main__":
    main()
