link do docsa z etapu 1:  
https://docs.google.com/document/d/1skbyKSlhSn320t2YR83KhIkbkRXluPliXLINKGTkQZ4/edit?usp=sharing

#### Instrukcja instalacji MySQL
* Należy pobrać MySQL ze strony https://dev.mysql.com/downloads/mysql/ (wariant Linux Generic).
  Otrzymane archiwum należy zapisać w katalogu ~/bd2_23L_z09_mysql pod nazwą mysql.tar.xz
    Bezpośredni link do pobrania:
        wersja 32-bitowa: https://dev.mysql.com/get/Downloads/MySQL-8.0/mysql-8.0.31-linux-glibc2.12-i686.tar.xz
        wersja 64-bitowa: https://dev.mysql.com/get/Downloads/MySQL-8.0/mysql-8.0.31-linux-glibc2.12-x86_64.tar.xz
    Można to osiągnąć z linii poleceń następującą komendą:
        wersja 32-bitowa:
`mkdir ~/bd2_23L_z09_mysql && wget https://dev.mysql.com/get/Downloads/MySQL-8.0/mysql-8.0.31-linux-glibc2.12-i686.tar.xz -O ~/bd2_23L_z09_mysql/mysql.tar.xz`
        wersja 64-bitowa:
`mkdir ~/bd2_23L_z09_mysql && wget https://dev.mysql.com/get/Downloads/MySQL-8.0/mysql-8.0.31-linux-glibc2.12-x86_64.tar.xz -O ~/bd2_23L_z09_mysql/mysql.tar.xz`
* Należy uruchomić skrypt instalacyjny `install.sh`. Jeżeli wyświetlony zostanie napis "Error
while loading shared libraries", należy brakujące biblioteki doinstalować i uruchomić skrypt ponownie. Potrzebna
może się okazać instalacja pakietów libnuma1, libtinfo5, libaio1 lub innych.
