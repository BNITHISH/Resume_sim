from __future__ import division
def sim(filepath1,filepath2):

  l=[] # this is list l for storing keywords from keywords.txt
  f=open('keywords.txt','r')
  for line in f:
    l.append(line.strip())
#uncomment the following line to see all the keywords loaded into list l
  #print l


# the following lines are for loading the resume1 into variable g
  g=open(filepath1,'r')
  g=g.read()
  g=g.split()
  g=' '.join(g)# this split and join aperations are done in order to make the words separeated with single space because the keywords are separated with only one space
  #keywords fail to match if above split and join are not considered

#uncomment the following line to see if resume1 is loaded into variable g or not

 #similarly for reading second resume into variable h
  h=open(filepath2,'r')
  h=h.read()
  h=h.split()
  h=' '.join(h)


#uncomment the following line to see if resume2 is loaded into variable h or not
  #print h


  ls=[] #ls is main_list for storing the sublists of [1,0] combination lists as described in abstract
  for i in l:
    if i in g and i in h:
      dum=[1,1] #dum is dummy list for appending sublistes of [1,0]'s into main_list,[1,1] is keyword is present in both resumes
      ls.append(dum)
    elif i in g and i not in h:
      dum=[1,0]  #[1,0] for keyword present in Resume1 but not in Resume2
      ls.append(dum)
    elif i not in g and i in h:
      dum=[0,1]  #[0,1] for keyword present in Resume2 but not in Resume1
      ls.append(dum)
    else:
      dum=[0,0]  #[0,0] for keyword not present in both resumes
      ls.append(dum)

#uncomment the following line to see the main_list ls
  #print ls




  cl=[]  #cl is count_vector as described in abstract for storing the number of times the keyword repeats in resumes
  for i in l:
    dum=[g.count(i),h.count(i)]
    dum=min(dum)
    cl.append(dum)

#uncomment the following line to see the count_vector
  #print cl
  #print len(ls)
  #print len(cl)


  c_num=0  # c_num is for storing the number of instances where keyword repeats in both resumes

  c=0      # c is for stroring the number of instances where keyword either occurs in any one of the resumes

#below for loop is for calculating c_num by looping through the entire main_list

  for i in xrange(len(ls)):
    if ls[i]==[1,1]:
      c_num=c_num+cl[i]

#uncomment the following line to check the value of c_num
  #print c_num

#below for loop is for calculating the c value

  for i in xrange(len(ls)):
    if ls[i]==[1,0] or ls[i]==[0,1]:
      c=c+1

#uncomment the following line to check the value of c
  #print c

# output is stored into ans variable
  ans=c_num/(c_num+c)

  print ("%.2f"%(ans)) #for printing the value of output upto two decimals
