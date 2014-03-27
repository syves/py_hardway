#import intro_game.text, skills_game.text
from sys import exit
from random import randint

#balance_balance = 8400
#code_no = 30

#base class for lands        
class Land(object):
    #get into land?
    def enter(self):
    #prints a string here for each land
    exit(1)

        
account = 8400  
code_no = 30
        
        #where does this go?
def rockstarState(code_no)
      if code_no >= 100:
          Rockstar == True

#instance of a land, inherits enter() from Land       
class OpeningLand(Land):

    def enter(self):
      print "you are learning to code a little bit everyday."
      print "You want to learn a lot more so you can get a job."
      print "What should you do you?"
      print "Your bank balance is $", (bank_balance)
      print "1. pay a lot for code school?"
      print "2. work for free at an internship?"
      print "3. get a paid internship?"
      print "4. keep on coding at home until you are a Rockstar?"
    
      raw_input(">") == next_land
    
      if next_land == "1":
          CodeSchool.enter()
        
      if next_land == "2":
          UnpaidInternship.enter()
    
      if next_land == "3":
         PaidInternship.enter()
     
      if next_land == "4":
          HomeCoder.enter()
        
Class HomeCoder(Land):
    #can this go before raw input months_at_home collected?
    
        
        
    
    def enter(self):
      print "for each month you stay home and code you save $400"
      print "and gain 20 rockstar points"
      print "How many months do you stay home and code?"
    
      raw_input(">") == months_at_home
      
      account += 400 * months_at_home
        print "Your bank balance is:", (bank_balance)
        
        code_no += 20 * months_at_home
            
            
      if months_at_home == "1":
          print "Your code knowledge is: ", (code_no)
          print "You should keep coding... and reconsider your options"
      if months_at_home == "2":
          print "Your code knowledge is: ", (code_no)
          print "You should keep coding... and reconsider your options"
      if months_at_home == "3":
          print "Your code knowledge is: ", (code_no)
          print "You should keep coding... you will be a rockstar soon!"
      if months_at_home == "4":
          print "Your code knowledge is: ", (code_no)
          print "Great job! You are a Rockstar now!"
          
      rockstarState()
          if rockstarState():
              Rockstar.enter()

         #should this be indented here?
          print "Do you want to reconsider your career options?"
    
          raw_input(">") == career_choice
    
          if career_choice == "YES":
              OpeningLand.enter()
        
          if career_choice == "NO":
              print "I guess you aren't really that interested in becoming"
              print "a programmer. Enjoy sewing those dirty cloths in" 
              print "the dark!"
          exit(1)
    
      else:
          print "Please Enter 1-10"
     
class UnpaidInternship(Land):

    def enter(self)
    
        bank_balance -= $3600 
        code_no += 70
        
       "Not working costs money!"
        print "Your bank balance is:{} at the end of the internship".format(bank_balance)
        print "You did learn a great deal! your code knowledeg is :{}".format(code_no)
        
        print "Do you take a job at the company you interned with?"
    
        raw_input(">") = job_status
    
        if job_status == "YES"
            get_job = 2500
            bank_balance += get_job
            "Your bank balance is:{} You got a signing bonus!".format(bank_balance)          
                      
        else:
            time_to_find_work = randint(1, 6) * -1200
            bank_balance -= time_to_find_work
            print "Not working costs money!"
            print "Your bank balance is:{} after 'blank time' looking for work".format(bank_balance)
          rockstarState()
              if rockstarState():
                    Rockstar.enter()
   
  
class PaidInternship(Land):

    def enter(self):
        bank_balance += 3200
        code_no = += 70
        print "You have earned a tiny amount of money.Your bank balance is:{} ".format(bank_balance)
        print "You did learn a great deal! your code knowledeg is :{}".format(code_no
    
        print "Do you take a job at the co. you interned with?"
    
        raw_input(">") = job_status
    
        if job_status == "YES"
            get_job = 2500
            bank_balance += get_job
            "Your bank balance is:{} You got a signing bonus!".format(bank_balance)

        else:
            time_to_find_work = randint(1, 6) * -1200
            bank_balance -= time_to_find_work
            print "Not working costs money!"
            print "Your bank balance is:{} after 'blank time' looking for work".format(bank_balance)
        
        rockstarState()
            if rockstarState():
                Rockstar.enter()

class CodeSchool(Land)

    def enter(self):
    
        bank_balance -= $3600 
        code_no += 70
        
        print "Did you get a scholarship?"
        raw_input(">") = scholarship
    
        if scholarship == "YES" #Hackbright
    
            
            "Not working costs money!"
            print "Your bank balance is:{} at the end of the internship".format(bank_balance)
            print "You did learn a great deal! your code knowledeg is :{}".format(code_no)
        
        else: #app academy
        
            bank_balance -= $3600 
            #bank_balance -= $18000
            "Not working costs money!"
            print "Your bank balance is:{} at the end of the internship, and {} after you pay your tuition".format(bank_balance, bank_balance -= $18000)
            print "You did learn a great deal! your code knowledeg is :{}".format(code_no)
            
        print "Do you take a job at a partner company?"
    
        raw_input(">") = job_status
    
        if job_status == "YES" and 
            get_job = 2500
            bank_balance += get_job
            "Your bank balance is:{} You got a signing bonus!".format(bank_balance)

        else:
            time_to_find_work = randint(1, 6) * -1200
            bank_balance -= time_to_find_work
            print "Not working costs money!"
            print "Your bank balance is:{} after 'blank time' looking for work".format(bank_balance)

            get_job = 2500
            bank_balance += get_job
            "Your bank balance is:{} You got a signing bonus!Your bank balance is:{} ".format(bank_balance)
        
        rockstarState()
            if rockstarState():
                Rockstar.enter()


class Rockstar(Land)
    def enter(self):
        salary = 80000
        taxes = .64
        bank_balance += salary * taxes
        print"You are a Rockstar!"
        print "Your hardwork paid off! You got a great contract. At the end of the year you've earned: {}, Your bank balance is:{} ".format(salary, bank_balance)

        exit(1)
    
    
class LandMap(object):

    lands = [OpeningLand, HomeCoder, CodeSchool, PaidInternship, UpaidInternship]

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass

        
class Engine(object):
    
    def __init__(self, land_map):
        self.land_map = land_map
        
    def play(self):
        #current_scene = self.scene_map.opening_scene()
    #while loop?

        
#a_map = Map('OpeningLand')
#a_game = Engine(a_map)
#a_game.play()
    
    
    