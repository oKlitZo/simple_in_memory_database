import copy

#reference 
# https://www.freecodecamp.org/news/how-to-write-a-simple-toy-database-in-python-within-minutes-51ff49f47f1/ -- How to write a simple toy database in Python within minutes
# https://stackoverflow.com/questions/61485253/python-nested-dictionary-is-changing-all-values-at-once -- Python: nested dictionary is changing all values at once
# https://www.w3schools.com/python/python_ref_dictionary.asp -- Python Dictionary Methods

class InMemoryDB:
    
    def __init__(self):
        self.main_db = {}
        self.transaction_db = {}
        self.looper = True

        self.db = self.get_space()
        
    def get_space(self): # function to switch to main db and transaction db
        transaction_count = len(self.transaction_db)
        
        return self.main_db if transaction_count == 0 else self.transaction_db[transaction_count-1]
    
    def set(self, key, value): 
        self.db[key] = value
        
    def get(self, key):
        print(self.db.get(key, "NULL"))

    def delete(self, key):
        self.db.pop(key)

    def count(self, value):
        count = 0
        for each in self.db.keys():
            if self.db[each] == value:
                count = count + 1
                
        print(count)

    def begin(self):
        transaction_count = len(self.transaction_db)

        if transaction_count == 0:
            self.transaction_db[transaction_count] = copy.deepcopy(self.main_db)
        else:
            self.transaction_db[transaction_count] = copy.deepcopy(self.transaction_db[transaction_count - 1])
        
        self.db = self.get_space()
                
    def rollback(self):
        transaction_count = len(self.transaction_db)
        
        if transaction_count == 0:
            print("TRANSACTION NOT FOUND.")        
        else:
            self.transaction_db.pop(transaction_count - 1)

        self.db = self.get_space()
    
    def commit(self):        
        self.main_db.clear()
        
        self.main_db = copy.deepcopy(self.db)
        
        self.transaction_db.clear()
        
        self.db = self.get_space()
    
    def controls(self):
        action_list = {
            "set": self.set,
            "get": self.get,
            "delete": self.delete,
            "count": self.count,
            "begin": self.begin,
            "rollback": self.rollback,
            "commit": self.commit,
            "end": self.end,
        }

        user_input = input("imdb >> ")
        user_input_split = user_input.split(" ")
        command = user_input_split[0].lower()
        
        if command == "set":
            action_list.get(command)(user_input_split[1], user_input_split[2])
        elif command == "get" or command == "delete" or command == "count":
            action_list.get(command)(user_input_split[1])
        elif command == "begin" or command == "rollback" or command == "commit" or command == "end":
            action_list.get(command)()
        else:
            print("COMMAND NOT FOUND!!!")
                        
    def end(self):
        self.looper = False
        return self.looper

if __name__ == "__main__":
    
    imdb = InMemoryDB()
    
    while imdb.looper:
        imdb.controls()
        