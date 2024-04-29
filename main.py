"""
Main function
Return 0 if no error
"""

def getFileContent(file: str):
    with open(file, 'r') as f:
        return f.read()

def wordsCount(file_content: str):
    return len(file_content.split())

def charCount(file_content: str, char: str):
    return file_content.count(char)

def main() -> int:
    file = "books/frankenstein.txt"
    char = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    char_count = {}

    file_content = getFileContent(file).lower()
    words_count = wordsCount(file_content)
    for c in char:
        char_count[c] = charCount(file_content, c)

    print(char_count["r"])

    return 0

if __name__ =="__main__":
    main()