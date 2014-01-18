#!/bin/python
import facebook
oauth_access_token = "CAACEdEose0cBAMXyvINsk7F2HSIBjQzLg5sIbepdTA9031BzB5DidJZAxAgNxogsjzPb8lCIEWxZAUgFPOQOZBpuBaq0B42H38NWZCRsihwbMW8W5rp06kEFnmjZCOI7aBroPZC0vGcbhZBylqjB9M8BruBO4pq4syiCcJchaWOz8IRZAZAgI6rdPqJyBYCVmEMBRMBuuOZCXv7gZDZD"
graph = facebook.GraphAPI(oauth_access_token)
#friendlistall = graph.get_object("me/friends(name,birthday)")
#friendlist = friendlistall["data"]
#friendlist = graph.get_object("me/friends")


friends = graph.get_connections("me", "friends")

friend_no = 1


for friend in friends["data"]:
  if friend_no is not 0:
    friend_no = friend_no -1
    try:
    #print "-"*10
      print "Friend ID: ", friend["id"]
      print "Name: ", friend["name"]
      #print "Birthday", graph.get_object(friend["id"])["birthday"]
      print "Birthday", graph.get_object(friend["id"],name,friends.fields(picture))
    except:
      print "No birthday"
  #print friend.get_birthday()
  else:
    break

print "-"*10
