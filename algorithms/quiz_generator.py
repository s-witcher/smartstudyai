def generate_quiz(llm, text: str, num_questions: int = 5) -> str:
    """
    Generate quiz questions based on research paper content.
    """
    prompt = f"Generate {num_questions} multiple-choice quiz questions based on the following text:\n\n{text}"
    return llm.generate(prompt)
