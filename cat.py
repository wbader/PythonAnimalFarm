class catDatabase:
    def __init__():
        catName = []
        catAge = []
        catWeight = []
        catColor = []
        catGender = []
        catCount = 0
    
    def addCat(self, newName, newAge, newWeight, newColor, newGender):
        if(newName in self.catName):
            return
        if(newWeight <= 0):
            return
        self.catName.Append(newName)
        self.catAge.Append(newAge)
        self.catWeight.append(newWeight)
        self.catColor.append(newColor)
        self.catGender.append(newGender)
        self.catCount = self.catCount + 1
        print(f"New cat {self.catName[self.catCount-1]} added!")
    
    def NumberOfCats(self):
        return self.catCount