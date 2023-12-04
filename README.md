# Take-Home Exam: In-Memory Database Implementation

### Objective:
Implement an in-memory database system with a command-line interface that meets specific functionality and performance requirements. Your code should be clear, well-documented, and handle edge cases effectively. You can use libraries except for database-specific or actual database systems. Feel free to use online references, such as Google and Stack Overflow.

### Instructions:
Create a command-line program that reads input from STDIN line by line and executes the following database functions. Additionally, provide a README file with instructions on how to run your program.

Database Functions:

- `SET` [name] [value]: Sets the value associated with the given name in the database.
- `GET` [name]: Retrieves and prints the value for the specified name. If the name is not in the database, print "NULL."
- `DELETE` [name]: Deletes the value associated with the specified name from the database.
- `COUNT` [value]: Returns the count of names that have the given value assigned to them. If the value is not assigned to any name, print "0."
- `BEGIN`: Starts a new transaction.
- `ROLLBACK`: Rolls back the most recent transaction. If there is no transaction to rollback, print "TRANSACTION NOT FOUND."
- `COMMIT`: Commits all open transactions and makes changes permanent.
- `END`: Exits the database.
### Performance Requirements:

Aim for efficient operations: Ensure that GET, SET, DELETE, and COUNT have a runtime of less than O(log n), if not better (where n is the number of items in the database).
Memory usage should not double with each transaction.
Minimum Requirements:

Pass the first three test cases outlined in the exam document.
Do not use actual database systems or database libraries.
Implement the basic commands (GET, SET, DELETE, and COUNT) as per the specification. They should accept the correct number of arguments and function correctly.

Certainly, I can reformat the examples to make them more readable. Here's the same set of examples in a more organized format:

**Example 1: Basic Commands**

1. Execute: `SET a foo`
2. Execute: `SET b foo`
3. Execute: `COUNT foo`
   - Expected Output: `2`
4. Execute: `COUNT bar`
   - Expected Output: `0`
5. Execute: `DELETE a`
6. Execute: `COUNT foo`
   - Expected Output: `1`
7. Execute: `SET bbaz`
8. Execute: `COUNT foo`
   - Expected Output: `0`
9. Execute: `GET bbaz`
   - Expected Output: `NULL`
10. Execute: `GET BNUL`
11. Execute: `END`

**Example 2: Multiple Transactions**

1. Execute: `SET a foo`
2. Execute: `SET a foo`
3. Execute: `COUNT foo`
   - Expected Output: `1`
4. Execute: `GET a foo`
5. Execute: `DELETE a`
6. Execute: `GET aNUL`
7. Execute: `COUNT foo`
   - Expected Output: `0`
8. Execute: `END`

**Example 3: Nested Transactions**

1. Execute: `BEGIN`
2. Execute: `SET a foo`
3. Execute: `GET a foo`
   - Expected Output: `foo`
4. Execute: `BEGIN`
5. Execute: `SET abar`
6. Execute: `GET abar`
   - Expected Output: `abar`
7. Execute: `SET abaz`
8. Execute: `ROLLBACK`
9. Execute: `GET a foo`
   - Expected Output: `foo`
10. Execute: `ROLLBACK`
11. Execute: `GET aNUL`
12. Execute: `END`

**Example 4: Nested Transactions with COMMIT**

1. Execute: `SET a foo`
2. Execute: `SET bbaz`
3. Execute: `BEGIN`
4. Execute: `GET a foo`
   - Expected Output: `foo`
5. Execute: `SET abar`
6. Execute: `COUNT bar`
   - Expected Output: `1`
7. Execute: `BEGIN`
8. Execute: `COUNT bar`
   - Expected Output: `1`
9. Execute: `DELETE a`
10. Execute: `GET aNUL`
11. Execute: `COUNT bar`
   - Expected Output: `0`
12. Execute: `ROLLBACK`
13. Execute: `GET abar`
   - Expected Output: `bar`
14. Execute: `COUNT bar`
   - Expected Output: `1`
15. Execute: `COMMIT`
16. Execute: `GET abar`
   - Expected Output: `bar`
17. Execute: `GET bbaz`
18. Execute: `END`

These reformatted examples should help candidates understand the sequence of commands and expected outcomes more easily.