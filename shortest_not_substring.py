
def list_joiner(input_list):
    saperator = ""
    Final_string_input = saperator.join(input_list)
    return Final_string_input


def shortest_subsequence_not_present(Final_string):  
    
    
	shortest_Final_stringing = ""
	N = len(Final_string)
	sub_segments = set()

	for i in range(N):
		sub_segments.add(Final_string[i])
		if (len(sub_segments) == 26) :
			shortest_Final_stringing += Final_string[i]
			sub_segments.clear()
		
	for ch in range(int(26)):
		if (chr(ch + 97) not in sub_segments) :			
			shortest_Final_stringing += chr(ch + 97)			
			return shortest_Final_stringing
	
	return shortest_Final_stringing




    
input_list=["abd","eg","bcd"] 

Final_string_input=list_joiner(input_list)

print(shortest_subsequence_not_present(Final_string_input))
