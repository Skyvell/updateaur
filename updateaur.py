import os
import subprocess
import argparse

def update_aur(path):
        """
        Simpel script which aquires build files for AUR pacakges, via git pull, and installs the packages.
        
        Arguments:
        path -  absolute path to the directory containing you builds.
        """
        os.chdir(path)
        gen =  os.walk(path)
        directories = gen.__next__()[1]

        for dir in directories:
                os.chdir(path + "/" + dir)
                result = subprocess.run(["git", "pull"], stdout=subprocess.PIPE)
                if result.stdout.decode('utf-8').strip() is "Already up-to-date.":  #this does not work
                        continue
                else:
                        subprocess.run(["makepkg", "-si"])


def main():
        parser = argparse.ArgumentParser()
        parser.add_argument("path", help = "The absolute path to the directory containing your AUR packages.", type = str)
        
        args = parser.parse_args()
        update_aur(args.path)

if __name__ == "__main__":
        main()
