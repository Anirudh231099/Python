import json
class base:
    def openfile(self):
        self.fname = open('data.json','r+')

class derived(base):
    def read(self):
        self.data = json.load(self.fname)

    def print(self,details):
        self.data["employee"].append(details)
        self.fname.seek(0)
        json.dump(self.data,self.fname,indent =4)

details={
         "id": "08",
         "name": "Rishab Pant",
         "department": "Cricket"
}

a=derived()
a.openfile()
a.read()
a.print(details)








