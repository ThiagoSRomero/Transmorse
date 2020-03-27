def transmorse():
    wrd = input('Digite uma palavra: ')
    wrd = wrd.lower()
    morse = {'a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.','f':'..-.','g':'--.','h':'....','i':'..','j':'.---','k':'-.-','l':'.-..','m':'--','n':'-.','o':'---','p':'.--.','q':'--.-','r':'.-.','s':'...','t':'-','u':'..-','v':'...-','w':'.--','x':'-..-','y':'-.--','z':'--..'}
    a = len(wrd)
    c = [];
    lista = []
    for i in range(a):
        b = str(wrd[i])
        c.append(morse[b])
    print("|".join(c))

transmorse()
