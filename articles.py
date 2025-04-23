import db


def get_all_articles():
    columns = ["id_article", "title", "content",
               "id_author", "id_category", "created_at", "active"]
    return db.select(columns, "articles")


def get_article_by_id(id):
    table = "articles"
    columns = ["id_article", "title", "content",
               "id_author", "id_category", "created_at", "active"]
    where = ["id_article", "=", str(id)]
    return db.select(columns, table, where)
