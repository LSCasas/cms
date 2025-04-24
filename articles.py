import db


def get_all_articles():
    columns = ["id_article", "title", "content",
               "id_author", "id_category", "created_at", "active"]
    return db.select(columns, "articles")


def get_active_articles():
    columns = ["id_article", "title", "content",
               "id_author", "id_category", "created_at", "active"]
    where_clause = ("active", "=", True)
    return db.select(columns, "articles", where=where_clause)


def get_by_category(category):
    columns = ["id_article", "title", "content",
               "id_author", "id_category", "created_at", "active"]
    where_clause = ("id_category", "=", category)
    return db.select(columns, "articles", where=where_clause)


def get_by_author(author):
    columns = ["id_article", "title", "content",
               "id_author", "id_category", "created_at", "active"]
    where_clause = ("id_author", "=", author)
    return db.select(columns, "articles", where=where_clause)


def get_active_articles():
    columns = ["id_article", "title", "content",
               "id_author", "id_category", "created_at", "active"]
    where_clause = ("active", "=", True)
    return db.select(columns, "articles", where=where_clause)


def get_article_by_id(id):
    table = "articles"
    columns = ["id_article", "title", "content",
               "id_author", "id_category", "created_at", "active"]
    where = ["id_article", "=", str(id)]
    return db.select(columns, table, where)


def create_articles(title, content, id_author, id_category, active):
    columns = ["title", "content",
               "id_author", "id_category", "active"]
    values = [title, content, id_author, id_category, active]
    return db.insert("articles", columns, values)


def update_articles(id, title, content, id_author, id_category, active):
    columns = ["title", "content",
               "id_author", "id_category", "active"]
    values = [title, content, id_author, id_category, active]
    return db.update("articles", columns, values, where=("id_article", "=", id))


def deactivate_articles(id, active):
    column = ["active"]
    value = [active]
    return db.update("articles", column, value, where=("id_article", "=", id))
