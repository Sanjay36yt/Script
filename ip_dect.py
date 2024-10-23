# ip_dect the code used to find the number of ip up in the network

import sys
import os

#The main consist of three process 
#1.getting the command line argument
#2.If the command line argument is not given give the instruction 
#3.If the argument is given move to next function 

def main():

 try:
  if len(sys.argv) > 1  :

    global first_Value # This gloable variable used in ip_loop function to process the ip address
    first_Value = str(sys.argv[1]) # Save the command line argument in a varable
    ip_sep(first_Value)
    
  else:
    
       print("""
ERROR :
             -----> Enter the input :<-------------
Eg: (192.168.1.x-y) --> (x="starting host",y="End host ")
             
ENTER THE IP RANGE YOU NEED TO FIND
             REPLACE THE IP WITH YOUR IP  

RUN THE CODE : python ip_sweap.py 192.168.1.1-155 
		        """)
 except:
      print(""" 
RUN THE CODE : python ip_sweap.py 192.168.1.1-155 
		        """)
     

def ip_sep(ip_add): # Used to seperate the ip address for precessing
        ip = ip_add.split(".") # using split function to seperate the input ip into array
        last_oct = ip[3].split("-") # seperate the last octect for the loop (1-255)
        ip_loop(last_oct[0],last_oct[1]) # functon passing

def ip_loop(start_oct,last_oct): # make the ping precess
     grep = "| grep "'"64 bytes"' # declaration of grep command in string
     cut_ip = "| cut -d "'" "' " -f 4" # decleration of cut commant in string
     tr = "| tr -d "'":"' # decleration of tr command in string

     ip = first_Value.split(".")# get the ip address in string formate and convert in to array and save it
 

#loop statement , the for loop run but the function argument
#start_oct as the starting value
#last_oct as the end value +1 to make the full iteration

     for i in range(int(start_oct),int(last_oct)+1):
          ip[3] = i #replace the 3rd index value into "i" , still it is array
          ip_add = ip # make a copy of the array
          strin = '.'.join(str(x) for x in ip_add) #convert back into string to run in "cli"
          out = os.system(f"ping {strin} -c 1 {grep} {cut_ip} {tr}") # cli command for ping
          print(out) 
             
    

main() # The Starting point


