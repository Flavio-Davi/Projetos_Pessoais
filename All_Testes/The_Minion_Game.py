# Ambos os jogadores recebem a mesma sequência, .
# Ambos os jogadores têm que fazer substrings usando as letras da string .
# Stuart tem que fazer palavras começando com consoantes.
# Kevin tem que fazer palavras começando com vogais.

Kevin = 0
Stuart = 0
VOGAIS = "AEIOU"
CONSOANTES = "BCDFGHJKLMNPQRSTVWXYZ"

var_consoantes = []
var_vogais = []
unic_consoante = []
unic_vogal = []

home = "BANANA"
var_temporaria = ""

for i, d in enumerate(home):
    if d in VOGAIS and d not in var_vogais:
          unic_vogal.append(i)
          var_vogais.append(d)
    elif d in CONSOANTES and d not in var_consoantes:
          unic_consoante.append(i)
          var_consoantes.append(d)
var_vogais.clear()
var_consoantes.clear()

for c in range(len(unic_vogal)):
    for d in home[unic_vogal[c]::]:
        var_temporaria += d
        if var_temporaria not in var_vogais:
            var_vogais.append(var_temporaria)

for c in range(len(unic_consoante)):
    var_temporaria = ""
    for d in home[unic_consoante[c]::]:
        var_temporaria += d
        if var_temporaria not in var_consoantes:
            var_consoantes.append(var_temporaria)

print(f"{var_vogais}\n{var_consoantes}")
