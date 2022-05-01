# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 17:27:56 2021

@author: Vinayak
"""


definition_dict={"name":"Vinayak","age":28,"Qualification":"Mtech"}


sample_dictionary={}


sample_dictionary["emp_name"]="Vinayak"
sample_dictionary["emp_id"]="2356"
sample_dictionary["designation"]="Data scientist"
sample_dictionary["salary"]="900"


sample_dictionary["salary"]


sample_dictionary["emp_name"]="Victor"

sample_dictionary.update({"emp_name":"test_user","salary":123023498,"teest":456})


sample_list=[12,3,6,8]
 
del sample_list[1]


del sample_dictionary["teest"]


# to clear dictionry (to reset)
sample_dictionary.clear()


# to delete dictionary
del sample_dictionary


var="test"
del var



sample_dictionary={}


sample_dictionary["emp_name"]="Vinayak"
sample_dictionary["emp_id"]="2356"
sample_dictionary["designation"]="Data scientist"
sample_dictionary["salary"]="900"


len(sample_dictionary)


# string_dict=str(sample_dictionary)

import json
d=json.dumps(sample_dictionary)


new_dict=json.loads(d)


list(sample_dictionary.keys())
list(sample_dictionary.values())







sample_dictionary["emp_nam"]

sample_dictionary.get("emp_name")

sample_dictionary.get("emp_name","my_name")


"""homework"""

factorial = {1 :1, 2:2*1,3:3*2*1,4:4*3*2*1}





sample_value_cubes={1:1,2:8,3:27}







