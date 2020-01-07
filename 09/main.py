


from password_strength import PasswordPolicy

policy = PasswordPolicy.from_names(
    length=8,  # min length: 8
    uppercase=2,  # need min. 2 uppercase letters
    numbers=2,  # need min. 2 digits
    special=2,  # need min. 2 special characters
    nonletters=2,  # need min. 2 non-letter characters (digits, specials, anything)
)
password = input("Provide a password")
tested_pass = policy.password(password)
print(tested_pass.strength())  # -> 0.812 -- very good!
print(tested_pass.test())