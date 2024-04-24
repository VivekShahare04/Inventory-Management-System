import sqlite3

def create_table():
    conn = sqlite3.connect('Goods.db')
    cursor = conn.cursor() #creating a cursor
    
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS Products(
                       id TEXT PRIMARY KEY,
                       name TEXT,
                       in_stock INTEGER)''')
    conn.commit()
    conn.close()
    
def fetch_Goods():
    conn = sqlite3.connect('Goods.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Goods')
    Goods = cursor.fetchall()
    conn.close()
    return Goods

def insert_goods(id,name,in_stock):
    conn = sqlite3.connect('Goods.db')
    cursor = conn.cursor() 
    cursor.execute('INSERT INTO GOODS(id,name,in_stock)VALUES(?,?,?)',(id,name,in_stock))
    conn.commit()
    conn.close()
    
def delete_product(id):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Products WHERE id =?',(id))                 
    conn.commit()
    conn.close()

def update_product(new_name ,new_stock,id):
    conn = sqlite3.connect('Goods.db')
    cursor =conn.cursor()
    cursor.execute("UPDATE Goods SET name =?, in_stock =? WHERE id = ?",
                  ( new_name, new_stock, id))
    conn.commit()
    conn.close()

def id_exists(id):
    conn = sqlite3.connect('Goods.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*)FROM PRODUCTS WHERE id = ?',(id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] > 0

create_table()
