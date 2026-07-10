import random
import string

# Random password generator
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(length))

# Random motivational quote
quotes = [
    "Keep going. Great things take time.",
    "Success starts with believing in yourself.",
    "Every day is a new opportunity.",
    "Small progress is still progress.",
    "Never stop learning."
]

print("=" * 40)
print("🎲 Random Generator")
print("=" * 40)

print(f"🎯 Lucky Number: {random.randint(1, 100)}")
print(f"🔑 Random Password: {generate_password()}")
print(f"💬 Quote: {random.choice(quotes)}")

colors = ["Red", "Blue", "Green", "Black", "White"]
print(f"🎨 Random Color: {random.choice(colors)}")

print("=" * 40)
print("Have a great day! 😊")
