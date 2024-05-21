import homework as db

while True :
   print('='*8,'Selamat Datang di Toko Kami','='*8)
   print('Pilihan')
   print('1. Tambah data barang')
   print('2. Hapus data barang')
   print('3. Tampilkan data barang')
   print('4. Edit data')
   print('5. Jumlah data')
   print('6. Cari data')
   print('7. Keluar')
   pilihan = int(input('Masukan pilihan : ')) 
   if pilihan == 1:
      db.insert()
   elif pilihan == 2:
      db.hapus_data()
   elif pilihan == 3:
      db.view_data()
   elif pilihan == 4:
      db.edit_data()
   elif pilihan == 5:
      db.jumlah_data()
   elif pilihan == 6:
      db.cari_data()
   elif pilihan == 7:
     print('Terimakasih Telah Datang di Toko Kami!')
     break