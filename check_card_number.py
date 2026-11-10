def check_card_number():
    while True:
        x = input('Type a 16 digit card number (XXXX-XXXX-XXXX-XXXX): ')
        d1 = False 
        d2 = False
        d3 = False
        d4 = False
        if len(x) == 19:
            d1 = True
            i =0
            for ch in x:
                if not ch.isdigit():
                    i +=1
            if x[4] == '-' and x[9] == '-' and x[14] == '-' and i == 3:
                d2 = True
            
            if int(x[0])>= 4 and int(x[0])<= 7:
                d3 = True
        if d1 and d2 and d3:
            i = 1
            sum = 0
            for ch in x:
                if ch.isdigit():
                    if i % 2 == 1:
                        d = int(ch)*2
                        if d > 9:
                            d -= 9 
                        sum += d
                    else:
                        sum += int(ch)
                    i = i +1
                    
               
                
            if sum % 10 == 0:
                d4 = True
            if d4:
                print('Valid number')
                break
            else:
                print('Invalid number')
        else:
            print('Wrong format')
check_card_number()