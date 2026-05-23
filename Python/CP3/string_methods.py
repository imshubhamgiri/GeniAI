letter = "harry is a gonner"
# strings are immutable, which means you cannot change them after they have been created. However, you can create a new string by replacing parts of the original string.
print(letter.replace("harry", "alok"))

print(letter.replace("is", "was"))

print(letter.replace("gonner", "winner").replace("is", "was").replace("winner", "IITIAN"))