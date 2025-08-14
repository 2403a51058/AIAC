import re

def extract_urls(text):
    # Regex pattern to match http, https, and www URLs
    url_pattern = re.compile(
        r'(https?://[^\s]+|www\.[^\s]+)',
        re.IGNORECASE
    )
    return url_pattern.findall(text)

if __name__ == "__main__":
    sample_text = input("Enter text: ")
    urls = extract_urls(sample_text)
    print("Extracted URLs:")
    for url in urls:
        print(url)
