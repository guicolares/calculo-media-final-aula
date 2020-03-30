
def calculateN1(a1, a2, a3): 
    return (a1 + a2 + a3) / 3;

print("Cálculo Média Final Uniritter. By Guilherme Leite Colares")

n1a1 = float(input("Informe N1:A1 : "))
n1a2 = float(input("Informe N1:A2 : "))
n1a3 = float(input("Informe N1:A3 : "))
n2a1 = float(input("Informe N1:A1 : "))

N1 = calculateN1(n1a1, n1a2, n1a3);
avgFinalNote = (N1 * 0.4) + (n2a1 * 0.6)
avgFormat = "{:.2f}".format(avgFinalNote)
print("Nota Final:",avgFormat )

