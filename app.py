from src.utils import read_text, save_summary
from src.summarizer import summarize

def main():
    input_file = "data/sample_texts/example1.txt"
    output_file = "data/output/summary1.txt"

    text = read_text(input_file)
    summary = summarize(text)
    save_summary(summary, output_file)

    print("Summary generated successfully! Check:", output_file)

if __name__ == "__main__":
    main()
