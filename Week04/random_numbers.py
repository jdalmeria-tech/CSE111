import random

def main():
  numbers = [16.2, 75.1, 52.3]
  print(f"numbers {numbers}")

  append_random_numbers(numbers)
  print(f"numbers {numbers}")

  append_random_numbers(numbers, 3)
  print(f"numbers {numbers}")

  words = []
  append_random_words(words)
  print(f"words {words}")

  append_random_words(words, 5)
  print(f"words {words}")

def append_random_numbers(numbers_list, quantity=1):
  for _ in range(quantity):
    random_number = random.uniform(0, 100)
    rounded_number = round(random_number, 1)
    numbers_list.append(rounded_number)

def append_random_words(words_list, quantity=1):
   words_choices = [
      "join", "love", "smile", "happy", "funny", "laptop", "moonlight", "beach", "sunset",
      "walk", "run", "play", "hope", "endure", "language", "truth"
    ]
   for _ in range(quantity):
      random_words = random.choice(words_choices)
      words_list.append(random_words)

# Call main to start this program.
if __name__ == "__main__":
    main()