#!/bin/python
import facebook
import os 
oauth_access_token="CAACEdEose0cBAMXyvINsk7F2HSIBjQzLg5sIbepdTA9031BzB5DidJZAxAgNxogsjzPb8lCIEWxZAUgFPOQOZBpuBaq0B42H38NWZCRsihwbMW8W5rp06kEFnmjZCOI7aBroPZC0vGcbhZBylqjB9M8BruBO4pq4syiCcJchaWOz8IRZAZAgI6rdPqJyBYCVmEMBRMBuuOZCXv7gZDZD"

graph = facebook.GraphAPI(oauth_access_token)
#friendlistall = graph.get_object("me/friends(name,birthday)")
#friendlist = friendlistall["data"]
profile = graph.get_object("me")
print "ME==>",profile["username"]

directory = profile["username"]
if not os.path.exists(directory):
  os.makedirs(directory)
  print "=> Created Directory:",directory

friends = graph.get_connections("me", "friends")

friend_no = 5
album_counter = 5

for friend in friends["data"]:
  if friend_no is not 0:
    friend_no = friend_no -1
    print "Friend ID: ", friend["id"]
    print "Name: ", friend["name"]
    BaseDir = directory + "/" +friend["name"]
    print "BaseDir:", BaseDir
    BaseDir = BaseDir.replace(" ", "_");
    if not os.path.exists(BaseDir):
      os.makedirs(BaseDir)
      print "=> Created Directory:",BaseDir
    
    #id= friend["id"]
    #print "Birthday", graph.get_object(id)
    #photos = graph.get_object(str(friend["id"])+"/photos")
    albums = graph.get_object(str(friend["id"])+"/albums")["data"]
    #print albums
    for album in albums:
      if album_counter is not 0:
        album_counter = album_counter -1
        AlbumName = album["name"]
        print "Album Name :|", AlbumName
        CurrentDir = BaseDir + "/" + AlbumName
        CurrentDir = CurrentDir.replace(" ", "_");
        if not os.path.exists(CurrentDir):
          os.makedirs(CurrentDir)
          print " => Created Directory:",CurrentDir
        print "Album Details:",album["id"]
        profile_pics = graph.get_object(album["id"])
        pictures = (graph.get_object(album["id"]+"/"+"photos")["data"])
        for picture in pictures:
          for pic in picture["images"]:
            if pic["width"] > 500 or pic["height"] > 500:
              print pic["width"], pic["height"]
              print pic["source"]
              os.system("wget -P "+CurrentDir+" "+pic["source"])
              break
        #os.system("wget "+album["link"]) 
      else:
        break
  else:
    break

print "-"*10
