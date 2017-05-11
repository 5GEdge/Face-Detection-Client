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

    while True:
        bytes+=stream.read(16384)
        a = bytes.find('\xff\xd8')
        b = bytes.find('\xff\xd9')

        if a != -1 and b != -1:
            jpg = bytes[a:b + 2]
            bytes = bytes[b + 2:]
            i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), 1)

            
            cv2.imshow('image',i)
            

            if cv2.waitKey(5) == 27:
                break