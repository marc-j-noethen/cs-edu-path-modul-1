## 📊 Summary Using the 80/20 Principle

## Installation for Windows 11 (instead of macOS)

**DB Browser for SQLite Installation:**

1. **Download:** Visit https://sqlitebrowser.org/dl/ and download the `.msi` file for Windows
2. **Installation:** Run the `.msi` file and follow the installation wizard
3. **Verification:** Launch "DB Browser for SQLite" from the Start menu

---

### Core Concept: What are Databases?

A **database** is like a highly organized digital filing cabinet that efficiently stores, manages, and makes large amounts of information accessible. Without databases, it would be impossible to quickly find specific information within large datasets. **The 5 Main Functions:**

1. **Store** – Reliably save data
2. **Organize** – Logically structure data
3. **Retrieve** – Quickly find specific data
4. **Update** – Make changes
5. **Manage** – Control access rights

### Relational Databases: Table Structure

**Tables** are the core of relational databases and work like spreadsheets:

- **Columns** = Categories of information (e.g. Name, Email, Date of Birth)
- **Rows** = Individual records (e.g. a specific customer)
- **Primary Key** = Unique ID for identifying each row (e.g. CustomerID) **Example of a Customers table:**
- Row 1: CustomerID=1, FirstName=Alice, Email=alice@email.com
- Row 2: CustomerID=2, FirstName=Bob, Email=bob@email.com The term "relational" comes from the fact that different tables can be linked to each other via shared columns (e.g. Orders table linked to Customers via CustomerID).

### SQL: The Language of Databases

**SQL (Structured Query Language)** is THE standard language for database operations. **The 4 Most Important SQL Commands (CRUD Operations):**

1. **SELECT** – Retrieve data (Read)
    
    ```sql
    SELECT * FROM Customers;
    SELECT FirstName, Email FROM Customers WHERE CustomerID = 2;
    ```
    
2. **INSERT INTO** – Insert new data (Create)
    
    ```sql
    INSERT INTO Customers (FirstName, Email) VALUES ('David', 'david@email.com');
    ```
    
3. **UPDATE** – Modify existing data (Update)
    
    ```sql
    UPDATE Customers SET Email = 'newemail@email.com' WHERE CustomerID = 1;
    ```
    
4. **DELETE FROM** – Delete data (Delete)
    
    ```sql
    DELETE FROM Customers WHERE CustomerID = 3;
    ```
    

### The SELECT Command in Detail (80% of all queries)

**Basic structure:**

```sql
SELECT columns
FROM table
WHERE condition;
```

- `SELECT *` = All columns
- `SELECT Name, Email` = Only specific columns
- `WHERE` = Filter (e.g. `WHERE SignupDate = '2023-01-15'`)
- Text in WHERE conditions requires quotation marks: `WHERE FirstName = 'Alice'`

### Practical Application: DB Browser for SQLite

**Workflow in 5 Steps:**

1. **Create new database** → Save file with `.sqlite` extension
2. **Define table** → Specify columns with names and data types
3. **Set primary key** → Mark one column as unique ID (e.g. FriendID)
4. **Enter data** → Add rows via "Browse Data"
5. **Execute SQL queries** → Enter commands in the "Execute SQL" tab and run them

### Relevance to Cybersecurity

**Why databases are important in IT security:**

- **Log analysis:** Security logs are often stored in databases and analyzed with SQL
- **Vulnerability databases:** CVE databases use SQL for queries
- **SQL injection:** Understanding SQL is essential for recognizing these attacks
- **Forensics:** Examining database activity during security incidents
- **User management:** Access rights and user accounts are managed in databases

### Key Takeaways

- **One table** = One category of objects (e.g. Customers, Orders, Products)
- **One row** = One specific object (e.g. the customer Alice)
- **One column** = One property (e.g. email address)
- **Primary key** = The unique "ID number" of each row
- **SELECT** is like "Show me..." – the most frequently used SQL command

---

## Tools Used

|**Category**|**Term**|**Meaning**|
|---|---|---|
|**Tools Used**|DB Browser for SQLite (Windows 11)|Free graphical application for creating and managing SQLite databases|
||SQLite|Lightweight, file-based database system without a separate server|
||SQL Editor|Integrated text editor for writing and executing SQL commands|
||Table Editor|Graphical interface for creating and editing database structures|
||Query Executor|Function for executing SQL queries and displaying results|

---

## Technical Terms

|**Category**|**Term**|**Meaning**|
|---|---|---|
|**Technical Terms**|Database|Organized, electronically stored collection of data for efficient management|
||Relational Database|Database that organizes data in interlinked tables|
||Table|Collection of related data entries in rows and columns|
||Row/Record|Single entry in a table with all values for one object|
||Column/Field|Vertical category in a table containing a specific data type|
||Primary Key|Column with a unique value for identifying each row (e.g. CustomerID)|
||Structured Data|Data organized in a predefined format (tables)|
||SQL (Structured Query Language)|Standard language for managing and querying relational databases|
||SELECT Statement|SQL command for retrieving data from a table|
||WHERE Clause|Filter condition in SQL queries for restricting results|
||INSERT INTO|SQL command for inserting new records|
||UPDATE|SQL command for modifying existing records|
||DELETE FROM|SQL command for deleting records|
||CREATE TABLE|SQL command for creating new tables|
||Data Types|Categories of data (INTEGER for whole numbers, TEXT for text, DATE for dates)|
||Query|Request to the database for retrieving or manipulating data|
||Relation|Link between tables via shared columns (e.g. CustomerID)|
|**Important Vocabulary**|Retrieve|Fetch and display data from the database|
||Store|Permanently save data in the database|
||Organize|Logically structure and arrange data|
||Update|Modify or supplement existing data|
||Manage|Control database structure and access rights|
||Field|Synonym for column in a table|
||Record|Synonym for row in a table|
||Unique Identifier|Value that appears only once in a column|
||Condition|Criterion for filtering records (e.g. WHERE CustomerID = 2)|
||Execute|Send an SQL command to the database and have it processed|
||Results|Data returned by the database after a query|