#!/usr/bin/env python

import sys
from datetime import datetime

user_data = {}


def greet() -> None:
    current_hour = datetime.now().hour
    if 5 <= current_hour < 12:
        greeting = "Good morning"
    elif 12 <= current_hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"
    if 'name' in user_data:
        print(f"{greeting}, {user_data.get("name")}! How can I assist you today?")
    else:
        print(f"{greeting}! I see we haven't met before, have we? What's your name?")
        ask()


def ask() -> None:
    user_name = input("Enter your name: ").title().split()
    if user_name:
        user_data['name'] = user_name
        print("Nice to meet you, {0}!".format(user_name[0]))
    else:
        print("Please, enter a valid name.")
        ask()


def main() -> None:
    greet()
    sys.exit()


if __name__ == "__main__":
    main()
