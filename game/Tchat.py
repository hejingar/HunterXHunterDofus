import time


class Tchat():

    def __init__(self, bot):
        self.bot = bot
        self.window_manager = bot.window_manager
        self.image_manager = bot.image_manager
        self.targets = self.image_manager.targets

    def send_in_chat(self, text):
        self.window_manager.click_img(self.targets["chat"], [0,0])
        time.sleep(3)
        print("Writing command : "+text)
        for lettre in text:
            self.window_manager.press(lettre)
            time.sleep(0.05)
        self.window_manager.press_entree()
        
    #use with "d" bcause i have a b** d
    #useless function, changed the logic now we writing mapID to make the hunt not pose jalon in wrong map
    def write_end_autopalote(self, text):
        self.window_manager.click_img(self.targets["chat"], [0,0])
        time.sleep(3)
        print("Writing command : "+text)
        for lettre in text:
            self.window_manager.press(lettre)
            time.sleep(0.05)

    def use_auto_palote(self, x, y):   
        self.send_in_chat("/mapid")
        self.send_in_chat(f"/travel {x} {y}")
        time.sleep(0.2)
        if (self.image_manager.is_in_screen(self.targets["no_mount"], 0.85)):
            print("coucou")
            self.window_manager.click_img(self.targets["mount_menu"], [0,0])
            #self.window_manager.press("d")
            time.sleep(0.5)
            self.window_manager.click_img(self.targets["on_mount"], [0,0])
            time.sleep(0.5)
            self.window_manager.click_img(self.targets["quit_mount_menu"], [0,0])
            time.sleep(0.5)
            self.send_in_chat(f"/travel {x} {y}")
        time.sleep(0.2)
        if(not self.image_manager.wait_for_img(self.targets["ok_popup"], 0.8, 0.01, 4)):
            return 0
        self.window_manager.press_entree()
        #time.sleep(5)
        screenshot = self.window_manager.get_screenshot()     
        nb = 0   
        while nb < 6 and not self.image_manager.is_in_screen(self.targets["is_arrived"], 0.95):
            new_screen = self.window_manager.get_screenshot()
            if(len(self.image_manager.positions(screenshot, new_screen, 0.95)) != 0):
                nb+=1
            else:
                nb=0
                screenshot = new_screen 
            time.sleep(1)