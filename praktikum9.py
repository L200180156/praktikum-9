####Kegiatan 1
##berkas=open('L200180156', 'w')
##berkas.write('L200180156\n')
##berkas.write('12-06-1999\n')
##berkas.write('Aulia Putri Rachmadani')
##berkas.close()

##kegiatan 2
berkas=open('L200180156', 'w')
berkas.write('L200180156''\n')
berkas.write('12-06-1999''\n')
berkas.write('Aulia Putri Rachmadani''\n')
berkas.write('12/06/1999''\n')
berkas.write('Bekasi''\n')
berkas.close()

berkas=open('L200180156', 'r')
nim=berkas.readline()
tl=berkas.readline()
nama=berkas.readline()
tlbaru=berkas.readline()
kota=berkas.readline()
berkas.close()

berkas=open('L200180156', 'w')
berkas.write(nim)
berkas.write(nama)
berkas.write(tlbaru)
berkas.write(kota)
berkas.close()

##kegiatan 3
import shelve
berkas=open('L200180156', 'r')
nim=berkas.readline()
tl=berkas.readline()
nama=berkas.readline()
kota=berkas.readline()
berkas.close()

berkas=shelve.open('Aulia')
berkas['a']=[nim, tl, nama, kota]

##kegiatan 4
import shelve
berkas=shelve.open('Aulia')
print ('nama:', tl)
print ('ttl:', kota)
print ('ttl:', nama)
print ('nim:', nim)


