duljina = int(input())
shirochina = int(input())
visochina = int(input())
procent_zaetost = float(input())

obem = duljina * shirochina * visochina
obshto_litri = obem * 0.001
procent = procent_zaetost*0.01
result = obshto_litri * (1 - procent)
print (result)