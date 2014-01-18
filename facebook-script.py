#!/bin/python
import facebook
import datetime,time
import os
oauth_access_token = "CAACEdEose0cBAPHeQHnJCbljjTufORGhyZAgWRgd3PUuOj4Aa8SpBWSQqPIJRnwwbPd5qvdlvbls9H29KXL0ZBGZALZBVShr5s1j3a0tTZAZATAhGZBZASp8u5FwyU0cEMqeuW96sQzf6MLQaXMGzXgrTnntkK6sBGgaXa77JmSytQJK7hRCRcIjOkCe0MCoIaIFeZCEzW8TIqgZDZD"
#friendlistall = graph.get_object("me/friends(name,birthday)")
#friendlist = friendlistall["data"]
#friendlist = graph.get_object("me/friends")
def main():

  def authenticate():
    try:
      graph = facebook.GraphAPI(oauth_access_token)
      return graph
    except:
      print "Failed to Authenticate!!"

  def get_all_birthdays(graph, friend_no):
    friends_info = []
    friends = graph.get_connections("me", "friends")
    for friend in friends["data"]:
      if friend_no is not 0:
        friend_no = friend_no -1
        try:
          #print "Friend ID: ", friend["id"]
          #print "Name: ", friend["name"]
          birthday =  graph.get_object(friend["id"])["birthday"]
          data = {'id': friend["id"], 'name': friend["name"], 'birthday': birthday }
          #print "=====>", data
          friends_info.append(data)
        except:
          pass
          #print "No birthday"
      else:
        return friends_info

  def within_range(friends_info,shipping_time):
    birthday_people = []
    now = datetime.datetime.now()
    print now.strftime("%m/%d")
    print now.year, "--", now.month, "--", now.day
    while shipping_time is not 0:
      shipping_time = shipping_time - 1
      for friend in friends_info:
        print friend
        if friend["birthday"] is now.strftime("%m/%d"):
            birthday_people.append(friend)
            print "Birthday Eligible Person :", friend["name"]
    return birthday_people 

  def create_main_directory(graph):
    profile = graph.get_object("me")
    print "ME==>",profile["username"]
    directory = profile["username"]
    if not os.path.exists(directory):
      os.makedirs(directory)
      print "=> Created Directory:",directory

  def get_data(graph, person_id, person_name, album_max):
    #print "Friend ID: ", friend["id"]
    #print "Name: ", friend["name"]
    BaseDir = directory + "/" +person_name
    print "BaseDir:", BaseDir
    BaseDir = BaseDir.replace(" ", "_");
    if not os.path.exists(BaseDir):
      os.makedirs(BaseDir)
      print "=> Created Directory:",BaseDir

    albums = graph.get_object(str(person_id)+"/albums")["data"]
    #print albums
    for album in albums:
      if album_max is not 0:
        album_max = album_max -1
        AlbumName = album["name"]
        print "Album Name :|", AlbumName
        CurrentDir = BaseDir
        #CurrentDir = BaseDir + "/" + AlbumName
        #CurrentDir = CurrentDir.replace(" ", "_");
        #if not os.path.exists(CurrentDir):
        #  os.makedirs(CurrentDir)
        #  print " => Created Directory:",CurrentDir
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
        os.system("wget "+album["link"]) 
      else:
        break
    return CurrentDir

  def create_collage(person_name):
    Dir = CurrentDir
    os.system("echo Run Collage Command Here!!") 

  def get_collage(graph,person_id, person_name, album_max):
    print "Getting Information of %s", person_name
    get_data(graph, person_id, person_name, album_max)
    create_collage(person_name)

#================== Function Code =========================
  friend_no = 10 # Number of friends
  shipping_time = 5 # Days
  album_max = 2 # Maximum number of Albums to be downloaded
  graph  = authenticate()
  friends_info = get_all_birthdays(graph, friend_no)
  print friends_info
  birthday_people = within_range(friends_info, shipping_time)
  create_main_directory(graph)
  for person in birthday_people:
    print "Get Collage for %s" % person["name"]
    get_collage(graph, person["id"], person["name"], album_max)


if __name__ == "__main__":
      main()
