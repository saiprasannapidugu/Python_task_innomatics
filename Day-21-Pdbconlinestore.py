from databaseorder import get_connection

con=get_connection()
cursor=con.cursor()

query="""
CREATE TABLE IF NOT EXISTS products
(id INT PRIMARY KEY,
name VARCHAR(100),
price INT,
quantity INT)
"""

cursor.execute(query)
con.commit()

print('Products table created successfully!')
while True:
    n=int(input("""
        1.Add product
        2.Show products
        3.Search product
        4.Purchase product
        5.Calculate bill
        6.Delete product
        7.Exit
        Enter your choice:"""))

    if n==1:
        id=int(input('Enter product id:'))
        name=input('Enter product name:')
        price=int(input('Enter product price:'))
        quantity=int(input('Enter product quantity:'))

        query='INSERT INTO products VALUES (%s,%s,%s,%s)'
        cursor.execute(query,(id,name,price,quantity))
        con.commit()

        print('Product added successfully!')

    elif n==2:
        query='SELECT * FROM products'
        cursor.execute(query)
        result=cursor.fetchall()

        for row in result:
            print(row[0], '       ',row[1],'               ',row[2],'       ',row[3])

    elif n==3:
        id=int(input('Enter product id:'))

        query='SELECT * FROM products WHERE id=%s'
        cursor.execute(query,(id,))
        result=cursor.fetchone()

        if result:
            print(result)
        else:
            print('Product not found!')

    elif n==4:
        id=int(input('Enter product id:'))
        quantity=int(input('Enter purchase quantity:'))

        query='SELECT * FROM products WHERE id=%s'
        cursor.execute(query,(id,))
        result=cursor.fetchone()

        if result:
            if result[3]>=quantity and quantity>0:
                price=result[2]*quantity

                query='UPDATE products SET quantity=quantity-%s WHERE id=%s'
                cursor.execute(query,(quantity,id))
                con.commit()

                print('Product purchased successfully!')
                print('Amount:',price)
            else:
                print('Insufficient stock or invalid quantity!')
        else:
            print('Product not found!')

    elif n==5:
        query='SELECT * FROM products'
        cursor.execute(query)
        result=cursor.fetchall()

        total=0
        print('ID         NAME                PRICE             QUANTITY')

        for row in result:
            print(row[0], '       ',row[1],'               ',row[2],'       ',row[3])
            total+=row[2]*row[3]

        print('Total stock value:',total)

    elif n==6:
        id=int(input('Enter product id to delete:'))

        query='DELETE FROM products WHERE id=%s'
        cursor.execute(query,(id,))
        con.commit()

        if cursor.rowcount>0:
            print('Product deleted successfully!')
        else:
            print('Product not found!')

    elif n==7:
        print('Thank you!')
        cursor.close()
        con.close()
        break

    else:
        print('Invalid choice! Please try again.')
