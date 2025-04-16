# fortune.py

def main():
    print("🔮 Welcome to Deveshi Singh's Fortune Teller (21JE0304) 🔮")
    mood = input("How are you feeling today? (happy/sad/neutral): ").strip().lower()

    if mood == "happy":
        print("✨ Your fortune: Great things await you, Deveshi! Keep smiling. ✨")
    elif mood == "sad":
        print("🌧️ Your fortune: Storms don't last forever. Better days are coming. 🌈")
    elif mood == "neutral":
        print("🌀 Your fortune: Balance is the key. Stay steady and enjoy the calm. 🧘")
    else:
        print("🤔 I couldn't read your mood. Try again with happy/sad/neutral!")

if __name__ == "__main__":
    main()
