import db


def get_all_categories():
    columns = ["id_category", "name"]
    return db.select(columns, "category")


def get_category_by_id(id):
    columns = ["id_category", "name"]
    table = "category"
    where = ["id_category", "=", str(id)]
    return db.select(columns, table, where)


def create_category(name):
    columns = ["name"]
    values = [name]
    return db.insert("category", columns, values)


def update_category(id, name):
    columns = ["name"]
    values = [name]
    return db.update("category", columns, values, where=("id_category", "=", id))
