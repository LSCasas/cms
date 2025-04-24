import db

# GET ALL


def get_all_categories():
    columns = ["id_category", "name"]
    return db.select(columns, "category")

# GET JUST ONE


def get_category_by_id(id):
    columns = ["id_category", "name"]
    table = "category"
    where = ["id_category", "=", str(id)]
    return db.select(columns, table, where)

# CREATE


def create_category(name):
    columns = ["name"]
    values = [name]
    return db.insert("category", columns, values)

# UPDATE


def update_category(id, name):
    columns = ["name"]
    values = [name]
    return db.update("category", columns, values, where=("id_category", "=", id))
