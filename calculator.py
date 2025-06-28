num = input('enter number 1: ')
op = input('input operator: ')
num1 = input('enter number 2: ')

if '.' in num or '.' in num1 and op in ["/","+","-",'*']:
   if op == '+':
    ans= float(num) + float(num1)
    print(ans)
    
   elif '.' in num or '.' and op in ["/","+","-",'*']:
    op == "-"
    ans= float(num) - float(num1)
    print(ans)

   elif '.' in num or '.' and op in ["/","+","-",'*']:
    op == "*"
    ans= float(num) * float(num1)
    print(ans)
    
   elif '.' in num or '.' and op in ["/","+","-",'*']:
    op == "/"
    ans= float(num) / float(num1)
    print(ans)
    
else:   
   if op == "+":
    ans = int(num) + int(num1)
    print(ans)

   elif op == "-":
     ans = int(num) - int(num1)
     print(ans)
   
   elif op == "/":
     ans = int(num) / int(num1)
     print(ans)

   elif op == "*":
     ans = int(num) * int(num1)
     print(ans)

   
