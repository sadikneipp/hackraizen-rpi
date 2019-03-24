import subprocess
from acquisition import camera

filename = 'image.jpg'

webcam = camera.init_camera()
camera.save_ss(webcam, 'image.jpg')

test = subprocess.Popen(["sudo", "docker", "run", "-it", "--rm" ,
                         "-v" , "$(pwd):/data:ro", "openalpr", 
                         "-c" ,"eu" , filename],
                        stdout=subprocess.PIPE)

output = test.communicate()[0]
print(output)