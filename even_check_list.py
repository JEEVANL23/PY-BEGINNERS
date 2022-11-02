


def even_list(num_list):
    
    even_num = []
    for num in num_list:
        if num%2 == 0:
            even_num.append(num)
            print("even number","at index ",num_list.index(num),"and the number is ",num)
        else:
            pass
    print(even_num)
    
even_list([5,6,1,2,4,3])   
     