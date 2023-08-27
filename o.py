LIKEBTN = "LIKE4LIKE.png"
LOGO = "LOGO.png"
LIKECONTENTBTN = "LIKEONTENTBTN.png"
CONFIRMBTN = "CONFIRMBTN.png"
LOGOTOAREAOFFSET = 270
REPEAT = 0

from random import randint

def searchImage(image):
    reg = None
    sleep(randint(2, 5))
    try:
        wait(Pattern(image).similar(0.8), 2)
    except:
        print("search area not visible, try again")
        return reg
    reg = find(image)
    if reg:
        reg.highlight(2, "green")
    else:
        print("search area not visible, try again")
    return reg

def closeWindow():
    keyDown(Key.ALT)
    keyDown(Key.F4)
    keyUp(Key.ALT)
    keyUp(Key.F4)

def refreshWindow():
    keyDown(Key.CTRL)
    keyDown(Key.R)
    keyUp(Key.CTRL)
    keyUp(Key.R)

REPEAT = int(input("Please enter number of loop, to repeat:", "10"))
for current_i in range(0,REPEAT):
    result = Do.popup("Loop remained:"+str(REPEAT-current_i)+"\nAutoclosed after 3 seconds, Click OK to stop!", 3)
    if result:
      exit(1)
    else:
      pass
    
    #OPEN CONTENT
    found_likebtn = searchImage(LIKEBTN)
    if found_likebtn:
        click(found_likebtn)
    else:
        result = Do.popup("Like4Like like button not found, refresh page in 3second", 3)
        refreshWindow()
    found_tiktokwindow = searchImage(LOGO)
    
    #LIKE
    if found_tiktokwindow:
        tiktok_vdo_area = found_tiktokwindow.offset(Location(LOGOTOAREAOFFSET, LOGOTOAREAOFFSET))
        tiktok_vdo_area.highlight(2, "red")
        doubleClick(tiktok_vdo_area)
        sleep(randint(2, 5))
        closeWindow()
    
    #CONFIRM
    found_confirmbtn = searchImage(CONFIRMBTN)
    if found_confirmbtn:
        click(found_confirmbtn)

    #INCREASE I
    current_i = current_i + 1

