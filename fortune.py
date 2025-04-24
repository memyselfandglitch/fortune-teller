# fortune.py - v1.0

print("🔮 Welcome to Deveshi Singh's Fortune Teller (21JE0304) 🔮")
mood = input("How are you feeling today? (happy/sad/neutral): ")

if mood.lower() == "happy":
    print("✨ Your fortune: Great things await you, Deveshi! Keep smiling. ✨")
elif mood.lower() == "sad":
    print("💧 Your fortune: Tough times don't last. You're stronger than you know.")
elif mood.lower() == "neutral":
    print("🔔 Your fortune: Today is a blank page. Write a great story.")
else:
    print("🤔 Mood not recognized. But something magical is coming your way!")
