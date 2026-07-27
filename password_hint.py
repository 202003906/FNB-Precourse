password = input("Enter your secret password: ")
clean_password = password.strip()
first_letter = clean_password[0]
last_letter = clean_password[-1]
print(f"Your password hint: It starts with {first_letter.upper()} and ends with {last_letter.upper()}")