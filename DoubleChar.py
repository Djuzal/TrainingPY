def dna_to_rna(dna):
    rna = ""
    array_dna = []
    for item in dna:
        array_dna.append(item)
    lenght = len(array_dna)
    for symbol_num in range(lenght):
        if array_dna[symbol_num] == "T":
            array_dna[symbol_num] = "U"
        else:
            continue
    for symbol in array_dna:
        rna = rna + symbol
    return rna
print (dna_to_rna("TTTT"))

            