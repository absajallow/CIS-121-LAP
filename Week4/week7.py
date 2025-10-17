week7
#question 4

def get_name(my_dict):
    names =[]
    #how ti iterate through the dictionary
    #how to get name ?
    for key in my_dict:
        #how do we access the value with the key ?
        print("keys:" +key)
        #how do you put the names in a lis ?

        return names
     names_dict = {"1,2,3,5": "matt","6,7,8,9":"even linder","789":"absa"}   
     print(get_name(names_dict))


     #question 5
     def find_oldest (persons):
        oldest_name = ""
        max_age = -1
        for name in persons:
            age = person[name]
            if age > max_age:
                max_age = age
                oldest_name = name
         return oldest_name
       pesrsons = {"absa":71,"Ous":45}  
       print(find_oldest{person})

