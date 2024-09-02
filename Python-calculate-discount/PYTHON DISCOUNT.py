# atur cara bagi mengira jumlah diskaun dan pembelian

# pengisytiharan pemboleh ubah dan pemalar
# input
jum_pembelian = float(input("Masukkan jumlah pembelian: RM "))

# tentukan jumlah pembelian
# proses
if  jum_pembelian <= 99:
    print("\nDiskaun ialah 0%")
    diskaun = 0.00
    jum_diskaun = jum_pembelian * diskaun
    print("\nJumlah diskaun: RM", round(jum_diskaun))
    
elif jum_pembelian >= 400:
    print("\nDiskaun ialah 25%")
    diskaun = 0.25
    jum_diskaun = jum_pembelian * diskaun
    print("\nJumlah diskaun: RM", round(jum_diskaun))
    
elif jum_pembelian >= 301:
    print("\nDiskaun ialah 20%")
    diskaun = 0.20
    jum_diskaun = jum_pembelian * diskaun
    print("\nJumlah diskaun: RM", round(jum_diskaun))
    
elif jum_pembelian >= 201:
    print("\nDiskaun ialah 15%")
    diskaun = 0.15
    jum_diskaun = jum_pembelian * diskaun
    print("\nJumlah diskaun: RM", round(jum_diskaun))
    
elif jum_pembelian >= 100:
    print("\nDiskaun ialah 10%")
    diskaun = 0.10
    jum_diskaun = jum_pembelian * diskaun
    print("\nJumlah diskaun: RM", round(jum_diskaun))
    
    
jum_pembelian = jum_pembelian - jum_diskaun

# output
print("Jumlah selepas diskaun: RM", round(jum_pembelian,2))

if jum_pembelian >= 300:
    print("Anda juga layak menerima sampul duit raya")
    
