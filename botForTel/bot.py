import pyautogui

import time
import random
import string


width,height = pyautogui.size()

my_adress = 'ouro1mkxfnjam4ksrgsmgqq2gm62l6xygdjtyus4nqc'

print(pyautogui.position())
def get_akkunt():
    token = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)for x in range(random.randint(10,15)))
    print(token)
    link = 'https://telegram.me/OuroClubBot?start=31cca4b8-8a12-4e38-a8cc-2e9ac03703e7'
    pyautogui.moveTo(114,23,duration =1)
    pyautogui.click()
    pyautogui.moveTo(width/2,height/2,duration = 1)
    pyautogui.scroll(2)
    pyautogui.moveTo(86,50,duration=1)

    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(width/2,height/2,duration=1)
    time.sleep(1)
    pyautogui.scroll(-2)
    pyautogui.moveTo(122,639,duration=1)

    pyautogui.click()
    pyautogui.moveTo(240,634,duration=1)
    pyautogui.click()
    time.sleep(120)
    pyautogui.moveTo(width/2,height/2,duration=1)
    pyautogui.scroll(2)
    pyautogui.moveTo(597,437,duration = 1)

    pyautogui.click()
    pyautogui.moveTo(253,753,duration=1)
    pyautogui.click()
    pyautogui.moveTo(692,496,duration=1)
    pyautogui.click()
    pyautogui.moveTo(576,375,duration=1)
    pyautogui.click()
    pyautogui.hotkey('backspace')
    pyautogui.typewrite('7')
    pyautogui.moveTo(636,378,duration=1)

    pyautogui.click()
    pyautogui.hotkey('ctrl','v')
    pyautogui.moveTo(684,467,duration=1)
    pyautogui.click()
    time.sleep(5)
    pyautogui.moveTo(203,752,duration=1)
    pyautogui.click()
    pyautogui.moveTo(1177,455,duration = 1)
    pyautogui.click()
    time.sleep(100)
    pyautogui.moveTo(1034,455,duration=1)
    pyautogui.doubleClick()
    pyautogui.hotkey('ctrl','c')
    pyautogui.moveTo(253,753,duration=1)
    pyautogui.click()
    pyautogui.moveTo(584,299,duration=1)
    pyautogui.click()
    pyautogui.hotkey('ctrl','v')
    pyautogui.move(572,476,duration=1)
    pyautogui.click()
    time.sleep(5)
    pyautogui.moveTo(557,305,duration=1)
    pyautogui.click()
    pyautogui.typewrite(token)
    pyautogui.moveTo(577,373,duration=1)
    pyautogui.click()
    pyautogui.typewrite(token)
    pyautogui.moveTo(588,460,duration=1)
    pyautogui.click()
    
    time.sleep(15)
    pyautogui.moveTo(29,46,duration=1)
    pyautogui.click()
    pyautogui.moveTo(107,239,duration=1)
    pyautogui.click()


    pyautogui.moveTo(661,326,duration=1)
    pyautogui.click()
    pyautogui.typewrite(token)
    pyautogui.moveTo(823,468,duration=1)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(761,502,duration=1)
    pyautogui.click()
    pyautogui.moveTo(754,644,duration=1)
    pyautogui.click()
    pyautogui.moveTo(703,712,duration=1)
    pyautogui.click()
    pyautogui.typewrite(link)
    pyautogui.hotkey('enter')
    pyautogui.moveTo(582,546,duration=1)
    pyautogui.click()
    time.sleep(15)
    #нажатие на start
    pyautogui.moveTo(739,704,duration=1)
    pyautogui.click()
    time.sleep(15)
    pyautogui.moveTo(565,657,duration=1)
    pyautogui.click()
    time.sleep(15)
    pyautogui.moveTo(565,657,duration=1)
    pyautogui.click()
    time.sleep(15)

    pyautogui.moveTo(565,657,duration=1)
    pyautogui.click()
    time.sleep(15)

    pyautogui.moveTo(565,657,duration=1)
    pyautogui.click()
    time.sleep(15)
    pyautogui.moveTo(565,657,duration=1)
    pyautogui.click()

    time.sleep(15)
    pyautogui.moveTo(637,557,duration=1)
    pyautogui.click()
    time.sleep(10)
    register_on_site()

    pyautogui.moveTo(26,55,duration=1)
    pyautogui.click()
    pyautogui.moveTo(84,368,duration=1)
    pyautogui.click()
    pyautogui.moveTo(808,87,duration=1)
    pyautogui.click()
    pyautogui.moveTo(689,161,duration=1)
    pyautogui.click()
    pyautogui.moveTo(782,410,duration=1)
    pyautogui.click()
    send_monet()






    


def register_on_site():
    token = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)for x in range(random.randint(10,50)))
    token = token+"@mail.ru"
    print(token)
    
    password = 'ganavo72e2'
    pyautogui.moveTo(206,755,duration=1)
    pyautogui.click()
    pyautogui.moveTo(347,18,duration=1)
    
    pyautogui.click()
    pyautogui.moveTo(892,176,duration=1)
    pyautogui.click()
    pyautogui.moveTo(402,694,duration=1)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(312,414,duration=1)
    pyautogui.click()

    pyautogui.typewrite(token)
    pyautogui.moveTo(334,499,duration=0.6)
    pyautogui.click()
    pyautogui.typewrite(password)
    pyautogui.moveTo(380,593,duration=0.5)
    pyautogui.click()
    pyautogui.typewrite(password)
    pyautogui.moveTo(473,685,duration=1)
    pyautogui.click()
    time.sleep(5)
    pyautogui.moveTo(513,684,duration=1)
    pyautogui.click()
    pyautogui.scroll(-3)
    pyautogui.moveTo(590,702,duration=1)
    pyautogui.click()
    pyautogui.moveTo(252,753,duration=1)



    pyautogui.click()
    pyautogui.moveTo(578,507,duration=1)
    pyautogui.click()
    pyautogui.hotkey('ctrl','v')
    pyautogui.hotkey('enter')




def send_monet():
    time.sleep(100)
    pyautogui.moveTo(202,758,duration=1)
    pyautogui.click()
    pyautogui.moveTo(width/2,height/2,duration=1)
    pyautogui.scroll(-3)
    pyautogui.moveTo(316,425,duration=1)
    pyautogui.click()
    time.sleep(3)
    pyautogui.moveTo(420,517,duration=1)
    pyautogui.click()
    pyautogui.typewrite(my_adress)
    pyautogui.moveTo(750,522,duration=1)
    pyautogui.click()
    pyautogui.typewrite('0.99')
    pyautogui.moveTo(406,617,duration=1)
    pyautogui.click()
    pyautogui.scroll(5)
    pyautogui.moveTo(121,18,duration=1)
    pyautogui.click()
    pyautogui.moveTo(1164,463,duration=1)
    pyautogui.click()


for i in range(2):
    get_akkunt()
