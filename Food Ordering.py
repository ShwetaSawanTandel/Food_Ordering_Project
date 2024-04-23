idly=10
dosa=20
sambar=20
vada=15
appam=20
puri=30
pongal=20
bill=0
while True:
    print('1.Idly (Price=10rs per Idly)')
    print('2.Dosa (Price=20rs per Dosa)')
    print('3.Sambar(Price=20rs per Sambar)')
    print('4.Vada (Price=15rs per Vada)')
    print('5.Appam(Price=20rs per Appam)')
    print('6.Puri (Price=30rs per Puri)')
    print('7.Pongal(Price=20rs per Pongal)')
    choice=int(input('Enter your choice:'))
    if choice==1:
        qty=int(input('Idly qty'))
        if qty>0:
            co=int(input('you want to continue.... press 1 or press 0'))
            if co==1:
                print('Thank you')
                nbill=idly*qty+bill
                bill=nbill
            else:
                nbill=idly*qty+bill
                bill=nbill
                print('your total bill is:',nbill)
                break
        else:
            print('Try Again')
    elif choice==2:    
        qty=int(input('Dosa qty'))
        if qty>0:
            #print(nbill)
            co=int(input('you want to continue.... press 1 or press 0'))
            if co==1:
                print('Thank you')
                nbill=dosa*qty+bill
                bill=nbill
            else:
                nbill=dosa*qty+bill
                bill=nbill
                print('your total bill is:',nbill)
                break
        else:
            print('Try Again')
    elif choice==3:    
        qty=int(input('Sambar qty'))
        if qty>0:
            co=int(input('you want to continue.... press 1 or press 0'))
            if co==1:
                print('Thank you')
                nbill=sambar*qty+bill
                bill=nbill
            else:
                nbill=sambar*qty+bill
                bill=nbill
                print('your total bill is:',nbill)
                break
        else:
            print('Try Again')
    elif choice==4:    
        qty=int(input('vada qty'))
        if qty>0:
            co=int(input('you want to continue.... press 1 or press 0'))
            if co==1:
                print('Thank you')
                nbill=vada*qty+bill
                bill=nbill
            else:
                nbill=vada*qty+bill
                bill=nbill
                print('your total bill is:',nbill)
                break
        else:
            print('Try Again')
    elif choice==5:    
        qty=int(input('appam qty'))
        if qty>0:
            co=int(input('you want to continue.... press 1 or press 0'))
            if co==1:
                print('Thank you')
                nbill=appam*qty+bill
                bill=nbill
            else:
                nbill=appam*qty+bill
                bill=nbill
                print('your total bill is:',nbill)
                break
        else:
            print('Try Again')        
            
    elif choice==6:    
        qty=int(input('Puri qty'))
        if qty>0:
            co=int(input('you want to continue.... press 1 or press 0'))
            if co==1:
                print('Thank you')
                nbill=puri*qty+bill
                bill=nbill
            else:
                nbill=puri*qty+bill
                bill=nbill
                print('your total bill is:',nill)
                break
        else:
            print('Try Again')    
        
    elif choice==7:    
        qty=int(input('Pongal qty'))
        if qty>0:
            co=int(input('you want to continue.... press 1 or press 0'))
            if co==1:
                print('Thank you')
                nbill=pongal*qty+bill
                bill=nbill
            else:
                nbill=(pongal*qty)+bill
                bill=nbill
                print('your total bill is:',nbill)
                break
        else:
            print('Try Again')    
        
    else:
        print('Wrong choice')
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        


