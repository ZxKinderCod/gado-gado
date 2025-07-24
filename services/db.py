import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='kios_sederhana'
    )

def insert_item(kode_barang, nama_barang, harga_barang, stok_barang):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute(
            "INSERT INTO kios_sederhana (kode_barang, nama_barang, harga_barang, stok_barang) VALUES (%s, %s, %s, %s)", 
            (kode_barang, nama_barang, harga_barang, stok_barang)
        )
        conn.commit()
        print("Data berhasil disimpan ke database!")
        
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def fetch_item():
    try:
        con = get_connection()
        cursor = con.cursor()
        # cursor = get_connection.cursor
        cursor.execute("SELECT * FROM kios_sederhana")
        items = cursor.fetchall()
        return items
    
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
        return[]
    finally:
        if cursor:
            cursor.close()
    if conn:
            conn.close()
            
def get_item_by_code(kode_barang):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM kios_sederhana WHERE kode_barang = %s", (kode_barang,))
        item = cursor.fetchone()
        return item
        
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
        return None
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
            
            
def delete_item(kode_barang):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        # Cek apakah item dengan kode tersebut ada
        cursor.execute("SELECT * FROM kios_sederhana WHERE kode_barang = %s", (kode_barang,))
        item = cursor.fetchone()
        
        if item:
            cursor.execute("DELETE FROM kios_sederhana WHERE kode_barang = %s", (kode_barang,))
            conn.commit()
            return True
        else:
            print(f"Barang dengan kode '{kode_barang}' tidak ditemukan!")
            return False
            
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
        return False
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
            
def update_item(kode_barang, nama_barang, harga_barang, stok_barang):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        # Cek apakah item dengan kode tersebut ada
        cursor.execute("SELECT * FROM kios_sederhana WHERE kode_barang = %s", (kode_barang,))
        item = cursor.fetchone()
        
        if item:
            cursor.execute(
                "UPDATE kios_sederhana SET nama_barang = %s, harga_barang = %s, stok_barang = %s WHERE kode_barang = %s",
                (nama_barang, harga_barang, stok_barang, kode_barang)
            )
            conn.commit()
            print(f"Data barang dengan kode '{kode_barang}' berhasil diupdate!")
            return True
        else:
            print(f"Barang dengan kode '{kode_barang}' tidak ditemukan!")
            return False
            
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
        return False
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()