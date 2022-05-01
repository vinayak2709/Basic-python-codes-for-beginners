def list_joiner(input_list):
    saperator = ""
    Final_string_input = saperator.join(input_list)
    return Final_string_input


def alphabet_check(alphabets,check_list):
    
    for i in alphabets:
        if i not in check_list:
            print(i)
            return i
        
    return "all_alphabets_present"


def double_alphabet_check(alphabets,check_list):
    for j in alphabets:
        for i in alphabets:
            if j+i not in check_list:
                return j+i
            
    return "all_double_alphabets_present"
     

def tripple_alphabet_check(alphabets,check_list):
    for k in alphabets:    
        for j in alphabets:
            for i in alphabets:
                if k+j+i not in check_list:
                    return k+j+i
                
    return "all_tripple_alphabets_present"
     

def combo4_alphabet_check(alphabets,check_list):
    for h in alphabets:    
        for k in alphabets:    
            for j in alphabets:
                for i in alphabets:
                    if h+k+j+i not in check_list:
                        return h+k+j+i
                
    return "all_combo4_alphabets_present"
     




def smallestString(N,S):    
    alphabets=""    
    for ch in range(int(26)):
        alphabets += chr(ch + 97)	   
    
    input_list=S        
    check_list=list_joiner(input_list)
    result1=alphabet_check(alphabets,check_list)    
    if result1!="all_alphabets_present":
        pass
    else:   
        result1=double_alphabet_check(alphabets,check_list)        
        if result1!="all_double_alphabets_present":
            pass
        else:
            result1=tripple_alphabet_check(alphabets,check_list)
            if result1!="all_tripple_alphabets_present":
                pass
            else:
                result1=combo4_alphabet_check(alphabets,check_list)
                if result1!="all_combo4_alphabets_present":
                    pass
                else:
                    print("more combinations required")
    
    return result1
    


# S=["abd","eg","bcd"] 
# N=len(S)
# smallestString(N,S)