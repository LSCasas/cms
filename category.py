import db


def get_all_categories():
    columns = ["id_category", "name"]
    return db.select(columns, "category")
