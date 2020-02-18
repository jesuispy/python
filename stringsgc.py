
#find position of character in string
explore = "supermanidnotanxman"
print(explore.index("x"))

#Fill in the gaps in the initials function so that it returns the initials of the words contained in the phrase received, in upper case. For example: "Universal Serial Bus" should return "USB"; "local area network" should return "LAN”. 
def initials(phrase):
    words = phrase.___
    result = ""
    for word in words:
        result += ___
    return ___

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS
