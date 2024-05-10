from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
    def __init__(self, name):
        super().__init__(name)
        #  self.name = name
    def __str__(self):
        return str(self.value)
		



class NumberTooShortError(Exception):
    def __init__(self, message="Number is too short"):
        self.message = message
        super().__init__(self.message)

class NumberStartsFromLowError(Exception):
    def __init__(self, message="Number is too long"):
        self.message = message
        super().__init__(self.message)



class Phone(Field):
    # реалізація класу
   def __init__(self, number) : 
     super().__init__(number) 
     if len(number) < 10:
        raise NumberTooShortError
     elif len(number) > 10:
        raise NumberStartsFromLowError
     else:
        self.number = number
   def __str__(self):
        return str(self.value)
		

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # реалізація класу
    def add_phone(self,number: str):
        self.phones.append(Phone(number))

    def remove_phone(self,phone_number:str):
       
         self.phone = [phone for phone in self.phones if self.phone != phone_number]
             


    def edit_phone(self, number:str,new_number:str): 
       for phone in self.phones:
           if phone.value == number:
               self.phones.remove(phone)
               break
       new_phone = Phone(new_number)
       self.phones.append(new_phone)
       

    def find_phone(self,number):
        for phone in self.phones:
           if phone.value == number:
               return phone 



    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
     def __init__(self):
        self.data = dict()

     def add_record(self,record):
       self.data[record.name.value] = record


    #  def add_record(self,name,number):
    #    record = Record(name)
    #    record.add_phone(number)
    #    self.records[name] = record

     def find(self,name):
       record = self.data.get(name)
       return record
       
     def delete(self,name):
       del self.data[name]
    


# Створення нової адресної книги
book = AddressBook()

    # Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
book.add_record(john_record)

    # Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

    # Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

    # Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
book.delete("Jane")
