import requests

def get_definition(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"\n📚 Definitions for '{word}':\n")
        for meaning in data[0]["meanings"]:
            part_of_speech = meaning["partOfSpeech"]
            print(f"• Part of Speech: {part_of_speech}")
            for i, definition in enumerate(meaning["definitions"], 1):
                print(f"  {i}. {definition['definition']}")
                if "example" in definition:
                    print(f"     👉 Example: {definition['example']}")
            print()
    else:
        print(f"\n❌ Sorry, no definitions found for '{word}'. Please check the spelling.")

def main():
    print("📖 Welcome to the Dictionary CLI App")
    while True:
        word = input("\nEnter a word (or type 'exit' to quit): ").strip()
        if word.lower() == 'exit':
            print("👋 Goodbye!")
            break
        elif word == '':
            print("⚠️ Please enter a valid word.")
        else:
            get_definition(word)

if __name__ == "__main__":
    main()
