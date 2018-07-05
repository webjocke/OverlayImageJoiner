
# OverlayImageJoiner - Combines all images in the watch folder with the overlay image and then puts it in the output folder

# ================== CONFIGURE THERE VARIABLERS TO YOUR LIKINGS ==========================

# WANTED RESOLUTION OF OUTPUT IMAGES
output_width = 800
output_height = 600

# PATHS (All are relative to where the program is running from)
watch_folder = "todo" # All new images in this folder will be converted
output_folder = "done" # The images are placed here after joining with the overlay
overlay_image = "overlay.png" # The image thats gonna be added to all the other images

# ========================================================================================




import os
import time
import re
from PIL import Image

def do_stuff(filename, fileformat):

    # WANTED RESOLUTION
    want_width = output_width
    want_height = output_height

    # Gets the original image
    background = Image.open(watch_folder+"/"+filename+"."+fileformat)
    width, height = background.size

    # Resizes the image
    if want_width/want_height > width/height:
        new_width = want_width
        new_height = new_width * height / width
        background = background.resize((new_width, int(new_height)), Image.ANTIALIAS)
        temp = (new_height - want_height)/2
        background = background.crop((0, temp, want_width, temp+want_height))
    else:
        new_height = want_height
        new_width = new_height * width / height
        background = background.resize((int(new_width), new_height), Image.ANTIALIAS)
        temp = (new_width - want_width)/2
        background = background.crop((temp, 0, temp+want_width, want_height))

    # Mearges with overlay
    foreground = Image.open(overlay_image)
    background.paste(foreground, (0, 0), foreground)
    background.save(output_folder+"/"+filename+".png")

    # Removes old image
    os.remove(watch_folder+"/"+filename+"."+fileformat)

    # Debugg
    print("Mearge of image "+filename+"."+fileformat+" was complete.")


count = 0

while True:
    HEJSAN = os.listdir(os.getcwd()+"/"+watch_folder)
    for file_name in HEJSAN:
        print("Found file(s) in the watch folder")
        try:
            name = re.search('(.+)\.[\w]+$', file_name).group(1)
            extention = re.search('.([\w]+)$', file_name).group(1)
            do_stuff(name, extention)
        except:
            print("Could not apply magic to '"+file_name+"'")
    time.sleep(1)
    print("Seconds since start: "+str(count))
    count += 1

