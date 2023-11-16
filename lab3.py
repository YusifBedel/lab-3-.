def sütun_hesabla(matris):
    n = len(matris)
    m = len(matris[0])
    
    sütun_hesabları = []
    
    for j in range(m):
        sütun_hesabı = 1
        for i in range(n):
            sütun_hesabı *= matris[i][j]
        sütun_hesabları.append(sütun_hesabı)
    
    return sütun_hesabları

# Örnək bir matris yaradırıq
matris = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Hər sütunun elementlərinin hasilini hesablaırıq
cavablar = sütun_hesabla(matris)

# Cavabları yazdırırıq
for i, cavab in enumerate(cavablar):
    print(f"Sütun {i+1} hasili: {cavab}")