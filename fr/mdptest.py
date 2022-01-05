def checkPwd(pwd):
    res = []
    res.append(True)
    special_characters = "\"!@#$%^&*()-+?_=,<>/'"
    blocked = ["qwertyuiop", "azertyuiop", "123456789", "password", "abcdefg"]

    if not(10 <= len(pwd) <= 25):
        res.append({"type": "len", "message": "la longueur doit être comprise entre 10 et 25"})
        res[0] = False

    if not(any(c for c in pwd if c.isdigit())):
        res.append({"type": "digit", "message": "Doit contenir des chiffres"})
        res[0] = False

    if not(any(c in special_characters for c in pwd)):
        res.append({"type": "special", "message": "Doit contenir des caractères spéciaux"})
        res[0] = False

    if not(any(c for c in pwd if c.isupper())):
        res.append({"type": "upper", "message": "Doit contenir une majuscule"})
        res[0] = False

    if not(any(c for c in pwd if c.islower())):
        res.append({"type": "lower", "message": "Doit contenir une minuscule"})
        res[0] = False

    if any(word for word in blocked if word in pwd):
        res.append({"type": "common", "message": "Trop commun"})
        res[0] = False

    return res


if __name__ == '__main__':
    mdp = input(f"Saisir un mot de passe : ")
    print(checkPwd(mdp))
