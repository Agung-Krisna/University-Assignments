class Personal:
    def __init__(self, name, sex):
        self.dad = None
        self.mom = None
        self.sex = sex
        self.name = name
        self.kids = []
        self.wife = []
        self.husband = []
    
    def setDad(self, dad):
        self.dad = dad
        
        self.in_kids = 0
        for kids in dad.kids:
            if (kids == self):
                self.in_kids = 1
        
        if (self.in_kids == 0):
            dad.setKid(self)
    
    def setMom(self, mom):
        self.mom = mom
        
        self.in_kids = 0
        for kids in mom.kids:
            if(kids == self):
                self.in_kids = 1
        
        if (self.in_kids == 0):
            mom.setKid(self) 
    
    def setKid(self, kid):
        self.kids.append(kid)
        if (self.sex == "M"):
            if(kid.dad != self):
                kid.setDad(self)
        else:
            if(kid.mom != self):
                kid.setMom(self)
    
    def setHusband(self, husband):
        if (self.sex == "F"):
            self.husband.append(husband)

            self.in_wife = 0
            for wife in husband.wife:
                if (self == wife):
                    self.in_wife = 1
            
            if (self.in_wife == 0):
                husband.setWife(self)
                
    def setWife(self, wife):
        if (self.sex == "M"):
            self.wife.append(wife)
            
            self.in_husband = 0
            for husband in wife.husband:
                if(self == husband):
                    self.in_wife = 1
            
            if (self.in_husband == 0):
                wife.setHusband(self)
    
    def showGrandChildren(self):
        if (len(self.kids)) == 0:
            return("You haven't got kids, yet")
        grandChildren = []
        for i in range (len(self.kids)):
            for j in range (len(self.kids[i].kids)):
                grandChildren.append(self.kids[i].kids[j].name)
        if (len(grandChildren)) == 0:
            return("Your children haven't got kids, yet")
        else:
            return(grandChildren)
    
    def showSiblings(self):
        dadKids = []
        momKids = []
        siblings = []
        for children in self.dad.kids:
            if (children.name != self.name):
                dadKids.append(children.name)
        
        for children in self.mom.kids:
            if (children.name != self.name):
                momKids.append(children.name)
        
        dadKids.sort()
        momKids.sort()
        for i in range (len(dadKids)):
            for j in range (len(momKids)):
                if dadKids[i] == momKids[j]:
                    siblings.append(dadKids[i])
        
        if (len(siblings) == 0):
            return ("You don't have a sibling")
        else:
            return "Blood-related siblings: {}".format(siblings)

    def showStepSiblings(self):
        dadKids = []
        momKids = []
        stepSiblings = []
        for children in self.dad.kids:
            if (children.name != self.name):
                dadKids.append(children.name)
        
        for children in self.mom.kids:
            if (children.name != self.name):
                momKids.append(children.name)
        
        dadKids.sort()
        momKids.sort()
        for i in range (len(dadKids)):
            for j in range (len(momKids)):
                if dadKids[i] != momKids[j]:
                    stepSiblings.append(dadKids[i])
        
        if (len(stepSiblings) == 0):
            return ("You don't have a step sibling")
        else:
            return "Step-siblings: {}".format(stepSiblings)
        
    def showCousins(self):
        paternalKids = []
        maternalKids = []
        paternalCousins = []
        maternalCousins = []
        for children in (self.dad.dad.kids):
            paternalKids.append(children)

        for children in (self.mom.dad.kids):
            maternalKids.append(children)
        i = 0
        j = 0
        for children in (paternalKids):
            if children.name != self.dad.name:
                paternalCousins.append(children.kids[i].name)
                i += 1
        
        for children in (maternalKids):
            if children.name != self.mom.name:
                paternalCousins.append(children.kids[j].name)
                j += 1
        if len(maternalCousins) == 0:
            return "Paternal Cousins:", paternalCousins
        
        elif len(paternalCousins) == 0:
            return "Maternal Cousins:", maternalCousins
        
        else:
            return "Paternal Cousins:", paternalCousins, "Maternal Cousins:", maternalCousins
        
    def showGrandpa(self):
        return "Paternal Grandpa: {}".format(self.dad.dad.name), "Maternal Grandpa: {}".format(self.mom.dad.name)

    def showGrandma(self):
        return "Paternal Grandma: {}".format(self.dad.mom.name), "Maternal Grandma: {}".format(self.mom.mom.name)
    
    def showSonInLaw(self):
        daughters = []
        sonInLaw = []
        for children in self.kids:
            if children.sex == "F":
                daughters.append(children)
        
        for i in range (len(daughters)):
            if (len(daughters[i].husband)) > 0:
                for j in range (len(daughters[i].husband)):
                    sonInLaw.append(daughters[i].husband[j].name)

        if (len(sonInLaw) > 0):    
            return sonInLaw

        else:
            return "You don't have any son-in-law"
    
    def showDaughterInLaw(self):
        sons = []
        daughterInLaw = []
        
        for children in self.kids:
            if children.sex == "M":
                sons.append(children)
        
        for i in range (len(sons)):
            if (len(sons[i].wife)) > 0:
                for j in range (len(sons[i].wife)):
                    daughterInLaw.append(sons[i].wife[j].name)

        if (len(daughterInLaw) > 0):    
            return daughterInLaw

        else:
            return "You don't have any daughter-in-law"
    
grandpa = Personal("Ngurah", "M")
grandma = Personal("Seroni", "F")

grandpaMaternal = Personal("Mayura", "M")
grandmaMaternal = Personal("Armini", "F")

dad = Personal("Arjawa", "M")
mom = Personal("Tresna", "F")
me = Personal("Agung Krisna", "M")
brother = Personal("Agung Dwipa", "M")
uncle = Personal("Alit", "M")
aunt = Personal("Putri", "F")
cousin = Personal("Diah", "F")

grandpaMaternal.setWife(grandmaMaternal)
grandpaMaternal.setKid(mom)
grandmaMaternal.setKid(mom)

grandpa.setWife(grandma)
grandpa.setKid(dad)
grandpa.setKid(aunt)
grandma.setKid(dad)
grandma.setKid(aunt)

dad.setWife(mom)
dad.setKid(me)
dad.setKid(brother)
mom.setKid(me)
mom.setKid(brother)

aunt.setHusband(uncle)
aunt.setKid(cousin)
uncle.setKid(cousin)
aunt.husband.pop(1)


print(me.showSiblings())
print(me.showStepSiblings())
print(me.showCousins())
print(me.showGrandma())
print(me.showGrandpa())
print(me.showGrandChildren())
print(me.showSonInLaw())
print(me.showDaughterInLaw())
