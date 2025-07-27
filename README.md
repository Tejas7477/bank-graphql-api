# GraphQL Bank Branch API

This is a Django + GraphQL API project that allows users to query information about Indian banks and their branches. It supports advanced GraphQL queries such as listing all banks, all branches, and filtering branches by city.

---

## 🚀 Features

- ✅ GraphQL endpoint with Graphene-Django  
- ✅ List all banks  
- ✅ List all branches with detailed info  
- ✅ Filter branches by city  
- ✅ View each branch's linked bank  

---

## 🛠️ Technologies Used

- Python 3.11  
- Django 4.x  
- Graphene-Django (GraphQL)  
- SQLite (default database)  
- GraphQL Playground (enabled at `/graphql/`)

---

## 📂 Project Structure

```
bank_api/
├── bank_api/       # Django project config
├── api/            # App with models & schema
│   ├── models.py   # Bank & Branch models
│   ├── schema.py   # GraphQL types and queries
│   ├── admin.py    # Django admin setup
│   └── ...
├── db.sqlite3      # SQLite DB
├── manage.py
└── README.md
```

---

## 🧪 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
# For Windows:
venv\Scripts\activate
# For macOS/Linux:
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install django graphene-django
```

### 4. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the server

```bash
python manage.py runserver
```

Now open [http://127.0.0.1:8000/graphql/](http://127.0.0.1:8000/graphql/) to test the GraphQL API.

---

## 💻 Example Queries

### 🔹 List All Banks

```graphql
{
  allBanks {
    id
    name
  }
}
```

### 🔹 List All Branches

```graphql
{
  allBranches {
    ifsc
    branch
    address
    city
    state
    bank {
      name
    }
  }
}
```

### 🔹 Filter Branches by City

```graphql
{
  branchesByCity(city: "Delhi") {
    ifsc
    branch
    address
    bank {
      name
    }
  }
}
```

---

## ⏱️ Time Taken

Total time taken to complete the assignment: ** 2 days **, including:

- Setting up the project  
- Designing models and schema  
- Implementing and testing GraphQL queries  
- Debugging errors and formatting output

---

## 📬 Contact

For any queries, feel free to connect via GitHub Issues or email.

---

## ✅ Final Notes

- Clean architecture with modular schema and models  
- Can be easily extended with filters like state, bank name, IFSC, etc.  
- GraphQL Playground is live at: `/graphql/`
