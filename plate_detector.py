import subprocess
from acquisition import camera
import os
import time

pwd = os.getcwd()
filename = 'image.jpg'
while True:
    webcam = camera.init_camera()
    for i in range(2):
        camera.save_ss(webcam, filename)
        time.sleep(1)
    camera.stop_camera(webcam)

    test = subprocess.Popen(["sudo", "docker", "run", "-it", "--rm" ,
                         "-v" , pwd + ":/data:ro", "openalpr", 
                         "-c" ,"eu" , "-p", "@@@####", filename],
                        stdout=subprocess.PIPE)

    #os.remove(filename)

    output = test.communicate()[0]
    print(output)
