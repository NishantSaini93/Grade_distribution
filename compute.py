import operator
import math
def option1(lisx,dicx,dicx1,tx,aa):
    at=aa
    print(tx+" grades (",aa[0], ")")
    lis1=[]
    lis2=[]
    lis3=[]
    lis4=[]
    lis5=[]
    lis6=[]
    lis7=[]
    lis8=[]
    lis9=[]
    lis10=[]
    lis11=[]
    lis12=[]
    lis13=[]
    lis14=[]
    lis15=[]
    dicm=dicx
    lis2=lisx
    dic2=dicx1
    for x in range(0,len(lis2)):
        lis3=lis2[x]
        lis4=lis3.split('|')
        lis10=dicm.get(lis4[0])
        lis11=lis10[0]
        lis12=lis11[0]
        lis13=lis11[1]
        lis14=dic2.get(lis4[0])
        lis15=lis14
        print((lis4[0]),"%-13s"%(lis12+","+lis13),"   ",lis15)

def option2(dicx,a1t,dx2,tx):
    dicm=dicx
    aa=a1t

    dic2=dx2
    ava1=[]
    ava1=sum(dic2.values())/len(dic2)
    print(tx+" average:"+str(float("{0:.2f}".format(ava1)))+"/"+aa[0])

def option3(lisx,dicx,a1t,a2t,prt,t1t,t2t):
    print("ID     "+"LN     "+"FN    "+"A1   "+ "A2   "+"PR   "+"T1   "+"T2   "+"GR   "+"FL")
    a1total=[]
    a2total=[]
    projecttotal=[]
    test1total=[]
    test2total=[]
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
    lis2=lisx
    dicm=dicx
    a1total=a1t
    a2total=a2t
    projecttotal=prt
    test1total=t1t
    test2total=t2t
    
    
    for x in range(0,len(lis2)):
            lis3=lis2[x]
            lis4=lis3.split('|')
            lis5=dicm.get(lis4[0])
            lis6=lis5[0]
            lis7.clear()
            lis8.clear()
            lis12.clear()
            lis13.clear()
            lis14.clear()
            lis15.clear()
            lis16.clear()
            lis17.clear()
            lis18.clear()
            lis19.clear()
            lis20.clear()
            lis7.append(lis6[0])
            lis8.append(lis6[1])
            if len(lis6[0])==6:
                lis9=lis6[0]
                if len(lis6[1])==6:
                    lis10=lis6[1]
                else:
                    for x in range(len(lis6[1]),6):
                        lis8.append(" ")
                        lis11=''.join(map(str, lis8))
                    lis10=lis11
                        
            else:
                for x in range(len(lis6[0]),6):
                    lis7.append(" ")
                    lis11=''.join(map(str, lis7))
                lis9=lis11
                if len(lis6[1])==6:
                    lis10=lis6[1]
                else:
                    for x in range(len(lis6[1]),6):
                        lis8.append(" ")
                        lis11=''.join(map(str, lis8))
                    lis10=lis11
            lis12.append(lis5[1])
            lis13.append(lis5[2])
            lis14.append(lis5[3])
            lis15.append(lis5[4])
            lis16.append(lis5[5])
            if lis12[0]==' ':
                lis17.append(0)
            else:
                lis17.append(float((lis12[0]/int(a1total[0]))*7.5))
                
            if lis13[0]==' ':
                lis17.append(0)
            else:
                lis17.append(float((lis13[0]/int(a2total[0]))*7.5))
            if lis14[0]==' ':
                lis17.append(0)
            else:
                lis17.append(float((lis14[0]/int(projecttotal[0]))*25))
            if lis15[0]==' ':
                lis17.append(0)
            else:
                lis17.append(float((lis15[0]/int(test1total[0]))*30))
            if lis16[0]==' ':
                lis17.append(0)
            else:
                lis17.append(float((lis16[0]/int(test2total[0]))*30))

            lis18.append(int(sum(lis17)))
            lis20.append(int(lis18[0]))
            if lis18[0]>93:
                lis19.append("A+")
            elif lis18[0]>86:
                lis19.append("A")
            elif lis18[0]>79:
                lis19.append("A-")
            elif lis18[0]>72:
                lis19.append("B+")
            elif lis18[0]>65:
                lis19.append("B")
            elif lis18[0]>58:
                lis19.append("B-")
            elif lis18[0]>50:
                lis19.append("C")
            else:
                lis19.append("F")
                
            print(lis4[0]+" "+lis10+" "+lis9+" "+"%-4s"%str(lis12[0])+" "+"%-4s"%str(lis13[0])+" "+"%-4s"%str(lis14[0])+" "+"%-4s"%str(lis15[0])+" "+"%-4s"%str(lis16[0])+" "+"%-4s"%str(lis20[0])+" "+lis19[0])    


def option4(lisx,dicx,a1t,a2t,prt,t1t,t2t,tupi):
    print("ID     "+"LN     "+"FN    "+"A1   "+ "A2   "+"PR   "+"T1   "+"T2   "+"GR   "+"FL")
    lismain=[]
    lisdis=[]
    a1total=[]
    a2total=[]
    projecttotal=[]
    test1total=[]
    test2total=[]
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
    lis2=lisx
    dicm=dicx
    a1total=a1t
    a2total=a2t
    projecttotal=prt
    test1total=t1t
    test2total=t2t
    dicmm={}
    
    
    for x in range(0,len(lis2)):
            lis3=lis2[x]
            lis4=lis3.split('|')
            lis5=dicm.get(lis4[0])
            lis6=lis5[0]
            lis7.clear()
            lis8.clear()
            lis12.clear()
            lis13.clear()
            lis14.clear()
            lis15.clear()
            lis16.clear()
            lis17.clear()
            lis18.clear()
            lis19.clear()
            lis20.clear()
            lis7.append(lis6[0])
            lis8.append(lis6[1])
            if len(lis6[0])==6:
                lis9=lis6[0]
                if len(lis6[1])==6:
                    lis10=lis6[1]
                else:
                    for x in range(len(lis6[1]),6):
                        lis8.append(" ")
                        lis11=''.join(map(str, lis8))
                    lis10=lis11
                        
            else:
                for x in range(len(lis6[0]),6):
                    lis7.append(" ")
                    lis11=''.join(map(str, lis7))
                lis9=lis11
                if len(lis6[1])==6:
                    lis10=lis6[1]
                else:
                    for x in range(len(lis6[1]),6):
                        lis8.append(" ")
                        lis11=''.join(map(str, lis8))
                    lis10=lis11
            lis12.append(lis5[1])
            lis13.append(lis5[2])
            lis14.append(lis5[3])
            lis15.append(lis5[4])
            lis16.append(lis5[5])
            if lis12[0]==' ':
                lis17.append(0)
            else:
                lis17.append(float((lis12[0]/int(a1total[0]))*7.5))
                
            if lis13[0]==' ':
                lis17.append(0)
            else:
                lis17.append(float((lis13[0]/int(a2total[0]))*7.5))
            if lis14[0]==' ':
                lis17.append(0)
            else:
                lis17.append(float((lis14[0]/int(projecttotal[0]))*25))
            if lis15[0]==' ':
                lis17.append(0)
            else:
                lis17.append(float((lis15[0]/int(test1total[0]))*30))
            if lis16[0]==' ':
                lis17.append(0)
            else:
                lis17.append(float((lis16[0]/int(test2total[0]))*30))

            lis18.append(int(sum(lis17)))
            lis20.append(int(lis18[0]))
            if lis18[0]>93:
                lis19.append("A+")
            elif lis18[0]>86:
                lis19.append("A")
            elif lis18[0]>79:
                lis19.append("A-")
            elif lis18[0]>72:
                lis19.append("B+")
            elif lis18[0]>65:
                lis19.append("B")
            elif lis18[0]>58:
                lis19.append("B-")
            elif lis18[0]>50:
                lis19.append("C")
            else:
                lis19.append("F")
            
            lismain.append([lis4[0],lis10,lis9,lis12[0],lis13[0],lis14[0],lis15[0],lis16[0],lis20[0],lis19[0]])
    if tupi==8:
        lismain.sort(key=lambda tup: tup[tupi])
        lismain.reverse()
        for x in range(0,len(lismain)):
            lisdis=lismain[x]
            print(lisdis[0]+" "+lisdis[1]+" "+lisdis[2]+" "+"%-4s"%lisdis[3]+" "+"%-4s"%lisdis[4]+" "+"%-4s"%lisdis[5]+" "+"%-4s"%lisdis[6]+" "+"%-4s"%lisdis[7]+" "+"%-4s"%lisdis[8]+" "+lisdis[9])    
    

    else:
        sorted_list = sorted(lismain, key=operator.itemgetter(tupi))
        
        for x in range(0,len(sorted_list)):
            lisdis=sorted_list[x]
            
            print(lisdis[0]+" "+lisdis[1]+" "+lisdis[2]+" "+"%-4s"%lisdis[3]+" "+"%-4s"%lisdis[4]+" "+"%-4s"%lisdis[5]+" "+"%-4s"%lisdis[6]+" "+"%-4s"%lisdis[7]+" "+"%-4s"%lisdis[8]+" "+lisdis[9])    
    

    
    
def option5(lisx,dicx,a1t,a2t,prt,t1t,t2t,pf):
    print("ID     "+"LN     "+"FN    "+"A1   "+ "A2   "+"PR   "+"T1   "+"T2   "+"GR   "+"FL")
    lispf=[]
    a1total=[]
    a2total=[]
    projecttotal=[]
    test1total=[]
    test2total=[]
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
    lis2=lisx
    dicm=dicx
    a1total=a1t
    a2total=a2t
    projecttotal=prt
    test1total=t1t
    test2total=t2t
    
    
    for x in range(0,len(lis2)):
            lis3=lis2[x]
            lis4=lis3.split('|')
            lis5=dicm.get(lis4[0])
            lis6=lis5[0]
            lis7.clear()
            lis8.clear()
            lis12.clear()
            lis13.clear()
            lis14.clear()
            lis15.clear()
            lis16.clear()
            lis17.clear()
            lis18.clear()
            lis19.clear()
            lis20.clear()
            lis7.append(lis6[0])
            lis8.append(lis6[1])
            if len(lis6[0])==6:
                lis9=lis6[0]
                if len(lis6[1])==6:
                    lis10=lis6[1]
                else:
                    for x in range(len(lis6[1]),6):
                        lis8.append(" ")
                        lis11=''.join(map(str, lis8))
                    lis10=lis11
                        
            else:
                for x in range(len(lis6[0]),6):
                    lis7.append(" ")
                    lis11=''.join(map(str, lis7))
                lis9=lis11
                if len(lis6[1])==6:
                    lis10=lis6[1]
                else:
                    for x in range(len(lis6[1]),6):
                        lis8.append(" ")
                        lis11=''.join(map(str, lis8))
                    lis10=lis11
            lis12.append(lis5[1])
            lis13.append(lis5[2])
            lis14.append(lis5[3])
            lis15.append(lis5[4])
            lis16.append(lis5[5])
            if lis12[0]==' ':
                lis17.append(0)
            else:
                lis17.append(float((lis12[0]/int(a1total[0]))*7.5))
                
            if lis13[0]==' ':
                lis17.append(0)
            else:
                lis17.append(float((lis13[0]/int(a2total[0]))*7.5))
            if lis14[0]==' ':
                lis17.append(0)
            else:
                lis17.append(float((lis14[0]/int(projecttotal[0]))*25))
            if lis15[0]==' ':
                lis17.append(0)
            else:
                lis17.append(float((lis15[0]/int(test1total[0]))*30))
            if lis16[0]==' ':
                lis17.append(0)
            else:
                lis17.append(float((lis16[0]/int(test2total[0]))*30))

            lis18.append(int(sum(lis17)))
            lis20.append(int(lis18[0]))
            ss1=100-pf
            lispf=ss1/7
           
            
            if lis18[0]>pf+math.ceil(lispf)+(5*math.floor(lispf)):
                lis19.append("A+")
            elif lis18[0]>pf+math.ceil(lispf)+(4*math.floor(lispf)):
                lis19.append("A")
            elif lis18[0]>pf+math.ceil(lispf)+(3*math.floor(lispf)):
                lis19.append("A-")
            elif lis18[0]>pf+math.ceil(lispf)+(2*math.floor(lispf)):
                lis19.append("B+")
            elif lis18[0]>pf+math.ceil(lispf)+math.floor(lispf):
                lis19.append("B")
            elif lis18[0]>pf+math.ceil(lispf):
                lis19.append("B-")
            elif lis18[0]>pf:
                lis19.append("C")
            else:
                lis19.append("F")
                
            print(lis4[0]+" "+lis10+" "+lis9+" "+"%-4s"%str(lis12[0])+" "+"%-4s"%str(lis13[0])+" "+"%-4s"%str(lis14[0])+" "+"%-4s"%str(lis15[0])+" "+"%-4s"%str(lis16[0])+" "+"%-4s"%str(lis20[0])+" "+lis19[0])    
