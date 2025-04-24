# CMS - Content Management System (Python)

> This project is part of the **Kodemia Master Bootcamp - Backend with Python**.

A simple content management system built in Python using PostgreSQL. This CMS allows you to manage articles, authors, and categories through basic CRUD operations. The system is structured in a modular way for scalability and clarity.

---

## 📁 Project Structure

```
├── author.py       # Logic for managing authors (create, update, retrieve)
├── articles.py     # Logic for managing articles (create, update, retrieve)
├── category.py     # Logic for managing categories (create, list)
├── db.py           # Database connection and query execution (PostgreSQL)
├── config.py       # Configuration settings (e.g., connection string)
├── example.env     # Sample environment variable file
├── requirements.txt# Dependencies for the project
├── venv/           # Virtual environment directory
```

---

## Features

- Create, update, and list authors
- Create, update, and list articles with author and category associations
- Filter articles by active status or category
- Create and list categories
- PostgreSQL query abstraction layer
- Structured and clean modular architecture

---

## Technologies

- Python 3
- PostgreSQL
- psycopg (PostgreSQL driver for Python)

---

## How to Use

1. Clone the repository:

   ```bash
   git clone https://github.com/LSCasas/cms.git
   cd cms
   ```

2. Set up a virtual environment and install dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Configure your `.env` file based on `example.env` with your PostgreSQL credentials.

4. Run your code using `ipython` or by importing the modules in scripts or notebooks.

---

## Example

```python
import articles

# Fetch all articles under the "Technology" category
def get_by_category(category):
    columns = ["id_article", "title", "content",
               "id_author", "id_category", "created_at", "active"]
    where_clause = ("id_category", "=", category)
    return db.select(columns, "articles", where=where_clause)

```

---

## Requirements

- Python 3.x
- PostgreSQL running locally or remotely
- psycopg library

---
