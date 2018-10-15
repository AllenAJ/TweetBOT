
#Explanations at the end!!

#The importing suite...

try: 
    import time
    import tweepy
    import sys
    from random import randint
except ImportError:
    print("Import Error!!!\nExiting!!!")
    time.sleep(3)
    #exit()
   

#The secret stuff suite...

    print("Import Error!!!\nExiting!!!")
CONSUMER_KEY = ''
CONSUMER_SECRET = ''               #Just get there keys from twitter
ACCESS_KEY = ''                    #you will get them on creating a bot
ACCESS_SECRET = ''


#The authentication suite...

z = 1
while z :
    try:
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        api = tweepy.API(auth)
        z = 0
    except:
        print("\nAuthentication error!!!\nPlease check your network... \nTrying again!!!")
        z = 1


#The file handling suite...
    
try:
	filename=open('tweets.txt','r')
	f=filename.readlines()    
except IOError as err:
	print("\nFile Error : " , err)
finally:
	filename.close()



#adding the 'Hashtag' suite...

substr = '#TCSITWiz'
newf = []

for line in f:
    if not substr in line:        
        newf.append(line[:-1] + '\n.....\n#TCSITWiz')
    else:
        newf.append(line)     
		
		
		
		
#The tweeting suite...

count = 0
init_thresh = 5
multiplier = 4


for line in newf:      
    t = init_thresh + multiplier*(randint(1,100)/100)  #line 1
    api.update_status(line)
    count = count + 1
    print ('\nPosted tweet #' , count)
    time.sleep(t)

    


#line 1 is the timer i told you about 
#the init_thresh represnts the min time before a tweet is posted (i.e the api method is called again)  
#i used 'randint(1,100)/100' to randomize the tweeting so as not to make it appear automated
#it gives a decimal between 0 and 1 
#the multiplier is used to vary the random values
#so the statement gives a time values between 5 and 5+4 when called














