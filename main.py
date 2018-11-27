import os
import requests
import time
import tarfile
import wget
import subprocess
class Task:
    image_url = "https://s3.eu-central-1.amazonaws.com/devops-exercise/pandapics.tar.gz"
    file_place = "./ops-exercise/public/images/pandapics.tar.gz"
    health_url = "http://127.0.0.1:3000/health"

    def extractimage(self):
        if not os.path.exists("./ops-exercise/public/images"):
            os.makedirs("./ops-exercise/public/images")
        if os.path.isfile(self.file_place):
            print("The tar file exist, no need download the tar file")
        else:
            print('Beginning file download with wget module')
            result = wget.download(self.image_url, self.file_place)
            if result == self.file_place:
                print('the tar file downloaded')
        tar = tarfile.open(self.file_place)
        tar.extractall(path="./ops-exercise/public/images/")
        if os.path.isfile(self.file_place):
            os.remove(self.file_place)

    def dockercompose(self):
        print("Run docker compose")
        print("###############################################")
        print("Waiting 2 min until docker-compose will finish ")
        print("###############################################")
        p1 = subprocess.Popen(['docker-compose', 'up'])
        time.sleep(120)

    def is_healthy(self):
        request = requests.get(self.health_url)
        if request.status_code == 200:
           print('Web site exists')
        else:
           print('Web site does not exist')
           p1 = subprocess.Popen(['docker-compose', 'down'])


def main():
    instance = Task()
    instance.extractimage()
    instance.dockercompose()
    instance.is_healthy()

if __name__ == "__main__":
    main()










