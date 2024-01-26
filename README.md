# Simple In-Memory Database using Python Dictionary

How to run the program:
 - Open terminal
 - run "python3 in_memory_database.py"

Database Functions:

SET [name] [value]: Sets the value associated with the given name in the database.
GET [name]: Retrieves and prints the value for the specified name. If the name is not in the database, print "NULL."
DELETE [name]: Deletes the value associated with the specified name from the database.
COUNT [value]: Returns the count of names that have the given value assigned to them. If the value is not assigned to any name, print "0."
BEGIN: Starts a new transaction.
ROLLBACK: Rolls back the most recent transaction. If there is no transaction to rollback, print "TRANSACTION NOT FOUND."
COMMIT: Commits all open transactions and makes changes permanent.
END: Exits the database.

