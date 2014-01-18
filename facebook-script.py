#!/bin/python
import facebook
oauth_access_token = "CAACEdEose0cBAGD7M30FPP7NeZAVrpkLoNbx9focFdQ8O3sdQqJKFtCrACZAZB1d8GHLHHZBlhvwfftwoxNBAEUeBaawJZAMa8aqZBivYQJLtZAZBOVNqHVbbRlXCIP6eKmS4uZB94ClTZBIo0iRoJhppZAvK46b0Ljadv61F3IHHvyOaplP4kZCOefzQbTtlv4lCA3o0vGva8QSQAZDZD"

 
graph = facebook.GraphAPI(oauth_access_token)
profile = graph.get_object("me")
friends_data = graph.get_object("me/friends")
print friends_data

'''
data = feed["data"]
Thanks = ["Thanks a lot :)","Thanks a ton!!","Thanks for the wishes!!"]
print "="*50
i = 0
print "="*50 
for x in data:
  i = i + 1
 # message = x["message"]
  sender= (x["from"]["name"])
#  try:
#    sender = unicode(sender, "utf-8")
#  except TypeError:
#    sender = unicode(sender, "ascii")
#  else:
#    # value was valid ASCII data
#    pass


#  value = unicode(sender, "utf-8")
#  print sender
#  print x["updated_time"] ,"=>",sender, "=>", message ,"=>", x["id"] ,"=>" ,Thanks[i%3]
 # Like the post and write comments
  graph.put_like(x["id"])  
  graph.put_comment(x["id"],Thanks[i%3])  
print "="*50 '''
