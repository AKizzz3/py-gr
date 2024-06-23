### README.md

# Skrypt do Zbierania Danych Diagnostycznych

To repozytorium zawiera skrypty w języku Python do zbierania danych diagnostycznych z komputera z systemem Windows. Skrypty wykonują różne polecenia systemowe i polecenia PowerShell, zapisują wyniki w plikach tekstowych i wysyłają te pliki na określony webhook.

## Pliki w Repozytorium

- `main.py`: Główny skrypt, który zarządza procesem zbierania i wysyłania danych.
- `funk.py`: Zawiera funkcje pomocnicze używane przez główny skrypt.

## Wymagania

- Python 3.x
- Moduły: `os`, `subprocess`, `requests`

## Instalacja

1. Sklonuj repozytorium na swój komputer:
    ```bash
    git clone https://github.com/twoje-repozytorium.git
    ```

2. Zainstaluj wymagane moduły:
    ```bash
    pip install requests
    ```

## Użycie

1. Uruchom `main.py`, aby rozpocząć proces zbierania danych diagnostycznych:
    ```bash
    python main.py
    ```

2. Skrypt utworzy folder `C:\dane_diagnostyczne`, jeśli nie istnieje, i zapisze w nim pliki z danymi diagnostycznymi.

3. Skrypt następnie wyśle te pliki na podany webhook.

## Funkcje

### `main.py`

- `main()`: Główna funkcja zarządzająca procesem zbierania danych.
    - Tworzy folder `C:\dane_diagnostyczne`.
    - Usuwa stare pliki diagnostyczne.
    - Wykonuje różne polecenia systemowe i PowerShell, zapisując wyniki w plikach tekstowych.
    - Wysyła pliki na webhook.

### `funk.py`

- `execute_cmd(commands)`: Wykonuje listę poleceń w wierszu poleceń.
- `wyslij_plik_do_webhooka(webhook_url, folder_path, file_name)`: Wysyła plik na podany URL webhooka.
- `czy_znaleziono_folder(sciezka)`: Sprawdza, czy istnieje dany folder.
- `lista_plikow_w_folderze(folder_path)`: Zwraca listę plików w danym folderze.
- `usun_pliki_z_diagnozy()`: Usuwa pliki diagnostyczne z folderu `C:\dane_diagnostyczne`.
- `extract_wifi_profiles(file_path)`: Ekstrahuje profile WiFi z pliku.
- `uruchom_komende(komenda, nazwa_pliku)`: Uruchamia polecenie i zapisuje wynik w pliku.
- `run_powershell_command(command, output_file)`: Uruchamia polecenie PowerShell i zapisuje wynik w pliku.

