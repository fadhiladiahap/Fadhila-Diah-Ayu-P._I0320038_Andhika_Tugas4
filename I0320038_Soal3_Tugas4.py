# Input beban bagasi maksimal
bebanmaks_lbs = 50
bebanmaks_kg = bebanmaks_lbs * 0.453592
beban110 = 110
beban49 = 49

# Seleksi beban 1 = 110 kg
seleksibeban1 = bebanmaks_kg > beban110
print(seleksibeban1)

# Seleksi beban 2 = 49 kg
seleksibeban2 = bebanmaks_kg > beban49
print(seleksibeban2)






