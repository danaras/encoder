
# coding: utf-8

# In[1]:

name = "danaaaaraaaaasaaaa"

    #print name[index]
nameList=list(name)
    #print nameList
    #print nameList[0]
times = nameList[:]
for i in range(len(nameList)):
    print "i: " + str(i)
    if i+1<len(nameList):
        print "nameList[i]: "+nameList[i]
        if nameList[i] == nameList[i+1]:
            print "same"
            if nameList[i]!=nameList[i-1]:
                times[i]=2
                print "times[i]: " + str(times[i])
            else:
                times[i]=0
                print "times[i]: " + str(times[i])
            for k in range(2,len(nameList)-i):
                if nameList[i]==nameList[i+k]:
                     if nameList[i]!=nameList[i-1]:
                        times[i]+=1
                        print "we are here"
                else:
                    print "broken"
                    break
                    
        else:
            print "not same as the next one"
            if i>-1:
                if nameList[i]!=nameList[i-1]:
                    print "not same as the previous one"
                    times[i]=1
                    print "times[i]: " + str(times[i])
                else:
                    times[i]=0
                    print "times[i]: " + str(times[i])
    else:
        if nameList[i]!=nameList[i-1]:
            times[i]=1
        else:
            times[i]=0
print times                 
            
  
        


# In[2]:

encodedZip=zip(times,nameList)
print encodedZip
print len(encodedZip)


# In[3]:

encodedTuple=[item for item in encodedZip if item[0] != 0]
print encodedTuple

