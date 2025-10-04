from ingestion.file_ingestion import ingest_file
from algorithms.summarizer import generate_summary
from algorithms.quiz_generator import generate_quiz
from algorithms.flashcard_creator import generate_flashcards
from providers.llm_providers import DOAIProvider
# from providers.doai_provider import DOAIProvider as llm_providers

def main():
    print("=== SmartStudyAI ===")
    file_path = input("Enter path to research paper (.pdf or .txt): ").strip()
    task = input("Choose task (summary/quiz/flashcards): ").strip().lower()

    print("\nProcessing file...")
    text = ingest_file(file_path)
    llm = DOAIProvider()

    if task == "summary":
        result = generate_summary(llm, text)
    elif task == "quiz":
        result = generate_quiz(llm, text)
    elif task == "flashcards":
        result = generate_flashcards(llm, text)
    else:
        print("Invalid choice.")
        return

    print("\n=== Result ===")
    print(result)

if __name__ == "__main__":
    main()
