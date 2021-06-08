import random
import requests
import time

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
code = ""

def check(r):
    json = r.json()

    if json["message"] == "Unknown Gift Code" or json["message"] == "You are being rate limited.":
        return False
    else:
        return True

def generatecode():
    generated = code

    length = random.randint(3, 5)

    for i in range(0, 4):
        for i in range(0, length):
            is_number = False
            is_lower  = False
            number    = random.randint(0, 4)

            if number == 2:
                is_number = True

            if number == 3:
                is_lower = True

            if is_number:
                generated = generated + random.choice(numbers)
            elif is_lower:
                generated = generated + random.choice(alphabet)
            else:
                generated = generated + random.choice(alphabet).upper()

        generated = generated + "-"

    generated = generated[0:len(generated) - 1]

    return generated

def main():
    while True:
        code = generatecode()
        r = requests.get("https://discord.com/api/v8/entitlements/gift-codes/" + code)

        if check(r) == True:
            print("VALID CODE FOUND: '" + code + "'")
            
            file = open("tried.txt", "a")

            file.write(code + "\tVALID" + "\n")

            file.close()

            return

        file = open("tried.txt", "a")

        file.write(code + "\tINVALID" + "\n")

        file.close()

        time.sleep(3)

main()
