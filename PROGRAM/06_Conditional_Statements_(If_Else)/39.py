# Q39. Internet Data  
#       Data 2 GB ya usse zyada → HD Video dekho.  
#       Data 500 MB–2 GB → Normal Video dekho.  
#       Data 500 MB se kam → Sirf Browsing karo.

permission=input("Sir, please confirm whether you will be using data in MB or GB. = ").lower()
if permission != 'mb' and permission != 'gb':
    print("Invalid !!  Try Again")
    exit()
elif permission == 'gb':
    data =int(input("Enter data in GB = "))
    data=data*1024
elif permission == 'mb':
    data =int(input("Enter data in MB = "))
if data >= 2048:
    print("HD Video Dekho")
elif data >=500:
    print("Normal Video Dekho")
else:
    print("Sirf Browsing Karo")     