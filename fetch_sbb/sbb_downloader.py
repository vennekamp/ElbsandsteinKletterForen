import urllib.request
import os

def get_files_dir(run_name: str):
    # Directory to save the database file
    dirname = os.path.dirname(__file__)
    d = os.path.join(dirname, run_name)
    os.makedirs(d, exist_ok=True)
    return d

if __name__ == '__main__':
    numberOfPages = 490
    baseurl = "https://www.sbbdb.de/public/agnw/wege?page="
    baseFolder = get_files_dir('sbb_HTMLfiles') + "\page_no"

    for x in range(0, numberOfPages):
        i = x + 1
        print("Starte Laden der Datei " + str(i).zfill(3), end=" - ")
        url = baseurl + str(i)
        response = urllib.request.urlopen(url)
        data = response.read()      # a `bytes` object
        text = data.decode("UTF-8",  errors="backslashreplace")  # ('ISO-8859-1') # a `str`; this step can't be used if data is binary
        with open(baseFolder + str(i).zfill(3) + ".html", "w", encoding="utf-8") as text_file:
            text_file.write(text)
        print(" erledigt! " + "{:05.1f}".format(i*100 / numberOfPages) + "%")
