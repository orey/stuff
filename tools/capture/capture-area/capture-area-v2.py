import mss.tools
from time import time
from time import sleep

#================================ Class monitor - Begin
class Monitor:
    top = 210
    left = 930
    width = 915
    height = 755
    screen = 1 # can be 2 in case of other monitor

    def getScreen(self):
        return self.screen

    def changeParams(self,t, l, w, h):
        self.top = t
        self.left = l
        self.width = w
        self.height = h

    def changeParamsString(self,s):
        lis = s.split(' ')
        if len(lis) != 4:
            print("Error in parameters, doing nothing")
            return;
        self.top = int(lis[0])
        self.left = int(lis[1])
        self.width = int(lis[2])
        self.height = int(lis[3])
    
    def printParams(self):
        print("Origin: Number of pixels from the top: " + str(self.top))
        print("Origin: Number of pixels from the left: " + str(self.left))
        print("Frame width: " + str(self.width))
        print("Frame height: " + str(self.height))
        print("Monitor number: " + str(self.screen))

    def getMonitor( self):
        return {
            "top": self.top,  # top px from the top
            "left":self.left,  # left px from the left
            "width": self.width,
            "height": self.height,
            "mon": self.screen
        }
#================================ Class monitor - End

#-------------------------------
# Define the name of the image. As it is in seconds it enables
# to have a good chronology for conversion to pdf
def getName():
    return str(time()).split('.')[0] + '.png'

#-------------------------------
# Main function to shot image
def shot(sct, monitor):
    #output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)
    #output = getName().format(**monitor)
    output = getName()

    mon = sct.monitors[monitor.getScreen()]

    # Grab the data
    sct_img = sct.grab(monitor.getMonitor())

    # Save to the picture file
    mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
    print(output)

    
#-------------------------------
def manualShots(monitor):
    choice = input("Start? [Return to continue, any key to stop] ")
    while choice == "":
        with mss.mss() as sct:
            shot(sct,monitor)
        choice = input("Continue? [Return to continue, any key to stop] ")
    print("End of capture")


#-------------------------------
def setup(monitor):
    print("The default monitor is as follows:")
    monitor.printParams()
    while True:
        answer = input("Provide new params like '120 230 133 156' or type 'q' to quit, or 's' to shot again: ")
        if answer == "q":
            print("The parameters you chose are the following: ")
            monitor.printParams()
            return
        if answer != "s":
            monitor.changeParamsString(answer)
        # shot
        with mss.mss() as sct:
            shot(sct,monitor)
    

#-------------------------------
def automaticShots(monitor):
    period = input("Provide the time interval in seconds: ")
    periodf = float(period)
    print("Type CTRL+C to end the program")
    input("Ready? [Type any key]")
    try:
        while True:
            with mss.mss() as sct:
                shot(sct,monitor)
            sleep(periodf)
    except KeyboardInterrupt:
        print("\nEnd of capture")


#======================================== MAIN
if __name__ == "__main__":
    monitor = Monitor()
    setup(monitor);
    mode = 0
    while mode not in ["1", "2"]:
        mode = input("Do you want to setup the frame [0], to do manual shots [1] or time-based automatic shots [2]? ")
    if mode == "1":
        manualShots(monitor)
    else:
        automaticShots(monitor)
    
    
    

    
