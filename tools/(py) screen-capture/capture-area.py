import mss.tools
#import gtk, pygtk
from time import time


#def getScreenSize():
#    window = gtk.Window()
#    screen = window.get_screen()
#    print("width = " + str(screen.get_width()) + ", height = " + str(screen.get_height()))
#    return [str(screen.get_width()), str(screen.get_height())]


def getName():
    return str(time()).split('.')[0] + '.png'


if __name__ == "__main__":
    #getScreenSize()
    choice = input("Start? [Y,y] ")
    while choice in ["y", "Y"]:
        with mss.mss() as sct:
            # The screen part to capture
            # Get information of monitor 2
            monitor_number = 1 #can be 2 in case of a second monitor
            mon = sct.monitors[monitor_number]

            # The screen part to capture
            monitor = {
                "top": mon["top"] + 210,  # 100px from the top
                "left": mon["left"] + 930,  # 100px from the left
                "width": 915,
                "height": 760,
                "mon": monitor_number,
            }
            #output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)
            output = getName().format(**monitor)

            # Grab the data
            sct_img = sct.grab(monitor)

            # Save to the picture file
            mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
            print(output)
        choice = input("Continue? [Y,y] ")
    print("End of capture")
    
    

    
