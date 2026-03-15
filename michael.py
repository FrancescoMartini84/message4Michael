import time
import os

verses = [
("Philippians 1:3",
"I thank my God every time I remember you."),

("Job 14:7-9",
"For there is hope for a tree, if it be cut down, that it will sprout again, and that the tender branch thereof will not cease. Though the root thereof wax old in the earth, and the stock thereof die in the ground; Yet through the scent of water it will bud, and bring forth boughs like a plant.")
]

def clear():
    os.system("clear")

def show(index):
    clear()
    ref, text = verses[index]
    print("\n")
    print("📖", ref)
    print("-" * len(ref))
    print(text)
    print("\n[n] next   [p] previous   [q] quit")

index = 0

while True:
    show(index)
    cmd = input("> ").lower()

    if cmd == "n":
        index = (index + 1) % len(verses)

    elif cmd == "p":
        index = (index - 1) % len(verses)

    elif cmd == "q":
        break
