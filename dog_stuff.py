import pickle
Signed_in = [("ADmin","Test1234")]
Animal_classes = ['test value','test value 2','test value 3']
global file_Name = "testfile"
global file_Name2 = "testfile2"

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
    fileObject = open(file_Name,'r')
    Animal_classes = pickle.load(fileObject)
    fileObject.close()

#Saving all current classes and all new classes
def Save_Animals():
    fileObject = open(file_Name,'wb')
    pickle.dump(Animal_classes,fileObject)
    fileObject.close()

#Creates a new animal and pits it in the Animal_list
def New_Animal(Animal_type, Name,Type,Age,Location,Color,Picture):
    Animals = Animal(Name,Age,Location,Color,Picture)
    Animal_classes.update({Animal_type:Animals})

#Finds all animals in the Animal_list
def Animal_search(Animal_type,Age):
    Animal_list[]
    for(Animal_type in Animal_classes):
        if(Animals.age = Age):
            Animal_list.append(Animals)
    return Animal_list
#==============================================================

#People classes
#==============================================================
#Loading in all the People Tuples
def Load_People():
    fileObject = open(file_Name2,'r')
    Signed_in = pickle.load(fileObject)
    fileObject.close()

#Saving in all the People Tuples
def Save_People():
    fileObject = open(file_Name2,'wb')
    pickle.dump(Signed_in,fileObject)
    fileObject.close()

#Creates a new Person tuple
def New_person(Username,Password):
    Signed_in.append((Username,Password))

#Finds a new person
def Find_person(Username,Password):
    for(item in Signed_in):
        if(item == (Username,Password)):
            return True
    return False
#==============================================================
