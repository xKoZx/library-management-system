
# Library Management System

A simple Flask application to manage books and members in a library.

---

## Features

- **Books**: Add, update, delete, and search for books by title or author.
- **Members**: Add, update, delete, and view members.
- **Preloaded Data**: Includes 3 Indian books and 3 Indian members.
- **CRUD Operations**: Fully supports Create, Read, Update, and Delete functionality.

---

## How to Clone and Run the Application

1. **Clone the Repository**:
   Open your terminal or command prompt and run:
   ```bash
   git clone https://github.com/yourusername/library-management-system.git
   cd library-management-system
   ```

2. **Install Dependencies**:
   Install the required Python libraries:
   ```bash
   pip install flask sqlalchemy
   ```

3. **Run the Application**:
   Start the Flask application:
   ```bash
   python app.py
   ```
   The application will run at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## Preloaded Data

### Books
1. **The Guide** by R.K. Narayan (Fiction)
2. **Gitanjali** by Rabindranath Tagore (Poetry)
3. **Wings of Fire** by A.P.J. Abdul Kalam (Autobiography)

### Members
1. Rahul Sharma (`rahul.sharma@koz.com`)
2. Priya Singh (`priya.singh@koz.com`)
3. Ananya Verma (`ananya.verma@koz.com`)

---

## Operations and Commands

### **1. Add Records**

#### Add a Book
To add a new book:
```bash
curl -X POST http://127.0.0.1:5000/books/ -H "Content-Type: application/json" -d "{"title":"Book Title", "author":"Author Name", "genre":"Genre", "available":true}"
```

#### Add a Member
To add a new member:
```bash
curl -X POST http://127.0.0.1:5000/members/ -H "Content-Type: application/json" -d "{"name":"Member Name", "email":"email@example.com", "active":true}"
```

---

### **2. View Records**

#### View All Books
```bash
curl -X GET http://127.0.0.1:5000/books/
```

#### View All Members
```bash
curl -X GET http://127.0.0.1:5000/members/
```

---

### **3. Search Records**

#### Search for Books by Title
```bash
curl -X GET "http://127.0.0.1:5000/books/?title=Book%20Title"
```

#### Search for Books by Author
```bash
curl -X GET "http://127.0.0.1:5000/books/?author=Author%20Name"
```

---

### **4. Update Records**

#### Update a Book
To update a book's details:
```bash
curl -X PUT http://127.0.0.1:5000/books/<book_id> -H "Content-Type: application/json" -d "{"title":"Updated Title", "author":"Updated Author", "genre":"Updated Genre", "available":false}"
```
Replace `<book_id>` with the actual book ID.

#### Update a Member
To update a member's details:
```bash
curl -X PUT http://127.0.0.1:5000/members/<member_id> -H "Content-Type: application/json" -d "{"name":"Updated Name", "email":"updated_email@example.com", "active":false}"
```
Replace `<member_id>` with the actual member ID.

---

### **5. Delete Records**

#### Delete a Book
```bash
curl -X DELETE http://127.0.0.1:5000/books/<book_id>
```

#### Delete a Member
```bash
curl -X DELETE http://127.0.0.1:5000/members/<member_id>
```

---

## Assumptions and Design Choices

- **Blueprints**: Books and members are handled in separate modules for clarity.
- **SQLite**: A lightweight database is used for simplicity.
- **RESTful APIs**: CRUD operations are implemented following RESTful standards.

---

## Limitations

- The application is built for demonstration purposes and not for production use.
- Advanced features like authentication and input validation are not implemented.

---
