import json
class base:
    def openfile(self):
        self.fname = open('Image.json','r+')

class derived(base):
    def read(self):
        self.data = json.load(self.fname)

    def print(self,details):
        self.data["image"].append(details)
        self.fname.seek(0)
        json.dump(self.data,self.fname,indent =4)

details={
        "file name": "Facebook pic",
        "file size": "4MB",
        "img resolution": "420p",
        "img pixels": "800",
        "camera": "one plus "
    }

a=derived()
a.openfile()
a.read()
a.print(details)
