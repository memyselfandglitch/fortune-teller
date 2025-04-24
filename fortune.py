# fortune.py - v1.1

import random

print("🔮 Welcome to Deveshi Singh's Fortune Teller (21JE0304) 🔮")
mood = input("How are you feeling today? (happy/sad/neutral/stressed): ")

fortunes = {
    "happy": [
        "Great things await you, Deveshi! Keep smiling.",
        "Your joy is contagious! The world is brighter with you in it.",
    ],
    "sad": [
        "Storms don’t last forever. Light is on the way.",
        "You’re stronger than you think. Keep moving forward.",
    ],
    "neutral": [
        "Balance is a gift. Use today to plan something great.",
        "Sometimes, calm days bring the biggest breakthroughs.",
    ],
    "stressed": [
        "Take a deep breath. Peace begins with you.",
        "Even storms have silver linings. Keep going, Deveshi!",
    ]
}

if mood.lower() in fortunes:
    print("✨ Your fortune:", random.choice(fortunes[mood.lower()]), "✨")
else:
    print("🤔 Mood not recognized. But a surprise is coming your way!")
