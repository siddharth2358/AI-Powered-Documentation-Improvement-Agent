import textstat

def evaluate_readability(text):
    score = textstat.flesch_kincaid_grade(text)
    explanation = "Good readability" if score < 10 else "Consider simplifying complex sentences for better accessibility."
    return f"Flesch-Kincaid Grade: {score:.2f} — {explanation}"

if __name__ == "__main__":
    sample_text = input("Enter a text sample to analyze readability:\n")
    print(evaluate_readability(sample_text))
