import random,string,time

def create():
    file1=input('Enter file to be stored\n')
    f=open('%s'%(file1),'a')
    print('enter the website and username\n')
    web_site=input()
    user_name=input()
        
    s=int(input('enter the length of password\n'))
    if (s<4 or s==4):
        print('password too weak,choose greater length')
        print('Suggestion: The Lenghty the password the safer the account *[7-12 chars]')
        print('Try Again!!!')
        print('\n')

    else:
        print('Password creating...')  
        time.sleep(3)  
        r=random.choices(string.ascii_letters+string.ascii_lowercase
        +string.ascii_uppercase,k=s-4)
        l=random.choices(string.digits,k=2)
        m=random.choices(string.punctuation,k=2)
        s=''.join(r)+''.join(l)+''.join(m)
        print('Password combination found.')
        time.sleep(1)
        print('The generated password is: ',s)
        print('\n')
        d=web_site+"|"+user_name+"|"+s
        result=d.split("|")
        f.write('%s\n'%(result))
        f.close()


def search():
    file1=input('Enter file to be searched\n')
    f=open('%s'%(file1),'a')
    with open('%s'%(file1),'r') as f:
        acc=input('User_id to be searched:\t')
        web=input('Website to be searched:\t')
        print('%s account being searched'%(acc))
        
        time.sleep(3)
        for i in f:
            if acc in i and web in i:
                time.sleep(1)
                print('Account found')
                print(i+"\n")
                return 
        print('Account not found\n') 


def delete():
    file1=input('Enter file to be deleted\n') 
    f=open('%s'%(file1),'a')
    acc=input('Account name to delete: ')
    web=input('Website name to delete: ')
    with open(file1) as f:
        reads=f.readlines()
        for i in reads:
            lines=i.split(",")
            if acc in lines[1] and web in lines[0]:
                reads.remove(i)
                time.sleep(1)
                print("Deleted successfully...\n")
                break
        else:
            time.sleep(1)
            print("Account not found!\n")
        with open(file1,'w') as f1:
            for i in reads:
                f1.write(i)   
                 
while(True):
    time.sleep(2)
    print('\nSelect a choice\n')
    print('-> Create new account :press N \n')
    print('-> Search existing account:Press S \n')
    print('-> Delete existing account :Press D \n')
    print('-> Quit :Press Q\n')

    q=input()
    
    if q=='N' or q=='n':
        create()
    elif q =='S' or q=="s":
        search()
    elif q =='D' or q=="d":                                   
        delete()
    elif q =='Q' or q=="q":
        break    
    else:
        print('please select from given choice\n')