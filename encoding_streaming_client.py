#!/usr/bin/env python
import cv2
import numpy as np
import pickle
import urllib

if __name__ == '__main__':
    import sys, getopt
    print(__doc__)

    streamurl = str(sys.argv[1])
    stream = urllib.urlopen(streamurl)
   	
    print (stream)

    bytes=''
    i = 0
    while True:
        # print(time.time())
        bytes += str(stream.read(163840))
        a = bytes.find('[start]')
        b = bytes.find('[finish]')


        if a != -1 and b != -1:

            jpg = bytes[a + 7:b]
            bytes = bytes[b + 8:]

            img = pickle.loads(jpg)

            r, buf = cv2.imencode(".jpg", img)

            cv2.imshow('image',img)

            if cv2.waitKey(5) == 27:
                break
