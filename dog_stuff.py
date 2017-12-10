import pickle
import os

Animal_classes = []

#==============================================================
#Class for keeping all the Animal data in
class Animal:
    kind = 'Stray'
    def __init__(self, name, Age,Location,Color,Picture):
        self.name = name
        self.age = Age
        self.color = Color
        self.Locations = Location
        self.Picture = Picture
#==============================================================

#Animal classes
#==============================================================
#Loading in all the animal classes
def Load_Animals():
        if os.path.getsize("static/Dogs.txt")>0:
            with open("static/Dogs.txt",'rb') as fileObject:
                unpickler = pickle.Unpickler(fileObject)
                Animal_classes = unpickler.load()
                fileObject.close()
#Saving all current classes and all new classes
def Save_Animals():
    fileObject = open("static/Dogs.txt",'wb')
    pickle.dump(Animal_classes,fileObject)
    fileObject.close()

#Creates a new animal and pits it in the Animal_list
def New_Animal(Animal_type, Animal_name,Type,Age,Location,Color,Picture):
    Animal_type = Animal(Animal_name,Age,Location,Color,Picture)
    Animal_classes.append(Animal_type)

#Finds all animals in the Animal_list
def Animal_search(Animal_type,Age):
    Animal_list = []
    for Animal_type in Animal_classes:
        if(Animal_type.age==Age):
            Animal_list.append(Animal_type)

    return Animal_list
#==============================================================

# #People classes
# #==============================================================
# #Loading in all the People Tuples
# def Load_People():
#     Signed_in = pickle.load(open(file_Name2,encoding="rb"))
#     fileObject.close()
#
# #Saving in all the People Tuples
# def Save_People():
#     fileObject = open(file_Name2,'wb')
#     pickle.dump(Signed_in,fileObject)
#     fileObject.close()
#
# #Creates a new Person tuple
# def New_person(Username,Password):
#     Signed_in.append((Username,Password))
#
# #Finds a new person
# def Find_person(Username,Password):
#     for item in Signed_in:
#         if(item == (Username,Password)):
#             return True
#     return False
# #==============================================================
