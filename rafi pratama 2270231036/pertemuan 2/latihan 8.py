# program konversi celcius ke satuan lain

print("\nPROGRAM KONVERSI TEMPRATUR\n")
celcius = float(input('masukan suhu dalam celcius :'))
print("suhu adalah",celcius,"Celcius")

#reamur
reamur = (4/5) * celcius
print("suhu dalam reamur adalah", reamur,"Reamur")

#farenhit
farenheit = ((9/5) *celcius) + 32
print("suhu dalam farenheit adalah",farenheit,"Farenheit")

#kelvin
kelvin = celcius + 273
print("suhu dalam kelvin adalah",kelvin,"kelvin")