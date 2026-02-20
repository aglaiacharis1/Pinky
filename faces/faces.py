def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

def main():
    user_input = input("Please enter something with emoji: ")
    result = convert(user_input)
    print(result)

main()
