import random
import string
import math

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def calculate_entropy(password):
    char_set = string.ascii_letters + string.digits + string.punctuation
    complexity = len(char_set)
    entropy = len(password) * math.log2(complexity)
    return entropy

def crackable(entropy):
    attempts_per_second = 10**10
    total_attempts = 2**entropy
    time_seconds = total_attempts / attempts_per_second
    return time_seconds

def format_time(seconds):
    units = [("year", 60 * 60 * 24 * 365), ("month", 60 * 60 * 24 * 30), ("day", 60 * 60 * 24), ("hour", 60 * 60), ("minute", 60), ("second", 1)]
    result = []

    for unit_name, unit_duration in units:
        if seconds >= unit_duration:
            unit_value = int(seconds // unit_duration)
            seconds %= unit_duration
            result.append(f"{unit_value} {unit_name + ('s' if unit_value > 1 else '')}")

    return ", ".join(result)

if __name__ == '__main__':
    while True:
        try:
            length = int(input("Enter the desired password length (minimum 8 characters): "))
            if length < 8:
            
                raise ValueError("Password length must be at least 8 characters.")
            break
        except ValueError as e:
            print(e)

    password = generate_password(length)
    entropy = calculate_entropy(password)
    timeToBrute = crackable(entropy)

    print(f"Generated password: {password}")
    print(f"Password entropy: {entropy:.2f} bits")
    print(f"Approximate time to brute force: {format_time(timeToBrute)}")
    print(f"Bear in mind, the time to brute force is based on your password being unique, never breached, and *modest* processing power.")
    print(f"Advanced in Quantum Computing may dramatically change this.")
