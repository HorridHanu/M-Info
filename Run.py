#
#!/usr/bin/python3
#
#  [Program]
#
#  MI
#  Movie Info
#
#  [Author]
#  HorridHanu
#
#
#
#  [License]
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#
#  See 'LICENSE' for more information.


import imdb
from colorama import Fore


__author__ = "Horrid Hanu"
__license__ = "GPL (GENERAL PUBLIC LICENSE)"
__version__ = "1.0"

print(f"{Fore.CYAN}\n")
print("##   ##   ######   ###    ##   ##   ##")
print("##   ##   ##  ##   ## #   ##   ##   ##")
print("#######   ######   ##  #  ##   ##   ##")
print("##   ##   ##  ##   ##   # ##   ##   ##")
print("##   ##   ##  ##   ##    ###   #######")

print(f"{Fore.RED}\n", 3 * " " + "[ HorridHanu | https://github.com/HorridHanu/]\r")
print(f'{Fore.CYAN}[*] Code By HorridHanu(^_~).')
print(f'{Fore.CYAN}[*] Get Movie Info.')


while True:




    print(f"{Fore.BLUE}\n###########################################")
    print(*"* 1 Search Movie :) ")
    print(*"* 2 Help :) ")
    print(*"* 3 About :) ")
    print(*"* 4 Exit :) ")
    print("###########################################\n")


    Run_Choice = int(input("Enter the choice (: "))
    if Run_Choice == 1:



        print("\nEnter the movie name and hit enter!")
        Name = input(f"{Fore.RED}[+] Enter the movie name (: ")
        print(f"\n\t{Fore.CYAN}[-] Searching",  Name, "movie..\n")



        imdbObject = imdb.IMDb()
        MovieName = Name
        Movies = imdbObject.search_movie(MovieName)
        index = Movies[0].getID()
        Movie = imdbObject.get_movie(index)





        """Title"""
        Title = Movie['title']
        print(f"{Fore.MAGENTA}[+] Title (:          " + Title)


        """Directors"""
        for Directors in Movie['director']:
            print("[+] Director (:      ", Directors)


        """Years"""
        print("[+] Year (:          ", Movie['year'])


        """Runtime"""
        for runtime in Movie['runtime']:
            Hours = int(runtime)//60
            Minutes = int(runtime)%60
            print("[+] Runtime (:       ", f"{Hours} Hour {Minutes} Minutes.")


        """Genres"""
        Genres = Movie['genres']
        print("[+] Genres (:        ", Genres)


        """Rating"""
        Rate = Movie['rating']
        print("[+] Rating (:        ", Rate)


        """Cast"""
        Cast = Movie['cast']
        castlist = list(map(str, Cast))
        slice = castlist[:10]
        print("[+] Cast (:          ", slice)


    elif Run_Choice == 2:
        print(f"\n{Fore.CYAN} ", 20*" ", "HELP.")
        print(f"{Fore.RED}[-] *. Check your internet connection must be stable :( ")
        print("[-] *. Check all the recommended packages installed :( ")


        print("\n* 1 List of packages.\n* 2 Exit.")
        Help = int(input(">Help : "))
        if Help == 1:
            print("\n[-] These packages must be installed!")
            print("[+] Colorama : pip install colorama")
            print("[+] Imdb : pip install imdbpy")
            print("[+] Upgrade pip : pip install --upgrade pip (Not recommended❕)")

        else:
            exit()
    elif Run_Choice == 3:
        print(f"\n{Fore.CYAN} ", 20 * " ", "VERSION.")
        print(f"{Fore.CYAN}[*] Version is ", __version__,
              "\n[*] GUI version AVAILABLE"
              "\n[*] Go To https://Github.com/HorridHanu/MovieInfo-Python"
              f"\n[*] Author {__author__}"
              f"\n[*] License {__license__}")

    elif Run_Choice == 4:
        print(f"{Fore.MAGENTA}\nEXIT..")
        print(f"\t\t######################")
        print("\t\t# Thanks for using.. #\n"
              "\t\t######################")
        exit()


