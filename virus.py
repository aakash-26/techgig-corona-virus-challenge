''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():

 # Write code here 

    w = input()
    #print(w)
    res = []
    temp = None
    flag = True
    n= int(input())
    #print("n",n)
    p = []
    for i in range(n):
        p.append(input())

    #print("p",p)

    for paitent in p:
        flag = True
        #print("paitent",paitent)
        v = w
        cnt = 0
        for l in paitent:
            cnt += 1
            if flag:
                
                ind = None
                if l in v:
                    
                    ind = v.index(l)
                    
                    if ind:
                        v = v[ind - 1:]
                        
                else:
                    res.append("NEGATIVE")
                    flag = False
                    #print("res",res)

                    
                if cnt == len(paitent) and flag:
                    #print("res",res)
                    res.append("POSITIVE")
            

    for j in res:
        print(j)



main()


