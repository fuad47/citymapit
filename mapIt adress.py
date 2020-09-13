import webbrowser  #pyperclip clipboard yaddasini getirmek ucundu pip install pyperclip et evvelce.
#webbrowser.open('http://inventwithpython.com/')         #browserle linki acir.

#// google mapsda şəhəri xeritede gosterir. http://automatetheboringstuff.com
#While True:

adres=input("Xəritədə baxmaq istədiyiniz şəhərin beynəlxalq adını yazın:  ")
webbrowser.open('https://www.google.com/maps/place/'+adres)
input('Proqramı bağlamaq üçün "Enter" düyməsinə basın')
