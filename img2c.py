#!/usr/bin/env python2

import re
import os
from PIL import Image
import sys

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print "Incorect invocation\n \
Example use: \n \
./img2c.py \"/directory/path/to/images\""
        exit()

    #allow handling of both full and relative paths
    os.chdir(sys.argv[1])

    sprite_name = raw_input("What is the name of this Sprite? ")
    filename = 'frames.h'
    f = open(filename, "w+")

    #put all png files in a list
    png_files = [i for i in os.listdir('./') if re.search(r'.*png',i)]

    im = Image.open(png_files[0])
    dimx = im.size[0]
    dimy = im.size[1]
    print "First image found has a size of " + str(dimy) + "x" + str(dimx)
    print "Generating array that assumes all images are of this size"
    f.write("int %s_frames[%d][%d*%d] = {\n" % (sprite_name, len(png_files), dimy, dimx))

    for i, arg in enumerate(png_files):
        im = Image.open(arg)
        pix = im.load()
        f.write("//%s_frame_%d\n{\n" %(sprite_name,i))
        for y in xrange(0, im.size[1]):
            for x in xrange(0, im.size[0]):
                r, g, b, a = pix[x, y]
                #f.write("%s, " % hex(a<<24|r<<16|g<<8|b) )
                f.write("%s, " % hex(r<<16|g<<8|b) )

            f.write("\n");

        f.write("},\n")
    f.write("};\n")
    f.close()
