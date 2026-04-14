from database.DB_connect import DBConnect


class DAO:

    @staticmethod
    def getAllBrand():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query="""
        select Product_Brand
        from go_products"""

        cursor.execute(query)

        res=[]
        for row in cursor:
            if row["Product_Brand"] not in res:
                res.append(row["Product_Brand"])

        cursor.close()
        cnx.close()
        lista = sorted(res)
        lista.insert(0, "Nessuna Opzione")
        return lista

    @staticmethod
    def getAllRetailer():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """select Retailer_name
                from go_retailers"""

        cursor.execute(query)

        res = []
        for row in cursor:
            if row["Retailer_name"] not in res:
                res.append(row["Retailer_name"])

        cursor.close()
        cnx.close()
        lista = sorted(res)
        lista.insert(0, "Nessuna Opzione")
        return lista

    @staticmethod
    def getAllAnno():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """select YEAR(Date) as Year
                   from go_daily_sales"""

        cursor.execute(query)

        res = []
        for row in cursor:
            if row["Year"] not in res:
                res.append(row["Year"])

        cursor.close()
        cnx.close()
        lista = sorted(res)
        lista.insert(0, "Nessuna Opzione")
        return lista





