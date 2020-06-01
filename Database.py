import mysql.connector


def database():
    conn = mysql.connector.connect(
        host="opusflights.com",
        user="course4",
        password="course4",
        db="course4.3")
    cursor = conn.cursor()
    mysql_insert_query = """select protein_name, lineage, description 
    from protein_seq natural join taxonomy"""
    cursor.execute(mysql_insert_query)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


def database_filter(filter, checkbox_p, checkbox_s, checkbox_f):
    conn = mysql.connector.connect(
        host="opusflights.com",
        user="course4",
        password="course4",
        db="course4.3")
    cursor = conn.cursor()
    if checkbox_p:
        if checkbox_s:
            if checkbox_f:  # p:True s:True f:True
                mysql_insert_query = """select protein_name, lineage, description from protein_seq natural join taxonomy 
                where protein_name like %s or lineage like %s or description like %s;"""
                query_input = (
                "%" + filter + "%", "%" + filter + "%", "%" + filter + "%")
            else:  # p:True s:True f:False
                mysql_insert_query = """select protein_name, lineage, description from protein_seq natural join taxonomy 
                where protein_name like %s or lineage like %s;"""
                query_input = ("%" + filter + "%", "%" + filter + "%")
        else:
            if checkbox_f:  # p:True s:False f:True
                mysql_insert_query = """select protein_name, lineage, description from protein_seq natural join taxonomy 
                where protein_name like %s or description like %s;"""
                query_input = ("%" + filter + "%", "%" + filter + "%")
            else:  # p:True s:False f:False
                mysql_insert_query = """select protein_name, lineage, description from protein_seq natural join taxonomy 
                where protein_name like %s;"""
                query_input = ("%" + filter + "%",)
    else:
        if checkbox_s:
            if checkbox_f:  # p:False s:True f:True
                mysql_insert_query = """select protein_name, lineage, description from protein_seq natural join taxonomy 
                where lineage like %s or description like %s;"""
                query_input = ("%" + filter + "%", "%" + filter + "%")
            else:  # p:False s:True f:False
                mysql_insert_query = """select protein_name, lineage, description from protein_seq natural join taxonomy 
                where lineage like %s;"""
                query_input = ("%" + filter + "%",)
        else:
            if checkbox_f:  # p:False s:False f:True
                mysql_insert_query = """select protein_name, lineage, description from protein_seq natural join taxonomy 
                where description like %s;"""
                query_input = ("%" + filter + "%",)
    cursor.execute(mysql_insert_query, query_input)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


if __name__ == "__main__":
    database()
