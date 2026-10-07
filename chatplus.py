"""Chat TUI *con contesto*: a ogni domanda viene reinviata tutta la conversazione precedente."""
import os

from agno.agent import Agent
from agno.db.in_memory import InMemoryDb
from agno.models.openrouter import OpenRouter
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ["OPENROUTER_API_KEY"]
MODEL = os.getenv("OPENROUTER_MODEL", "openai/gpt-4o-mini")


def main() -> None:
    # Un solo agente per tutta la sessione: la cronologia è salvata in memoria
    # e rimandata al modello a ogni richiesta (il modello resta stateless!).
    agent = Agent(
        model=OpenRouter(id=MODEL, api_key=API_KEY),
        db=InMemoryDb(),
        add_history_to_context=True,
        num_history_runs=50,
    )

    print(f"Chat con contesto con {MODEL}  (Ctrl+C o 'exit' per uscire)\n")
    while True:
        try:
            question = input("Tu > ").strip()
        except (KeyboardInterrupt, EOFError):
            break
        if question.lower() in {"exit", "quit"}:
            break
        if question:
            print(f"LLM > {agent.run(question).content}\n")
    print("\nCiao!")


if __name__ == "__main__":
    main()
