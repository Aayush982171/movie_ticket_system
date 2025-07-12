print("╔════════════════════════════════════════════════════════╗")
print("║               🎬 MOVIE TICKET SYSTEM 🎟️              ║")
print("║════════════════════════════════════════════════════════║")
print("║           Created by : Aayush Singh 💻                ║")
print("║                 From : Nepal 🇳🇵                      ║")
print("╚════════════════════════════════════════════════════════╝")

user = int(input("\n👉 Enter your age: "))

if user < 1:
    print("⚠️ Please enter a valid age above 0.")
elif user >= 1 and user < 5:
    print("✅ Free Ticket —", user, "years old little kid 👶")
elif user >= 5 and user <= 12:
    print("🎫 Child Ticket —", user, "years old — Price: रू100")
elif user >= 13 and user <= 59:
    print("🎫 Adult Ticket —", user, "years old — Price: रू200")
elif user >= 60 and user <= 90:
    print("🎫 Senior Citizen Ticket —", user, "years old — Price: रू120")
else:
    print("❌ Sorry, age limit exceeded. You can't enter the cinema hall.")

print("\n🎉 Thank you for visiting! Enjoy your movie! 🍿")
