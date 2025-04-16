# fortune.py

import random

def main():
    print("🔮 Welcome to Deveshi Singh's Fortune Teller (21JE0304) 🔮")
    mood = input("How are you feeling today? (happy/sad/neutral/stressed): ").strip().lower()

    fortunes = {
        "happy": [
            "Great things await you, Deveshi! Keep smiling.",
            "Happiness is contagious. Spread it like confetti!"
        ],
        "sad": [
            "Storms don't last forever. Better days are coming.",
            "Tough times never last, but tough people do."
        ],
        "neutral": [
            "Balance is the key. Stay steady and enjoy the calm.",
            "Neutral today, powerful tomorrow!"
        ],
        "stressed": [
            "Take a deep breath. You got this, Deveshi!",
            "Stress is temporary, success is forever."
        ]
    }

    if mood in fortunes:
        print(f"✨ Your fortune: {random.choice(fortunes[mood])} ✨")
    else:
        print("🤔 I couldn't read your mood. Try again with happy/sad/neutral/stressed!")

if __name__ == "__main__":
    main()
