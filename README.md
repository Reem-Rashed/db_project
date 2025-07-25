# db_project
# Task 1: JSON-backed Database

## Objective  
Create a Python class (e.g. `LibraryDatabase` or `ContactList`) that stores records in memory and allows saving/loading them using a JSON file.

---

## Requirements

### 1. Record Structure
- Use `namedtuple` from the `collections` module to define the structure of each record.  
  Example: A `Book` with fields like title, author, and year.

---

### 2. Enumerations
- Use `Enum` from the `enum` module to define fixed categories.  
  Example: Book genre or contact status.

---

### 3. Data Encapsulation
- Store records in a private list or dictionary inside the class to protect internal data.

---

### 4. CRUD Operations
Implement the following methods:

- Create – Add a new record  
- Read – Retrieve and display records  
- Update – Modify an existing record  
- Delete – Remove a record

---

### 5. Input Validation and Processing
- Use `if / else` statements and loops to validate and process inputs before storing records.

---

### 6. String Formatting
- Use `f-strings` or `.format()` to display records in a clean and readable way.

---

### 7. Built-in Math Functions
- Use the `math` module to calculate:
  - Averages  
  - Totals  
  - Other basic statistics

---

### 8. File and Directory Handling
- Use the `os` module to:
  - Ensure the directory for storing files exists  
  - Handle file paths properly

---

### 9. JSON Input/Output

- Saving:  
  Convert the records into dictionaries and use `json.dump()` to write them to a file.

- Loading:  
  Use `json.load()` to read data from a file, and reconstruct records using the correct format.

---

### 10. Unicode Support
- Ensure all text, including Arabic or other Unicode characters, is stored and displayed correctly.  
  JSON supports Unicode natively — no additional configuration is required.
