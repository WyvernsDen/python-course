from stripaccents import strip_accents

text = strip_accents(str.lower(input("Type in some text: ")))
consonants = ""

for char in text:
    if char not in "aeiou":
        consonants = consonants + char
print(consonants)