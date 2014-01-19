#!/bin/python
import facebook
import datetime,time
import os
import lob

lob.api_key = "test_204515ce2c65d12b8ae9eea9f10f2edcba5"
oauth_access_token = "CAACEdEose0cBADNgZBZA8CDxgiCSoqmFLPFm1oT2Ch6kk251mbGVkrMo2ZCannPywNbybEZBsyqk3z0BifXSZBd7KPntZBUmD98TxHjMTIcS95ZCuTgEQkdWUgFm92FqCZBofYF1mBqHIxapSWVJlsgeTUynCpuYNosDjIAr4WUEffIQbi7gk4aDbuu466NVA5e2PePIhM4r8AZDZD"
#friendlistall = graph.get_object("me/friends(name,birthday)")
#friendlist = friendlistall["data"]
#friendlist = graph.get_object("me/friends")
def main():
  global from_add
  from_add = {
            'name': 'Himanshu Shah',
            'address_line1': '14, Beverly Hills',
            'address_line2': 'Palm Villas',
            'address_city': 'Los Angeles',
            'address_state': 'CA',
            'address_country': 'US',
            'address_zip': '02125'
        }
  def get_my_option(choices):
    # The format of Choices i for each 
    # choice["id"],
    # choice["name"],
    # choice["selection"] = 101 -> Color Document - 8.500 X 11 
    #                     = 305 -> Posters - 11 X 17 
    #                     = 306 -> Posters - 18 X 24 
    #                     = 307 -> Posters - 24 x 36 
    #                     = 502 -> Poster - 8 x 10 
    #                     = 700 -> Mug - 8.58 X 3.7
    #                     = 1 -> Post Card - 8.58 X 3.7
    # choice["delivery"] = 0 -> Email
    #                      1 -> Delivery
    # choice["address"] = if its Delivery
    # choice["email"] =  is its Email

    for choice in choices:
      sel = choice["selection"]
      if sel == 305:
        print "Poster Selected"
        invoke_Poster(choice, width = 11, height = 17)
      elif sel == 306:
        print "Poster Selected"
        invoke_Poster(choice, width = 18, height = 24)
      elif sel == 307:
        print "Poster Selected"
        invoke_Poster(choice, width = 24, height = 36)
      elif sel == 502:
        print "Poster Selected"
        invoke_Poster(choice, width = 8, height = 10)
      elif sel == 700:
        print "Mug Selected"
        invoke_Mug(choice)
      elif sel == 1:
        print "PostCard Selected"
        invoke_Postcard(choice)
      else:
        print "Choice --> ", choice
        print "Choices --> ", choices
        print "Invalid choice"
    return

  def invoke_Poster(choice ,width = 18, height = 24 ):
    person_id = choice["id"]
    person_name = choice["name"]
    graph = authenticate()
    CurrentDir = get_data(graph, person_id, person_name, album_max = 5, directory="vin.jay.90")
    create_collage(CurrentDir)
    image_name = "collage.jpg"
    convert_pdf(image_name, width, height)
    #TODO if choice["delivery"] is 0:
    #  email = choice["email"]
    #else if choice["delivery"]
    to_add = choice["address"]

    output = open("temp.pdf", 'rb')
    print_object("Poster_print", output, from_add, to_add, choice_id = 2)
    return


  def invoke_Postcard(choice):
    person_id = choice["id"]
    person_name = choice["name"]
    address = choice["address"]
    graph = authenticate()
    CurrentDir = get_data(graph, person_id, person_name, album_max = 1, max_photos = 1, directory="vin.jay.90")
    image_name = "profile.jpg"
    create_frontpdf(address) 
    create_backpdf(image_name) 
    #pc_front.pdf
    #pc_back.pdf
    front = open("PC_front.pdf", 'rb')
    back = open("PC_back.pdf", 'rb')
    to_add = address
    send_postcard("Post_card_print", front, back, from_add, to_add)

    

  def invoke_Mug(choice):
    person_id = choice["id"]
    person_name = choice["name"]
    to_add = choice["address"]
    graph = authenticate()
    CurrentDir = get_data(graph, person_id, person_name, album_max = 1, max_photos = 1, directory="vin.jay.90")
    image_name = "profile.jpg"
    create_mug_pdf(image_name)
    #mug_file = CurrentDir+"/mug.pdf"
    mug_file = open("mug.pdf", 'rb')
    global from_add
    print_object("Mug_File", mug_file, from_add, to_add, choice_id = 15, quantity = 1)
  
  def create_frontpdf(toaddress_full,fromaddress_full = from_add):
#  (to_name, to_street_address, to_city, to_state, to_zip_code, from_name, from_street_address, from_city, from_state, from_zip_code):
# 
#
#  tempaddr1 = {
#            'name': 'Siddharth Saha',
#            'address_line': '220 William T Morrissey, Sunset Town',
#            'address_city': 'Boston',
#            'address_state': 'MA',
#            'address_country': 'US',
#            'address_zip': '02125'
#        }

      to_name = toaddress_full["name"]
      to_street_address = toaddress_full["address_line1"]
      to_city = toaddress_full["address_city"]
      to_state = toaddress_full["address_state"]
      to_zip_code = toaddress_full["address_zip"]
  
      from_name = fromaddress_full["name"]
      from_street_address = fromaddress_full["address_line1"]
      from_city = fromaddress_full["address_city"]
      from_state = fromaddress_full["address_state"]
      from_zip_code = fromaddress_full["address_zip"]
      
      from reportlab.pdfgen import canvas
      from reportlab.lib.units import inch
      from reportlab.lib.colors import black, white
  
      #CREATE THE FRONT SIDE
      canvas = canvas.Canvas("PC_front.pdf")
      canvas.setLineWidth(.3)
      canvas.setFont('Helvetica', 10)
      canvas.setPageSize((6*inch, 4*inch))
  
      #Border and Stamp
      canvas.setFillColor(white)
      canvas.rect(0.1*inch, 0.1*inch, 5.8*inch, 3.8*inch, stroke=1, fill=1)
      #canvas.rect(4.8*inch, 2.8*inch, 0.85*inch, 0.85*inch, stroke=1, fill=1)
  
      #Center Line
      canvas.line(3*inch, 0.5*inch, 3*inch, 3.5*inch)
  
      #To Address Lines (5 nos)
      
      canvas.setFillColor(black)
      canvas.drawString(3.4*inch, 3.4*inch,'To,')
      canvas.drawString(3.5*inch, 3.2*inch,to_name)
      canvas.drawString(3.5*inch, 3.0*inch,to_street_address)
      canvas.drawString(3.5*inch, 2.8*inch,to_city)
      canvas.drawString(3.5*inch, 2.6*inch,to_state)
      canvas.drawString(3.5*inch, 2.4*inch,to_zip_code)
  
      #From Address Lines (5 nos)
      
      canvas.setFillColor(black)
      canvas.drawString(3.4*inch, 2.0*inch,'From,')
      canvas.drawString(3.5*inch, 1.8*inch,from_name)
      canvas.drawString(3.5*inch, 1.6*inch,from_street_address)
      canvas.drawString(3.5*inch, 1.4*inch,from_city)
      canvas.drawString(3.5*inch, 1.2*inch,from_state)
      canvas.drawString(3.5*inch, 1.0*inch,from_zip_code)
  
      canvas.setFont('Helvetica', 18)
      canvas.drawString(0.5*inch, 2.5*inch,'Many Many Happy ')
      canvas.drawString(0.5*inch, 2.0*inch,'Returns of the Day')
      
  
      canvas.save()
      
  def create_backpdf(image_name):
  
      from reportlab.pdfgen import canvas
      from reportlab.lib.units import inch
      
      canvas = canvas.Canvas('PC_back.pdf')
      canvas.setPageSize((6*inch, 4*inch))
      canvas.drawImage(image_name, 0.1*inch, 0.1*inch, 5.9*inch, 3.9*inch)
      canvas.showPage()
      canvas.save()
  
  def create_mug_pdf(image_name):
  
      from reportlab.pdfgen import canvas
      from reportlab.lib.units import inch
      
      canvas = canvas.Canvas('mug.pdf')
      canvas.setPageSize((8.58*inch, 3.7*inch))
      canvas.drawImage(image_name, 0.1*inch, 0.1*inch, 5.9*inch, 3.9*inch)
      canvas.showPage()
      canvas.save()
  
  def convert_pdf(image_name, width, height):
  
      from reportlab.pdfgen import canvas
      from reportlab.lib.units import inch
      
      canvas = canvas.Canvas('output.pdf')
      canvas.setPageSize((width*inch, height*inch))
      canvas.drawImage(image_name, 0.1*inch, 0.1*inch, (width-0.1)*inch, (height-0.1)*inch)
      canvas.showPage()
      canvas.save()
  
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

  def get_data(graph, person_id, person_name, album_max = 5, max_photos = 16, directory="vin.jay.90"):
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
          if max_photos is 1:
            max_photos = max_photos - 1
            for pic in picture["images"]:
              if pic["width"] > 500 or pic["height"] > 500:
                print pic["width"], pic["height"]
                print pic["source"]
                os.system("wget -P "+CurrentDir+" -O profile.jpg "+pic["source"])
                break
          if max_photos is not 0:
            max_photos = max_photos - 1
            for pic in picture["images"]:
              if pic["width"] > 500 or pic["height"] > 500:
                print pic["width"], pic["height"]
                print pic["source"]
                os.system("wget -P "+CurrentDir+" "+pic["source"])
                break
          else:
            break
        #os.system("wget "+album["link"]) 
      else:
        break
    return CurrentDir

  def create_collage(currentdir):
    path = currentdir+"/*.jpg"
    print "Path: ", path
    Command = "montage -resize 100x150 "+path+ " -geometry +3+3 -tile 4x4 -shadow collage.jpg"
    os.system(Command) 

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
    object_created = lob.Object.create(name = job_name, file = pdf_file,
    setting_id=lob.Setting.list()[choice_id].id, quantity=1).to_dict()
    print setting_id
    print Setting.list()[choice_id].id
    last = len(lob.Object.list())
    print "Job Created", lob.Job.create(name = job_name, to = to_add,
                         objects=lob.Object.list()[last-1].id, from_address = from_add).to_dict()

  def send_postcard(job_name, front, back, from_add, to_add):
    print "===="*10, from_add
    print "Post Card", lob.Postcard.create(name = job_name, to = to_add, front = front,
                                                              back = back,
                                                              from_address= from_add).to_dict()
    
    

#================== Function Code =========================
  friend_no = 10 # Number of friends
  shipping_time = 5 # Days
  album_max = 2 # Maximum number of Albums to be downloaded
  graph  = authenticate()
  friends_info = get_all_birthdays(graph, friend_no)
  #print friends_info
  tempaddr1 = {
            'name': 'Siddharth Saha',
            'address_line1': '220 William T Morrissey',
            'address_line2': 'Sunset Town',
            'address_city': 'Boston',
            'address_state': 'MA',
            'address_country': 'US',
            'address_zip': '02125'
        }
  choices = [{'id': '1306797872', 'name': 'Kaylee Marie Allen' ,'address':tempaddr1, 'delivery': 1, 'selection': 305 }]             
  get_my_option(choices)
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
  to_addr = {
            'name': 'Siddharth Saha',
            'address_line1': '220 William T Morrissey',
            'address_line2': 'Sunset Town',
            'address_city': 'Boston',
            'address_state': 'MA',
            'address_country': 'US',
            'address_zip': '02125'
        }




#  name_job = 'Post Card New code'
#  file_pdf = "http://www.cs.stonybrook.edu/~hkshah/PDF/CV.pdf"
#  front_pdf = open('./front.pdf','rb')
#  back_pdf = open('./front.pdf','rb')
#  send_postcard(job_name= name_job, front = front_pdf, back = back_pdf, from_add = from_addr, to_add= to_addr)




#  print lob.Object.list()
  #print address.to_dict()
  #print lob.Address.list()





  #print lob.Postcard.list()


if __name__ == "__main__":
      main()
