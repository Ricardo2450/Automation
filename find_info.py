import re



#context manager
with open("./potential-contacts.txt", "r") as f:
    # we do logic and stuff with the file f
    text_from_file = f.read()

#print(text_from_file)

# Same pattern as before:
phone_pattern = r'\b(?:\+?1[-. ]?)?\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})|([0-9]{7})\b$'
email_pattern = r"[\w.+-]+@[\w-]+\.[\w.-]+"

# re.findall() returns a list of matches
phone_nums = set(re.findall(phone_pattern, text_from_file))
email_address = set(re.findall(email_pattern, text_from_file))

# re.search() searches the entire string but stops after the first
#soc_sec_nums = re.search(pattern, text_from_file).group()

# re.match() only looks at the beginning of the string
#soc_sec_nums = re.match(pattern, text_from_file).group()



print(phone_nums)
print(email_address)

phone_nums = sorted(phone_nums)
email_addy = sorted(email_address)

new_phone_list = ['{}-{}-{}'.format(number[0], number[1], number[2]) for number in phone_nums]

with open("new_emails.txt", "w") as f:
    for emails in email_addy:
        f.write(emails + "\n")

with open("new_contacts.txt", "w") as f:
    for numbers in new_phone_list:
        f.write(numbers + "\n")

#assert len(phone_nums) == 10

print(f"THis is the length of phones we found: {len(phone_nums)}")
print(f"This is the length of email address {len(email_address)}")