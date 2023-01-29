import mss.tools
from time import time
from time import sleep

def getName():
    return str(time()).split('.')[0] + '.png'

def shot(sct):
    # The screen part to capture
    # Get information of monitor 2
    monitor_number = 1 #can be 2 in case of a second monitor
    mon = sct.monitors[monitor_number]

    # The screen part to capture
    monitor = {
        "top": mon["top"] + 210,  # 100px from the top
        "left": mon["left"] + 930,  # 100px from the left
        "width": 915,
        "height": 755,
        "mon": monitor_number,
    }
    #output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)
    output = getName().format(**monitor)

    # Grab the data
    sct_img = sct.grab(monitor)

    # Save to the picture file
    mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
    print(output)

    
def manualShots():
    choice = input("Start? [Return to continue, any key to stop] ")
    while choice == "":
        with mss.mss() as sct:
            shot(sct)
        choice = input("Continue? [Return to continue, any key to stop] ")
    print("End of capture")

    
def automaticShots():
    period = input("Provide the time interval in seconds: ")
    periodf = float(period)
    print("Type CTRL+C to end the program")
    input("Ready? [Type any key]")
    try:
        while True:
            with mss.mss() as sct:
                shot(sct)
            sleep(periodf)
    except KeyboardInterrupt:
        print("\nEnd of capture")

if __name__ == "__main__":
    mode = 0
    while mode not in ["1", "2"]:
        mode = input("Do you want manual shots [1] or time-based automatic shots [2]? ")
    if mode == "1":
        manualShots()
    else:
        automaticShots()
    
    
    

    
