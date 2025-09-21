import requests

def get_definition(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    
    try:
        response = requests.get(url, timeout=5)

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
        elif response.status_code == 404:
            print(f"\n❌ No definitions found for '{word}'. Please check the spelling.")
        else:
            print(f"\n⚠️ Error: Received unexpected status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"\n🚫 Network error occurred: {e}")


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
