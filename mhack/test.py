from django.db import models

# Create your models here.
class User:
    name = models.CharField(max_length=30)
    birthday = models.CharField(max_length=30)
    def __init__(self,name,bday):
        self.name=name
        self.birthday=bday
        print (self.name)
        print(self.birthday)
class temp:
    def __init__(self,obj):
        userList=[]
        for x in obj:
            self.name=x['name']
            self.birthday=x['birthday']
            u=User(self.name,self.birthday)
            userList.append(u)

friends_info = [{'birthday': '04/06', 'id': '517614939', 'name': 'Shannon Hunter'}, {'birthday': '07/14/1994', 'id': '1306797872', 'name': 'Kaylee Marie Allen'}, {'birthday': '09/15', 'id': '100000073500871', 'name': 'Jada Leigh'}, {'birthday': '09/07/1994', 'id': '100000351939887', 'name': 'April Roulette'}, {'birthday': '12/22', 'id': '100001348159093', 'name': 'Heidi Butler'}, {'birthday': '09/06/1995', 'id': '100001361974023', 'name': 'Xena Roulette'}, {'birthday': '12/22', 'id': '100001402788224', 'name': 'Sammy Leckie'}, {'birthday': '07/03', 'id': '100002690531733', 'name': 'Mercedes Heaven Beaar'}, {'birthday': '07/15/1994', 'id': '100002957226119', 'name': 'Savanah Littlejohn'}]
tem=temp(friends_info)



		
			


