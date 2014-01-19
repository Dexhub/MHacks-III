#!/bin/python
import facebook
import datetime,time
import os
import lob

lob.api_key = "test_204515ce2c65d12b8ae9eea9f10f2edcba5"
oauth_access_token = "CAACEdEose0cBAEBsaDIxzjrufURJ5HkWIkp5x3aKx6CLFxakbJTWg4myYNZBOCmZANkVKOcX4WXAI8MWpQNgbCMpLk85s48Xg2wLtZAvuvgLUStqygQqrNsgGBUnKrzsRO8a7iNg0CWxZCIIfB8gLjWZCZBVu16s4mBul3koBiyJARXnldaxtEoTheazL0fBcHewEcUi8A1QZDZD"
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
        #print "===>", friend
        if friend["birthday"] is not now.strftime("%m/%d"): # hk ===> Fix this date thing
            birthday_people.append(friend)
            print "Birthday Eligible Person :", friend["name"]
    return birthday_people 

  def create_main_directory(graph):
    profile = graph.get_object("me")
    #print "ME==>",profile["username"]
    directory = profile["username"]
    if not os.path.exists(directory):
      os.makedirs(directory)
      #print "=> Created Directory:",directory
    return directory

  def get_data(graph, person_id, person_name, album_max, directory):
    #print "Friend ID: ", friend["id"]
    #print "Name: ", friend["name"]
    BaseDir = directory + "/" +person_name
    #print "BaseDir:", BaseDir
    BaseDir = BaseDir.replace(" ", "_");
    if not os.path.exists(BaseDir):
      os.makedirs(BaseDir)
      #print "=> Created Directory:",BaseDir

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
        #os.system("wget "+album["link"]) 
      else:
        break
    return CurrentDir

  def create_collage(person_name):
    #Dir = CurrentDir
    os.system("echo Run Collage Command Here!!") 

  def get_collage(graph,person_id, person_name, album_max, directory):
    print "Getting Information of ", person_name
    get_data(graph, person_id, person_name, album_max, directory)
    create_collage(person_name)

#  def what_type_object():
#    print lob.Service.list()
#    for service in lob.Service.list():
#      dir(service)
#      #print service
#      print x[0].id
#    print lob.setting.list() 
  
  def print_object(job_name, pdf_file, from_add, to_add, choice_id = 0, quantity = 1):
    #print sender_name
    #print from_add

    object_created = lob.Object.create(name = job_name, file = pdf_file,
    setting_id=lob.Setting.list()[0].id, quantity=1).to_dict()
    last = len(lob.Object.list())
    print "Job Created", lob.Job.create(name = job_name, to = to_add,
                         objects=lob.Object.list()[last-1].id, from_address = from_add).to_dict()
#    print "Object Created : ", object_created
   
#    print "Job Created: ", (lob.Job.create(sender_name, from_add,
#                         object_created, from_address=from_add)).to_dict()

   # print "Job Created", lob.Job.create(name = sender_name, to=lob.Address.list(count=1)[0].id,
   #                      objects=lob.Object.list()[last-1].id, from_address=lob.Address.list(count=1,
   #                                                                                     offset=5)[0].id).to_dict()

  def send_postcard(job_name, front, back, from_add, to_add):
    print "Post Card", lob.Postcard.create(name = job_name, to = to_add, front = front,
                                                              back = back,
                                                              from_address= from_add).to_dict()
    
    

#================== Function Code =========================
#  friend_no = 10 # Number of friends
#  shipping_time = 5 # Days
#  album_max = 2 # Maximum number of Albums to be downloaded
#  graph  = authenticate()
#  friends_info = get_all_birthdays(graph, friend_no)
#  #print friends_info
#  birthday_people = within_range(friends_info, shipping_time)
#  directory = create_main_directory(graph)
#  for person in birthday_people:
#    print "Get Collage for %s" % person["name"]
#    get_collage(graph, person["id"], person["name"], album_max, directory)
#
##################### Abhinav Tests ################
#hk = User()
####################################################

    ################ after creating a post card 

  ## Code for lob
  from_addr = {
            'name': 'Siddharth Saha',
            'address_line1': '220 William T Morrissey',
            'address_line2': 'Sunset Town',
            'address_city': 'Boston',
            'address_state': 'MA',
            'address_country': 'US',
            'address_zip': '02125'
        }
  to_addr = {
            'name': 'Siddharth Saha',
            'address_line1': '220 William T Morrissey',
            'address_line2': 'Sunset Town',
            'address_city': 'Boston',
            'address_state': 'MA',
            'address_country': 'US',
            'address_zip': '02125'
        }
  name_job = 'Post Card New code'
  file_pdf = "http://www.cs.stonybrook.edu/~hkshah/PDF/CV.pdf"
  #back_pdf = "PC_front.pdf"
  #back_pdf  = "/home/dexter/scripts/temp/wishme-thankyou/my-test/Hackathon-MHacks/PC_front.pdf"
  #front_pdf = "/home/dexter/scripts/temp/wishme-thankyou/my-test/Hackathon-MHacks/PC_front.pdf"
  #front_pdf = "http://www.joshuanoll.com:4334/front.pdf"
  front_pdf = open('./front.pdf','rb')
  back_pdf = open('./front.pdf','rb')
  #back_pdf = "/home/dexter/scripts/temp/wishme-thankyou/my-test/Hackathon-MHacks/front.pdf"
  #front_pdf = "http://100startup.com/resources/business-plan.pdf"
  #print_object(job_name = name_job, pdf_file = file_pdf, from_add = from_addr, to_add =  to_addr)
  send_postcard(job_name= name_job, front = front_pdf, back = back_pdf, from_add = from_addr, to_add= to_addr)




#  print lob.Object.list()
  #print address.to_dict()
  #print lob.Address.list()





  #print lob.Postcard.list()


if __name__ == "__main__":
      main()
