a=input('請輸入性別(M/F)')
if a=='M':
    print('男')
if a=='m' or a=='M':
    print('男')    
if a in ['M','m']:
    print('男')
if a in ['m','M']:
    print('男') 
elif a in ['f','F']:
    print('女')   
else:
    print('輸入錯誤')    