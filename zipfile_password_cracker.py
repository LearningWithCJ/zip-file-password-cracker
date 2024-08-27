#
#  _                                _                __          __ _  _    _        _____      _ 
# | |                              (_)               \ \        / /(_)| |  | |      / ____|    | |
# | |      ___   __ _  _ __  _ __   _  _ __    __ _   \ \  /\  / /  _ | |_ | |__   | |         | |
# | |     / _ \ / _` || '__|| '_ \ | || '_ \  / _` |   \ \/  \/ /  | || __|| '_ \  | |     _   | |
# | |____|  __/| (_| || |   | | | || || | | || (_| |    \  /\  /   | || |_ | | | | | |____| |__| |
# |______|\___| \__,_||_|   |_| |_||_||_| |_| \__, |     \/  \/    |_| \__||_| |_|  \_____|\____/ 
#                                              __/ |                                              
#                                             |___/                         -  By CJ
#
# YouTube : www.youtube.com/@LearningWithCJ
# GitHub  : www.github.com/LearningWithCJ
# Telegram: t.me/LearningWithCJ
#

import zipfile, os



ZIP_PATH = fr"" # enter path of zip file
UNZIP_PATH = fr"" # enter path where you wanna extract zip file
PASSWORDLIST_PATH = fr"" # enter path of password list


class Crack():
    def __init__(self, zip_file, unzip_path, passlist_path):
        self.zipFile = zip_file
        self.unzipFile = unzip_path
        self.passFile = passlist_path
        self.passlist = []

    def checkFiles(self):
        if os.path.exists(self.zipFile):
            if os.path.exists(self.passFile):
                file = open(self.passFile, "r", encoding="utf-8")
                self.passlist = file.readlines()
                self.crackZip()
            else:
                print("Password List Is Not Exists.")
        else:
            print("Zip File Is Not Exists.")

    def crackZip(self):
        with zipfile.ZipFile(self.zipFile, "r") as zipObject:
            num = 0
            while num + 1 <= len(self.passlist):
                password = self.passlist[num]
                print("Attempt " + str(num + 1) + "\nPassword: " + password.replace("\n", ""))
                try:
                    zipObject.extractall(path=self.unzipFile, pwd=bytes(password.replace("\n", ""), "utf-8"))
                    print("Zip File Cracked, Password: " + password)
                    break
                except NotImplementedError:
                    print("Error: Zip Legacy Encryption Is Not Enabled.")
                    break
                except PermissionError:
                    print("Error: Permission Denied.")
                    break
                except zipfile.BadZipFile:
                    print("Error: Bad Zip File.")
                    break
                except zipfile.LargeZipFile:
                    print("Error: Zip File Is Too Large.")
                    break
                except RuntimeError as e:
                    print("Error: " + str(e) + "\n")
                    num += 1
                except Exception as e:
                    print("Error: " + str(e) + "\n")
                    num += 1



if __name__ == "__main__":
    crack = Crack(ZIP_PATH, UNZIP_PATH, PASSWORDLIST_PATH)
    crack.checkFiles()
