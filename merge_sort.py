def divide_elements(list_a):
    list_length = len(list_a)
    median = list_length/2
    remainder = list_length % 2
    if remainder == 0:
        divided_list_a = [data for i,data in enumerate(list_a) if i<median]
        divided_list_b = [i for i in list_a  if i not in divided_list_a]
    else :
        divided_list_a = [data for i,data in enumerate(list_a) if i<=median]
        divided_list_b = [i for i in list_a  if i not in divided_list_a]
        median = median+1
    
    return divided_list_a,divided_list_b



def merge_sort(divided_list_a):
    
    x,y = divide_elements(divided_list_a)
    if len(x)!=1 & len(y) != 1:
        new_list.append(y)
        merge_sort(x)    
       
    else:
        sorted_list = compare_list(x,y)
        empty_list.extend(sorted_list)  
           
            
         
    print(final_list)



def compare_list(list_1,list_2):
    new_list = []
    if list_1[0]>list_2[0]:
        new_list.append(list_2[0])
        new_list.append(list_1[0])
    else:
        new_list.append(list_1[0])
        new_list.append(list_2[0])
        
    return new_list






if __name__ == "__main__":
    empty_list = []
    final_list=[]
    new_list = list()
    merge_sort([8,7,6,5])
