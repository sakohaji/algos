#Sako Haji  
#Dynamic Programming  
#Paper1 version2  
#04/01/2019  
	  
#brute-force  
from datetime import datetime #initializes the function to test for runtime  
start = datetime.now()  
end = datetime.now()  
	  
def fibanocci(j):  
	start = datetime.now()  
		a = 0  
	    b = 1  
	    if (j) <= 1:  
	        if j < 0:  
	            return None  
	        if j == 0:  
	            return a  
	        if  j == 1:   
	            return b  
	    else:  
	        return  fibanocci(j-1) + fibanocci(j-2)  
	    end = datetime.now()  
	  
	print (end- start) #gave run time from start to end  
	  
	###test cases  
	##print (fibanocci(1))  
	##print (fibanocci(3))  
	##print (fibanocci(90))  
	  
	#Memoization(top-down)  
	from datetime import datetime  
	start = datetime.now()  
	end = datetime.now()  
	  
	cache = {0:1,  
	         1:1,  
	         2:1}  
	  
	def fibanocci(j):  
	   start = datetime.now()  
	    if j in cache:  
	        return cache[j]  
	    a = 0  
	    b = 1  
	    if (j) <= 1:  
	        if j < 0:  
	            return None  
	        if j == 0:  
	            cache[0] = a  
	            return (cache[0])  
	        if  j == 1:  
	            cache[1] = b  
	            return (cache[1])  
	    else:  
	        cache[j] = fibanocci(j-1) + fibanocci(j-2)  
	        return (cache[j])  
	    end = datetime.now()  
	  
	print (end- start)   
	print (cache) #Prints the cache of saved solutions  
	  
	#Tabulaion(bottom-up)  
	  
	from datetime import datetime  
	start = datetime.now()  
	end = datetime.now()  
	  
	def fibanocci(j):  
	    start = datetime.now()  
	    if j in cache:  
	        return (cache[j])  
	    for i in range(2, j+1):  
	        cache[j] = fibanocci(j-1) + fibanocci(j-2)  
	        return (cache[j])  
	    end = datetime.now()  
	  
	print(end-start)  
	print (cache)  


