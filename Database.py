import mysql.connector


def database():
    """Haalt de gegevens in de database op.

    :return: Een lijst met proteine naam, een lijst met de lineage,
    een lijst met de functie
    """
    conn = mysql.connector.connect(
        host="opusflights.com",
        user="course4",
        password="course4",
        db="course4.3")
    cursor = conn.cursor()
    list_protein_name = []
    list_lineage = []
    list_description = []
    mysql_insert_query = """select protein_name, lineage, description 
    from protein_seq join taxonomy t on protein_seq.taxonomy_tax_id = t.tax_id limit 10"""
    cursor.execute(mysql_insert_query)
    for i in cursor:
        list_protein_name.append(i[0])
        list_lineage.append(i[1])
        list_description.append(i[2])
    cursor.close()
    conn.close()
    return list_protein_name, list_lineage, list_description


def database_filter(filter, checkbox_p, checkbox_s, checkbox_f, checkbox_o):
    """Filtert in de database op het zoekwoord in kolommen die gevinkt 
    waren op de Resultaten pagina.

    :param filter: Een string waarop gefilterd wordt
    :param checkbox_p: Een boolean of er wel of niet gefilterd wordt in
    de proteine naam
    :param checkbox_s: Een boolean of er wel of niet gefilterd wordt in
    de lineage
    :param checkbox_f: Een boolean of er wel of niet gefilterd wordt in
    de functie
    :param checkbox_o: Een boolean of er wel of niet gefilterd wordt in
    het organisme
    :return: Een lijst met proteine naam, een lijst met de lineage,
    een lijst met de functie
    """
    conn = mysql.connector.connect(
        host="opusflights.com",
        user="course4",
        password="course4",
        db="course4.3")
    cursor = conn.cursor()
    list_protein_name = []
    list_lineage = []
    list_description = []
    if checkbox_p:
        if checkbox_s:
            if checkbox_f:
                if checkbox_o:# p:True s:True f:True o:True
                    mysql_insert_query = """select protein_name, lineage, description 
                    from protein_seq join taxonomy t on protein_seq.taxonomy_tax_id = t.tax_id 
                    where protein_name like %s or lineage like %s or description like %s or organism like %s;"""
                    query_input = ("%" + filter + "%", "%" + filter + "%", "%"
                                   + filter + "%", "%" + filter + "%")
                else: #p:True s:True f:True o:False
                    mysql_insert_query = """select protein_name, lineage, description 
                                        from protein_seq join taxonomy t on protein_seq.taxonomy_tax_id = t.tax_id 
                                        where protein_name like %s or lineage like %s or description like %s;"""
                    query_input = ("%" + filter + "%", "%" + filter + "%", "%"
                                   + filter + "%")
            else:
                if checkbox_o: # p:True s:True f:False o:True
                    mysql_insert_query = """select protein_name, lineage, description 
                    from protein_seq join taxonomy t on protein_seq.taxonomy_tax_id = t.tax_id
                    where protein_name like %s or lineage like %s or organism like %s;"""
                    query_input = ("%" + filter + "%", "%" + filter + "%", "%" + filter + "%")
                else: #p:True s:True f:False o:False
                    mysql_insert_query = """select protein_name, lineage, description 
                                        from protein_seq join taxonomy t on protein_seq.taxonomy_tax_id = t.tax_id
                                        where protein_name like %s or lineage like %s;"""
                    query_input = ("%" + filter + "%", "%" + filter + "%")
        else:
            if checkbox_f:
                if checkbox_o: # p:True s:False f:True o:True
                    mysql_insert_query = """select protein_name, lineage, description 
                                        from protein_seq join taxonomy t on protein_seq.taxonomy_tax_id = t.tax_id
                                        where protein_name like %s or description like %s or organism like %s;"""
                    query_input = ("%" + filter + "%", "%" + filter + "%", "%" + filter + "%")
                else:# p:True s:False f:True o:False
                    mysql_insert_query = """select protein_name, lineage, description 
                    from protein_seq join taxonomy t on protein_seq.taxonomy_tax_id = t.tax_id
                    where protein_name like %s or description like %s;"""
                    query_input = ("%" + filter + "%", "%" + filter + "%")
            else:
                if checkbox_o: # p:True s:False f:False o:True
                    mysql_insert_query = """select protein_name, lineage, description 
                                        from protein_seq join taxonomy t on protein_seq.taxonomy_tax_id = t.tax_id 
                                        where protein_name like %s or organism like %s;"""
                    query_input = ("%" + filter + "%", "%" + filter + "%")
                else: # p:True s:False f:False o:False
                    mysql_insert_query = """select protein_name, lineage, description 
                    from protein_seq join taxonomy t on protein_seq.taxonomy_tax_id = t.tax_id 
                    where protein_name like %s;"""
                    query_input = ("%" + filter + "%",)
    else:
        if checkbox_s:
            if checkbox_f:
                if checkbox_o: # p:False s:True f:True o:True
                    mysql_insert_query = """select protein_name, lineage, description 
                                        from protein_seq join taxonomy t on protein_seq.taxonomy_tax_id = t.tax_id
                                        where lineage like %s or description like %s or organism like %s;"""
                    query_input = ("%" + filter + "%", "%" + filter + "%", "%" + filter + "%")
                else: # p:False s:True f:True o:False
                    mysql_insert_query = """select protein_name, lineage, description 
                    from protein_seq join taxonomy t on protein_seq.taxonomy_tax_id = t.tax_id
                    where lineage like %s or description like %s;"""
                    query_input = ("%" + filter + "%", "%" + filter + "%")
            else:  
                if checkbox_o: # p:False s:True f:False o:True
                    mysql_insert_query = """select protein_name, lineage, description 
                                        from protein_seq join taxonomy t on protein_seq.taxonomy_tax_id = t.tax_id
                                        where lineage like %s or organism like %s;"""
                    query_input = ("%" + filter + "%", "%" + filter + "%")
                else: # p:False s:True f:False o:False
                    mysql_insert_query = """select protein_name, lineage, description 
                    from protein_seq join taxonomy t on protein_seq.taxonomy_tax_id = t.tax_id
                    where lineage like %s;"""
                    query_input = ("%" + filter + "%",)
        else:
            if checkbox_f:  
                if checkbox_o: # p:False s:False f:True o:True
                    mysql_insert_query = """select protein_name, lineage, description 
                                        from protein_seq join taxonomy t on protein_seq.taxonomy_tax_id = t.tax_id
                                        where description like %s or organism like %s;"""
                    query_input = ("%" + filter + "%", "%" + filter + "%")
                else: # p:False s:False f:True o:False
                    mysql_insert_query = """select protein_name, lineage, description 
                    from protein_seq join taxonomy t on protein_seq.taxonomy_tax_id = t.tax_id
                    where description like %s;"""
                query_input = ("%" + filter + "%",)
            else:
                if checkbox_o: # p:False s:False f:False o:True
                    mysql_insert_query = """select protein_name, lineage, description 
                                        from protein_seq join taxonomy t on protein_seq.taxonomy_tax_id = t.tax_id
                                        where organism like %s;"""
                    query_input = ("%" + filter + "%",)
                else: # All False p:False s:False f:False o:False
                    mysql_insert_query = """select protein_name, lineage, description 
                                        from protein_seq join taxonomy t on protein_seq.taxonomy_tax_id = t.tax_id"""
    cursor.execute(mysql_insert_query, query_input)
    for i in cursor:
        list_protein_name.append(i[0])
        list_lineage.append(i[1])
        list_description.append(i[2])
    cursor.close()
    conn.close()
    return list_protein_name, list_lineage, list_description