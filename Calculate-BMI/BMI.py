#Pengisytiharab pemboleh ubah dan pemalar
berat = float(input('Masukkan berat anda: '))
tinggi = float(input('Masukkan tiggi anda: '))
BMI = berat / tinggi ** 2
BMI = round(BMI, 1)

#Proses
if BMI <= 18.5:
    keputusan = 'KURANG BERAT BADAN'
elif 18.5 < BMI <= 24.9:
    keputusan = 'NORMAL'
elif 25 < BMI <= 29.9:
    keputusan = 'BERAT BADAN BERLEBIHAN'
elif 30.0 > BMI <= 35.5:
     keputusan = 'OBES 1'
elif 35.5 < BMI <= 40.0:
     keputusan = 'OBES 2'
else:
    BMI > 40.0
    keputusan = 'OBES 3'

#Result
print('BMI anda ialah :', BMI, 'dan anda ialah', keputusan, end='. ')
