#!/bin/python

class ContactData:
  contactsCounter = 0

  def __init__(self, ID, name, phone):
    self.ID = ID
    self.name = name
    self.phone = phone
    ContactData.contactsCounter += 1

class ContactManagement:
  contacts = {}

  @staticmethod
  def addContact():
    ID = input("Entet the contact ID: ")
    name = input("Enter the name: ")
    phone = input("Enter the phone mumber: ")

    ContactManagement.contacts[ID] = ContactData(ID, name, phone)

    print(f"\n{name} was added successfully..\n")

  @staticmethod
  def viewContact():
    contactsDict = ContactManagement.contacts

    for key in contactsDict:
      print("{", end="")
      print(f"ID: {contactsDict[key].ID}", end=", ")
      print(f"name: {contactsDict[key].name}", end=", ")
      print(f"phone: {contactsDict[key].phone}", end="}\n")

  @staticmethod
  def editContact():
    contactsDict = ContactManagement.contacts
    contactID = input("Enter the contact ID: ")

    if contactID in contactsDict:
      newID = input("Enter the new ID: ")
      newName = input("Enter the new name: ")
      newPhone = input("Enter the new phone: ")

      contactsDict[contactID] = ContactData(newID, newName, newPhone)
      print(f"\nContact with ID {contactID} was updated successfully..\n")
    else:
      print(f"\nContact with ID {contactID} does not exist.\n")

def printUserChoices():
  print("Contact Management\n")
  print("1- Add a contact")
  print("2- View contact")
  print("3- Edit comtact")
  print("4- Exit\n")

contactManagement = ContactManagement

while True:
  try:
    printUserChoices()
    userChoice = int(input("Enter a number from 1 to 4: "))

    if userChoice == 1:
      contactManagement.addContact()
    elif userChoice == 2:
      contactManagement.viewContact()
    elif userChoice == 3:
      contactManagement.editContact()
    elif userChoice == 4:
      print("Programme exit....")
      break
    else:
      print("Please enter a valid number between 1 and 4.")
  except ValueError:
    print("Invalid input. Please enter a number.")


  print("========================================")
