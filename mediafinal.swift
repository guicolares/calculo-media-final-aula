import Foundation

func calculateN1(A1: Double, A2: Double, A3: Double) -> Double {
    return (A1 + A2 + A3) / 3
}

let N2 = 10.0 // only a value
let N1 = calculateN1(A1: 6, A2: 7, A3: 8);

let avgFinalNote = (N1 * 0.4) + (N2 * 0.6)

let formatedValue = String(format: "%.2f", avgFinalNote)
print("##Algoritmo Avaliação em Swift###")
print("##Nota final  ###")
print(formatedValue)
