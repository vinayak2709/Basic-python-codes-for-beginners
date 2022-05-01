# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 19:29:21 2021

@author: Vinayak
"""

class Human:
    number_eyes=2
    inteligence_than_animal="SMART"
    number_of_hands=2
    age_inc=1

       
    def __init__(self,name_argument="test_name",gender_argument="M/F",age_argument="0"):
        self.name=name_argument
        self.gender=gender_argument
        self.age=age_argument
        self.own_fav_values=None
        self.iq=100
        self.qualification=None
        self.profession_value=None
        self.weight_increment_value=1
        self.weight_in_kg=1
        self.nationality_value="birth nation"
        print("name = ",self.name," gender= ",self.gender,"age= ",self.age)
    
    
    def show_details(self):
        print("Details are , name = ",self.name,", gender= ",self.gender,", age= ",self.age)
        print(" fav things sweets & ",self.own_fav_values)
        print("all time favourtites :: ")
        Human.favourites()

    def age_change(self):
        self.age+=Human.age_inc
        
    def favourites():
        print(" fav things sweets, icecreams..")
        
    
       
    def own_fav(self,favourites_values):
        
        self.own_fav_values=favourites_values
        print(" fav things sweets & ",self.own_fav_values)
        Human.favourites()
        
    def port_folio(self):
        print("portfoli is , name = ",self.name,", gender= ",self.gender,", age= ",self.age)
        print("His/Her fav things sweets & ",self.own_fav_values)
     
  
    def iq_change(self,iq_value):
        self.iq=iq_value
        
    def education(self,qualification_value):
        self.qualification=qualification_value
    
    def profession(self,profession_value):
        self.profession_value=profession_value
        
    def nationality(self,nation_value):
        self.nationality_value=nation_value

    def weight_increment(self,activity_level):
        
        if activity_level>10 :
            self.weight_increment_value=-2
        elif activity_level<=10 and activity_level>=8:
            
            self.weight_increment=-1
        elif activity_level<8 and activity_level>=6:
            self.weight_increment_value=0
        
        elif activity_level<6 and activity_level >=4 :
            self.weight_increment_value=1
        
        elif activity_level<4 and activity_level >=2:
            self.weight_increment_value=2
     
        elif activity_level<2 and activity_level >0 :
            self.weight_increment_value=3
        else:
            self.weight_increment_value=4
         
     
            
        
    def display_all_details(self):
        self.show_details()
        print("name_argument : ",self.name)
        print("gender_argument : ",self.gender)
        print("age_argument:",self.age)
        print("own_fav_values : ",self.own_fav_values,    "iq :",    self.iq, "qualification :",  self.qualification, "profession_value :",self.profession_value,   "weight_increment_value :",     self.weight_increment_value,    "weight_in_kg :",    self.weight_in_kg,"nationality :",self.nationality_value)

    

"""
1. Favourites
2. iq level
3. hieght increment
4. weight increment
5. behaviour,
6. Nationality
7. Qualification
8. profession
9. display_all details/ portfolio


"""      
     
        
vinayak_obj=Human("Vinayak","M",28)

Sonali_obj=Human("Sonali","F",27)

Sonali_obj.number_eyes
vinayak_obj.number_eyes

new_human=Human()



vinayak_obj.show_details()
Sonali_obj.show_details()
new_human.show_details()



new_human.name="Arvind"
new_human.gender="M"
new_human.age=23

new_human.show_details()

Human.favourites()

Sonali_obj.display_all_details()




favourites_values={"desssrts":["cake","icecream"],"nonveg":"shawrma"}
Sonali_obj.own_fav(favourites_values)

new_human.own_fav(favourites_values)

new_human.show_details()


vinayak_obj.own_fav({"main_course ": "paneer"})

vinayak_obj.show_details()

vinayak_obj.iq_change(140)

vinayak_obj.education("Mtech")
vinayak_obj.profession("Python Devloper")
vinayak_obj.nationality("USA CITIZEN")
vinayak_obj.weight_increment(6)
vinayak_obj.display_all_details()


vinayak_obj.port_folio()



Sonali_obj.iq_change(150)

Sonali_obj.education("Phd")
Sonali_obj.profession("Data scientist")
Sonali_obj.nationality("INDIAN CITIZEN")
Sonali_obj.weight_increment(3)
Sonali_obj.display_all_details()




