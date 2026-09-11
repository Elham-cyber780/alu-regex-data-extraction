import re
import json
#checks if the phonenumber/card is accurate by flagging a number that doesn't contain different digits 
def is_placeholder(number_string):
    digits_only = re.sub(r"[^\d]", "", number_string)
    unique_digits = set(digits_only)
    if len(unique_digits) == 1:
        return True
    else:
        return False
#Only showas the last four digits of the card number to protect the card user's privacy 
def mask_card(number_string):
        digits_only = re.sub(r"[^\d]", "", number_string)
        last4 = digits_only[-4:]
        masked = "**** **** **** " + last4
        return masked
    
with open("../input/raw-text.txt", "r") as file:
    content = file.read()
print(content)
pattern = r"#[a-zA-Z]+"
matches = re.findall(pattern, content)
print(matches)  
pattern_local = r"\b0\d{9}\b"
matches_local = re.findall(pattern_local, content)
print(matches_local)  
pattern_intl = r"\+250-?\d{3}-?\d{3}-?\d{4}"
matches_intl = re.findall(pattern_intl, content)
print(matches_intl)
pattern_card = r"\d{4}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4}"
matches_card = re.findall(pattern_card, content)
print(matches_card)
# Separate detected card numbers into safe (masked) and rejected (fake/placeholder) lists
safe_cards = []
rejected_cards = []

for card in matches_card:
    if is_placeholder(card):
        rejected_cards.append(card)
    else:
        safe_cards.append(mask_card(card))

print("Safe cards:", safe_cards)
print("Rejected cards:", rejected_cards)
#catches potential script injection attempts in a raw text whether it is in upper or lower case letters and flags it as a security concern
pattern_script = r"<script"
matches_script = re.findall(pattern_script, content, re.IGNORECASE)
print(matches_script)
security_flags = []

if matches_script:
    security_flags.append("Script tag detected in input")
    print("⚠️ Suspicious content detected and flagged")
pattern_email = r"[a-zA-Z0-9.]+[a-zA-Z0-9.]+@[a-zA-Z]+\.[a-zA-Z]+"
matches_email = re.findall(pattern_email, content)
print(matches_email)
pattern_alumni = r"[a-zA-Z0-9.]+@alumni\.alueducation\.com" 
matches_alumni = re.findall(pattern_alumni, content)
print(matches_alumni)
pattern_si = r"[a-zA-Z0-9.]+@si\.alueducation\.com"
matches_si = re.findall(pattern_si, content )
print(matches_si)
pattern_official = r"[a-zA-Z0-9.]+@alueducation\.com"
matches_official = re.findall(pattern_official, content)
print(matches_official)
# Combine all validated and extracted results into one organized dictionary, and save it as a structured JSON output file for easy verification
results = {
    "hashtags": matches,
    "phones_local": matches_local,
    "phones_intl": matches_intl,
    "cards_safe": safe_cards,
    "cards_rejected": rejected_cards,
    "emails_general": matches_email,
    "emails_alumni": matches_alumni,
    "emails_si": matches_si,
    "emails_official": matches_official,
    "security_flags": security_flags
}
print(results)
with open("../output/sample-output.json", "w") as outfile:
    json.dump(results, outfile)
