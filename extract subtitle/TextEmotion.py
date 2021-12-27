with open('hobbsandshaw.srt') as file:
    subtitle = file.readlines()
    sub_list = [subtitle[i : i+4] for i in range(0, len(subtitle), 4)]
    
    this_dict = {}
    subtitle=[]
    
    for item in sub_list:
        number = item[0].strip('\n')
        this_dict[number] = item[2].strip('\n')
        
        
    #print(this_dict)
for x in this_dict:
  #print(this_dict[x])
  subtitle.append(this_dict[x])
print(subtitle)