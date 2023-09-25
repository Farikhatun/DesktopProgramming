import mysql.connector


koneksi = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="codeloop"
)


mycursor = koneksi.cursor()

lanjut = True
while lanjut:
    print("")
    print("")
    print("")
    print("CRUD User")
    print("1.LIHAT DATA")
    print("2.TAMBAH DATA")
    print("3.UBAH DATA")
    print("4.HAPUS DATA")
    print("5.KELUAR")
    print("")

    p = int(input("PILIH MENU :"))
    print("")
    print("")
    if (p == 1):
        mycursor.execute("SELECT * FROM siswa")
        myresult = mycursor.fetchall()
        print("======================")
        print("(nim, nama, tempat_lahir, tanggal_lahir, alamat)")
        for x in myresult:
            print(x)
    elif (p == 2):
        nim = input("NIM :")
        nama = input("Nama :")
        tempat_lahir = input("Tempat Lahir :")
        tanggal_lahir = input("Tanggal Lahir :")
        alamat = input("Alamat :")
        sql = "INSERT INTO siswa (nim, nama, tempat_lahir, tanggal_lahir, alamat) VALUES (%s,%s,%s,%s,%s)"
        val = (nim, nama, tempat_lahir, tanggal_lahir, alamat)
        mycursor.execute(sql, val)
        koneksi.commit()
        print(mycursor.rowcount, "data siswa berhasil di tambah")
    elif (p == 3):
        nim = input("NIM :")
        mycursor.execute("SELECT * FROM siswa where nim ="+nim+" LIMIT 1")
        myresult = mycursor.fetchall()
        siswa = None
        for x in myresult:
            siswa = x
        if (siswa != None):
            nama = input("Nama ("+siswa[1]+") :") or siswa[1]
            tempat_lahir = input("Tempat Lahir ("+siswa[2]+") :") or siswa[2]
            tanggal_lahir = input("Tanggal Lahir ("+siswa[3]+") :") or siswa[3]
            alamat = input("Alamat ("+siswa[4]+") :") or siswa[4]
            sql = "UPDATE siswa SET nama=%s,tempat_lahir=%s,tenggal_lahir=%s,alamat+%s WHERE nim=%s"
            val = (nim, nama, tempat_lahir, tanggal_lahir, alamat)
            mycursor.execute(sql, val)
            koneksi.commit()
            print(mycursor.rowcount, "data siswa berhasil di simpan")
        else:
            print("data tidak ditemukan")
    elif (p == 4):
        nim = input("NIM SISWA :")
        mycursor.execute("SELECT * FROM siswa where nim ="+nim+" LIMIT 1")
        myresult = mycursor.fetchall()
        siswa = None
        for x in myresult:
            siswa = x
        if (siswa != None):
            print("MENGHAPUS DATA :", siswa)
            sql = "DELETE FROM siswa WHERE nim="+nim
            mycursor.execute(sql)
            koneksi.commit()
            print(mycursor.rowcount, "data siswa berhasil di hapus")
        else:
            print("data tidak ditemukan")
    elif (p == 5):
        lanjut = False
