#Reading File
# import pandas as pd
# data=pd.read_csv("Hello.csv")
# print(pd)
# print(data)


# Writing to the file
# import pandas as pd
# df = pd.DataFrame([[1,'Anirudh', 22], [2,'Rishab Pant', 23]], columns = ['Sno','Name', 'Age'])
# df.to_csv('PandasCSV.csv')


# import pandas
# df = pandas.read_csv('PandasCSV.csv', index_col='Sno')
# print(df)

# import pandas
# df = pandas.read_csv('PandasCSV.csv', header=0,names=['Serial no', 'Employee name', 'Employee age'])
# print(df)


#Only columns
# import pandas
# col_list = ["Sno","Name", "Age"]
# df = pandas.read_csv("PandasCSV.csv", usecols=col_list)
# print(df["Name"])
# print(df["Age"])
# print(df["Sno"])


#Inheritance
import csv
class Player:

    def PlayerDetails(self):
        with open('Hello.csv', newline='') as csvfile:
            data = csv.reader(csvfile, delimiter=' ')
            for row in data:
                print(', '.join(row))

class Sample(Player):

    def Details(self):
        super()

        with open('PandasCSV.csv', newline='') as csvfile:
            data = csv.reader(csvfile, delimiter=' ')
            for row in data:
                print(', '.join(row))


obj = Sample()


print("-----Player Details-----")
obj.PlayerDetails()

print("-----Details-----")
obj.Details()


