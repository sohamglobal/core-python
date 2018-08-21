# Search algorithms by sharayu

class SearchAlgos:

    def binarySearch(self,lst):
        first=0
        last=len(lst)-1
        middle=(first+last)//2

        n=int(input("Enter a number to search in list : "))

        while(first<=last):

            if(lst[middle]==n):
                print(n," is present at ",middle)
                break
            elif lst[middle]<n:
                first=middle+1
            else:
                last=middle-1
            
            middle=(first+last)//2

        if(first>last):
            print(n," is not present in list")



    def linearSearch(self,lst):
        
        n=int(input("Enter a number to search in list : "))
        flag=False
        for i in range(len(lst)):
            if lst[i]==n:
                print(n," is present at ",i," index")
                flag=True
            
        if flag==False:
            print(n," is not present in list")
            

# Content of sohamglobal.com