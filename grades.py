import compute
def grades1():
    f=open('class.txt','r')
    lis1=[]
    lis2=[]
    lis3=[]
    lis4=[]
    lis5=[]
    lis6=[]
    lis7=[]
    lis8=[]
    lis9=[]
    lis16=[]
    
    a1total=[]
    a2total=[]
    projecttotal=[]
    test1total=[]
    test2total=[]
    dic={}
    dic2={}
    dic3={}
    dic4={}
    dic5={}
    dic6={}
    dicm={}
    ava1=[]
    lis33=[]
    lis34=[]
    lis35=[]
    lis36=[]
    lis37=[]
    
    

    for line in f:
        lis1=line.strip('\n')
        lis2.append(lis1)
    lis2.sort()
    

    for x in range(0,len(lis2)):
        lis3=lis2[x]
        lis4=lis3.split('|')
        
        dic[lis4[0]]=[lis4[1],lis4[2]]
    
    f.close()
    f=open('a1.txt','r')
    for line in f:
       lis1=line.strip('\n')
       lis5.append(lis1)
    
    
    

    for x in range(0,len(lis5)):
        if x==0:
            
            
            a1total.append(lis5[x])
        else:
            lis33.append(lis5[x])
    lis33.sort()

    for x in range(0,len(lis33)):


        lis4=lis33[x].split('|')
        dic2[lis4[0]]=int(lis4[1])
    
    f.close()
    f=open('a2.txt','r')
    for line in f:
       lis1=line.strip('\n')
       lis6.append(lis1)
    
    
    

    for x in range(0,len(lis6)):
        if x==0:
            lis3=lis6[x]
            
            a2total.append(lis3)
        else:
            lis34.append(lis6[x])
        lis34.sort()
    for x in range(0,len(lis34)):

            lis4=lis34[x].split('|')
            dic3[lis4[0]]=int(lis4[1])
    
    f.close()
    f=open('project.txt','r')
    for line in f:
       lis1=line.strip('\n')
       lis7.append(lis1)
    
    
    

    for x in range(0,len(lis7)):
        if x==0:
            lis3=lis7[x]
           
            projecttotal.append(lis3)
        else:
            lis35.append(lis7[x])
        lis35.sort()
    for x in range(0,len(lis35)):
            lis4=lis35[x].split('|')
            dic4[lis4[0]]=int(lis4[1])
    
    f.close()
    f=open('test1.txt','r')
    for line in f:
       lis1=line.strip('\n')
       lis8.append(lis1)
    
    

    for x in range(0,len(lis8)):
        if x==0:
            lis3=lis8[x]
            
            test1total.append(lis3)
        else:
            lis36.append(lis8[x])
    for x in range(0,len(lis36)):
            lis4=lis36[x].split('|')
            dic5[lis4[0]]=int(lis4[1])
    
    f.close()
    f=open('test2.txt','r')
    for line in f:
       lis1=line.strip('\n')
       lis9.append(lis1)
    
    
    

    for x in range(0,len(lis9)):
        if x==0:
            lis3=lis9[x]
            
            test2total.append(lis3)
        else:
            lis37.append(lis9[x])
    for x in range(0,len(lis37)):
            lis4=lis37[x].split('|')
            dic6[lis4[0]]=int(lis4[1])
    
    for x in range(0,len(lis2)):
        lis3=lis2[x]
        lis4=lis3.split('|')
        dicm[lis4[0]]=[dic.get(lis4[0],' '),dic2.get(lis4[0],' '),dic3.get(lis4[0],' '),dic4.get(lis4[0],' '),dic5.get(lis4[0],' '),dic6.get(lis4[0],' ')]
    print("1>Display individual component\n")
    print("2>Display component average\n")
    print("3>Display Standard Report\n")
    print("4>Sort by alternate column\n")
    print("5>Change Pass/Fail point\n")
    print("6>Exit\n")
    lis10=[]
    lis11=[]
    lis12=[]
    lis13=[]
    lis14=[]
    lis15=[]
    lis17=[]
    lis18=[]
    lis19=[]
    lis20=[]
    iny=int(input("Choose 1,2,3,4,5,6:"))
    if iny==1:
        ch=input("Enter module A1,A2,PR,T1,T2:")
        if ch=='a1' or ch=='A1':
            
            compute.option1(lis33,dicm,dic2,"A1",a1total)
        
        elif ch=='a2' or ch=='A2':
            
            compute.option1(lis34,dicm,dic3,"A2",a2total)    
        elif ch=='pr' or ch=='PR' or ch=='Pr' or ch=='pR':
            
            compute.option1(lis35,dicm,dic4,"PR",projecttotal)
                
        elif ch=='T1' or ch=='t1':
            
            compute.option1(lis36,dicm,dic5,"T1",test1total)
        elif ch=='T2' or ch=='t2':
            
            compute.option1(lis37,dicm,dic6,"T2",test2total)
        else:
            print("Wrong option try again")
        grades1()
    elif iny==2:
        choi=input("Enter the module A1,A2,PR,T1,T2:")
        if choi=='a1' or choi=='A1':
            compute.option2(dicm,a1total,dic2,'A1')
        elif choi=='a2' or choi=='A2':
            compute.option2(dicm,a2total,dic3,'A2')
        elif choi=='PR' or choi=='pr' or choi=='Pr' or choi=='pR':
            compute.option2(dicm,projecttotal,dic4,'PR')
        elif choi=='t1' or choi=='T1':
            compute.option2(dicm,test1total,dic5,'T1')
        elif choi=='T2' or choi=='t2':
            compute.option2(dicm,test2total,dic6,'T2')
            
        else:
            print("choose correct option")
                
        grades1()
    elif iny==3:
        
        compute.option3(lis2,dicm,a1total,a2total,projecttotal,test1total,test2total)
                
            
        
        grades1()
    elif iny==4:
        driv=input("Sort by LT(Last name) or GR(Numeric grade),Enter LT or GR: ")
        if driv=='LT' or driv=='lt' or driv=='Lt' or driv=='lT':
            compute.option4(lis2,dicm,a1total,a2total,projecttotal,test1total,test2total,1)
        elif driv=='GR' or driv=='gr' or driv=='Gr' or driv=='gR':
            compute.option4(lis2,dicm,a1total,a2total,projecttotal,test1total,test2total,8)
        else:
            print("Wrong choice,please choose correct option")
            
        grades1()
    elif iny==5:
        ss=int(input("Enter new P/F Point:"))
        compute.option5(lis2,dicm,a1total,a2total,projecttotal,test1total,test2total,ss)
        grades1()
    elif iny==6:
        print("Good Bye")
        return 0
    else:
        print("Choose correct option:")
        grades1()
    
    
    
grades1()
    

    
     
        
    
