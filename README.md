## BD2 - Obsługa banku
Projekt ma na celu przygotowanie i zarządzanie bazą danych banku.

#### Dokumentacja projektu
Dokumentacja projektu jest zawarta w plikach .pdf w repozytorium:
* z etapu 1: BD2_z09_etap_1.pdf
* z etapu 2: BD2_z09_etap_2.pdf
* z etapu 3: BD2_z09_etap_3.pdf

#### Instrukcja instalacji MySQL
* Należy uruchomić skrypt instalacyjny `./install.sh`. Jeżeli wyświetlony zostanie napis "Error
while loading shared libraries", należy brakujące biblioteki doinstalować i uruchomić skrypt ponownie. Potrzebna
może się okazać instalacja pakietów libnuma1, libtinfo5, libaio1 lub innych.

#### Instrukcja uruchomienia aplikacji
* Zainstalować interpreter Pythona w wersji co najmniej 10.
* Zainstalować pakiet libmysqlclient-dev.
* Zainstalować biblioteki języka Python określone w pliku requirements.txt komendą `pip install -r requirements.txt`
* Uruchomić bazę danych komendą `./mysql.sh start`
* Uruchomić aplikację komendą `python3 main.py`
