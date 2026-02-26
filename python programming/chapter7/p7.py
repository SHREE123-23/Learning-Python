#
def countvc(userinput):
    vowels="aeiouAEIOU"
    countv=0
    countc=0
    for eachchar in userinput:
       if(eachchar.isalpha()):
         if(eachchar in vowels):
            countv=countv+1

    else:
        countc=countc+1

        return countv,countc
    

    v,c=countvc("shree")

    print(f"{v} are vowles and {c} are consonants",v,c)