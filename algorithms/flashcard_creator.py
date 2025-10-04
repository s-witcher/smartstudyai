def generate_flashcards(llm, text: str, num_cards: int = 5) -> str:
    """
    Create flashcards (Q&A format) from the text.
    """
    prompt = f"Create {num_cards} flashcards from the following text. Each card should have a question and a concise answer:\n\n{text}"
    return llm.generate(prompt)
