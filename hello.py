def hello(to):
    print("hello,", to)

name = input("Whats your name? ").strip().title()

hello(name)

print(f"hello, {name}")
