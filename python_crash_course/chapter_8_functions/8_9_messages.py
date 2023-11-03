def print_messages(messages):
    while messages:
        current_message = messages.pop()
        print(current_message)

messages = [
    "Some Text",
    "Let's go shopping.",
    "He failed his French test.",
    "Odds are that he is cheating on her.",
]

print_messages(messages=messages[:])