#import intro_game.text, skills_game.text

class Land(object):
    #get into land?
    def enter(self):
    pass
    exit(1)
    
    def __init__(self, bank):
        self.bank = bank
    
        
    def bank(bank_balance):
    bank_balance = 7000
        print "Your bank balance is:", (bank_balance) 
        
    def Code_knowledge(code_no):
        code_no = 30
        print "Your code knowledge is:", (code_no)
    
    def Rock_star_state(code_no):
        if code_no >= 100:
            rock_star == true
            if rock_star == true:
                RockStar.enter()

        
class OpeningLand(Land):
    print "you work at Beach and are learning to code a little bit everyday."
    print "You want to learn alot more so you can get a job."
    print "What should you do you?"
    print "Your bank balance is $", (bank_balance)
    print "1. pay a lot for code school?"
    print "2. work for free at an internship?"
    print "3. get a paid internship?"
    print "4. keep on coding at home until you think you are a ninja?"
    
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
    print "for each month you stay home and code you save $400"
    print "and gain 20 rockstar points"
    print "How many months do you stay home and code?"
    
    raw_input(">") == months_at_home
    
    if months_at_home == 1:
        code_no += 20
        print "Your code knowledge is: ", (code_no)
        print "You should keep coding... and reconsider your options"
    if months_at_home == 2:
        code_no += 20
        print "Your code knowledge is: ", (code_no)
        print "You should keep coding... and reconsider your options"
    if months_at_home == 3:
        code_no += 20
        print "Your code knowledge is: ", (code_no)
        print "You should keep coding... you will be a rockstar soon!"
    if months_at_home == 4:
        code_no += 20
        print "Your code knowledge is: ", (code_no)
        print "Great job! You are a Rockstar now!"
        RockStar.enter()
        
        #should this be indented here?
        print "Do you want to reconsider your career options?"
    
        raw_input(">") == career_choice
    
        if career_choice == "YES":
        OpeningLand.enter()
        
        if career_choice == "NO":
        print "I guess you aren't really that interested in becoming"
        print "a programmer. Enjoy sewing those dirty cloths in the dark!"
        #exit game
    
    else:
        print "Enter 1-10"
     

    def __init__(self, bank):
    pass
   #when does bank balance get called?
    def bank(bank_balance):# should this be an object?
        bank_balance += 400 * months_at_home
        print "Your bank balance is:", (bank_balance)
    
    #should code no go in here?    
    def Code_knowledge(months_at_home): #object or method?
    #does this go here?
    def Rock_star_state(code_no):
    
class UnpaidInternship(Land):

    print "Not working costs money"
    bank_balance -= $3600 
    bank()
    
    print "Do you take a job at the co. you interned with?"
    
    raw_input(">") = job_status
    
    if job_status == "YES"
      get_job = 2500
      bank_balance += get_job
      bank()
    else:
      time_to_find_work = randint(1, 6) * -1200
      bank_balance -= time_to_find_work
      bank()
   
  
class PaidInternship(Land):
print "You have earned a tiny amount of money"
    bank_balance += 3200 
    bank()
    
    print "Do you take a job at the co. you interned with?"
    
    raw_input(">") = job_status
    
    if job_status == "YES"
      get_job = 2500
      bank_balance += get_job
      bank()
    else:
      time_to_find_work = randint(1, 6) * -1200
      bank_balance -= time_to_find_work
      bank()


class CodeSchool(Land)
    print "Did you get a scholarship?"
    raw_input(">") = scholarship
    
    if scholarship == "YES" #Hackbright
    
    bank_balance -= $3600 
    bank()
        
    else: #app academy
    bank_balance -= $3600 
    bank_balance -= $18000
    bank()

    
    print "Do you take a job at a partner company?"
    
    raw_input(">") = job_status
    
    if job_status == "YES" and 
      get_job = 2500
      bank_balance += get_job
      bank()
    else:
      time_to_find_work = randint(1, 6) * -1200
      bank_balance -= time_to_find_work
      bank()
      get_job = 2500
      bank_balance += get_job
      bank()

class Rockstar(Land)
    bank_balance += 
    bank()
    
    
class Map(object):

    lands = [HomeCoder, CodeSchool, PaidInternship, UpaidInternship,   Rockstar]
    
    
    