import db


def get_all_authors():
    columns = ["id_author", "name", "last_name", "email", "password", "alias"]
    return db.select(columns, "author")


def get_author_by_id(id):
    table = "author"
    columns = ["id_author", "name", "last_name", "email", "password", "alias"]
    where = ["id_author", "=", str(id)]
    return db.select(columns, table, where)


def create_author(name, last_name, email, password, alias):
    columns = ["name", "last_name", "email", "password", "alias"]
    values = [name, last_name, email, password, alias]
    return db.insert("author", columns, values)
