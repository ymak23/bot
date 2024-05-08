INSERTREGS = "INSERT INTO regs (user_id, first_name, last_name, adress, phone, code_prod, ddate) " \
              "VALUES (%s, %s, %s, %s, %s, %s, current_timestamp)"
INSERTUSERS = "INSERT INTO users (user_id, first_name, last_name) VALUES (%s, %s, %s)"
INSERTCOURIER = "INSERT INTO courier (first_name, last_name, adress, phone) VALUES ( %s, %s, %s, %s)"
INSERTPRODUCT = "INSERT INTO product (name, code_prod, price, pricerus, priсesng) \
                        VALUES (%s, %s, %s, %s, %s)"
UPDPROD = "UPDATE product SET name = %s  WHERE code_prod =%s;"
DELPROD = "DELETE FROM product WHERE code_prod=%s;"
DELCOURIER = "DELETE FROM courier WHERE first_name = %s;"
UPDSTATUS = "UPDATE regs SET status =%s WHERE id = %s ;"
UPDADRESSC = "UPDATE courier SET adress = %s " \
              "  WHERE first_name =%s;"
UPDPHONEC = "UPDATE courier SET phone = %s " \
              "  WHERE first_name =%s;"
UPDNUM = "UPDATE regs SET num =%s " \
              "WHERE id = %s ;"
UPDIDCOUR = "UPDATE regs SET id_courier =%s " \
              "WHERE id = %s ;"
SELECTPROD = "SELECT * FROM product"
SELECTAVG = "SELECT AVG(ratings) FROM rating WHERE id_courier = %s"
INSERTRAT = " insert into rating(id_courier, ratings) values (%s, %s)"
