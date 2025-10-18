import random

# Step 1: List of predefined words
words = ["apple", "banana", "orange", "grapes", "mango"]

# Step 2: Randomly choose one word
word = random.choice(words)
guessed_letters = []  # To store guessed letters
attempts = 6          # Limit of incorrect guesses

print("🎯 Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("_ " * len(word))  # Display blanks for the word

# Step 3: Game loop
while attempts > 0:
    guess = input("\nEnter a letter: ").lower()

    # Validation: Check if input is a single alphabet
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter only one letter.")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You've already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Step 4: Check if guess is in word
    if guess in word:
        print("✅ Good guess!")
    else:
        attempts -= 1
        print(f"❌ Wrong guess! Attempts left: {attempts}")

    # Step 5: Display current progress
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("\n" + display_word)

    # Step 6: Check if the word is fully guessed
    if all(letter in guessed_letters for letter in word):
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

# Step 7: If player runs out of attempts
if attempts == 0:
    print("\n😞 Game Over! The word was:", word)
