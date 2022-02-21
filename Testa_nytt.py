t4 = "jag har \u03c0 och \u2654  en kung"
print(t4) 

while True:
    text = input("Skriv vad som? ")
    if text[0] == text[-1]:
        print("Ditt första och ditt sista tecken är likadana")
        break
    else:
        print("Skriv någonting till,tips skriv nånting med samma start och slut bokstav")

