from agents.analyzer_agent import analyze_documentation
from utils.fetcher import extract_text_from_html

def main():
    html_path = "article.html"  # local HTML file saved from browser
    try:
        with open(html_path, "r", encoding="utf-8") as file:
            html = file.read()
    except FileNotFoundError:
        print(f"❌ File '{html_path}' not found. Please save an article as 'article.html' in this folder.")
        return

    url = "Local File: article.html"
    print(f"Analyzing documentation from: {url}")
    report = analyze_documentation(url, html)
    
    # Save report
    with open("analysis_report.md", "w", encoding="utf-8") as f:
        f.write(report)

    print("✅ Analysis complete! See 'analysis_report.md' for the report.")

if __name__ == "__main__":
    main()
