#!/bin/python
import facebook
oauth_access_token = "CAACEdEose0cBAEV42kcZChyDjJS66jRojPECe2fdZAwojIKyNgVUYJlrwoQeEHIFUJ4qyHMjaFbYWLAsNMnRHOtV1MKRX8AWKu2gE78KH70ThY9dTzEN2jF6RY273e4DM3pbBZCl1ed4pRRW8wGnXPFR3C1L38ogXn16lOJ4xUwf7OBHZCfxJLD4LFbAvtWDBY45Pw2xTQZDZD"

graph = facebook.GraphAPI(oauth_access_token)
#friendlistall = graph.get_object("me/friends(name,birthday)")
#friendlist = friendlistall["data"]
#friendlist = graph.get_object("me/friends")


friends = graph.get_connections("me", "friends")



for friend in friends["data"]:
  print "-"*10
  print "Friend ID: ", friend["id"]
  print "Name: ", friend["name"]
  try:
    print "Birthday", graph.get_object(friend["id"])["birthday"])
  except:
    print "No birthday"
  #print friend.get_birthday()
  print "-"*10
