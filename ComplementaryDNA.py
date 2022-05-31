def DNA_strand(dna):
    tableA = "ATCG"
    tableB = "TAGC"
    table = dna.maketrans(tableA, tableB)
    return dna.translate(table)
print(DNA_strand("TAACG"))