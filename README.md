# OverlayImageJoiner
A small program that adds a overlay image to all images inside a watch folder. The goal with this program was to create better product images that standed out more for my product listings on [tradera.com](https://www.tradera.com/). I never used it live but it's a great little software non the less.

## Basic workflow of the program:
* Watches the watch folder for new images
* When it founds a image, combined it by puting the overlay image on top of the original, use a transparent png overlay image in order to see though to the original image
* Puts the final image in the output folder
* Removes the original file from the watchfolder

## Configure
On the top of the `imageoverlayjoiner.py` file is a section where you can specify your desierd resolution of the output image and also the paths to the watch folder, output folder and the overlay image.

## How to run
* You need to have `python` installed
* Install Pillow though pip `pip install Pillow`
* Install Regex though pip `pip install regex`
* Stand in the project folder and type `python overlayimagejoiner.py`.

The program is then active and all images put in the watch foler will be combined with the overlay image and then puts the final image in the output folder. You can try with the example images in the `example_images/` folder.
