def check_str_int(query_value):
# Check pour ajouter la valeur en format STR ou INT.
    value_int = False
    value_int = all ([c.isdigit() for c in query_value ])
    if value_int:
        query_value = int(query_value)
        return query_value
    else:
        return query_value.lower()