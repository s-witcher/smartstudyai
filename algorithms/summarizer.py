def generate_summary(llm, text: str, max_words: int = 200) -> str:
    """
    Summarize the given research paper text.
    """
    prompt = f"Summarize the following research paper in under {max_words} words:\n\n{text}"
    return llm.generate(prompt)
