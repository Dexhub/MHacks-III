#!/bin/python
import facebook
oauth_access_token = "CAACEdEose0cBAIWLdY15VT6yZBeBbQCo6o2MnaZCtU0Ql5Bo7fwiPev621KHRzmqxtliDGZAZAI1mTLYpBueI4ixibhT8xofmB4BZBBOtoCiYzKYjv2OA3G74RrMWrohAFfPYKkoXkGiDSJVb8EoTbprGcezSIklZCbHZAzZArxcd9kLtgDtDOXWcAoGVHEo7KYZAO25KRHokGwZDZD"

graph = facebook.GraphAPI(oauth_access_token)
#friendlistall = graph.get_object("me/friends(name,birthday)")
#friendlist = friendlistall["data"]
#friendlist = graph.get_object("me/friends")


friends = graph.get_connections("me", "friends")

friend_no = 5


for friend in friends["data"]:
  if friend_no is not 0:
    friend_no = friend_no -1
    try:
    #print "-"*10
      print "Friend ID: ", friend["id"]
      print "Name: ", friend["name"]
      print "Birthday", graph.get_object(friend["id"])["birthday"]
  #print request(self, friend["id"], args=birthday)
    #print graph.get_object(friend["id"],birthday)
    except:
      print "No birthday"
  #print friend.get_birthday()
  else:
    break

print "-"*10
