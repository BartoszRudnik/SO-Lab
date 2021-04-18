#!/bin/bash -eu

#Z pliku yolo.csv wypisz wszystkich, których id jest liczbą nieparzystą. Wyniki zapisz na standardowe wyjście błędów.
grep -E "^[0-9]{0,3}[1,3,5,7,9]{1}," yolo.csv 1>&2
echo "-------------------------------------------------------------------------------------------------------"

#Z pliku yolo.csv wypisz każdego, kto jest wart dokładnie $2.99 lub $5.99 lub $9.99. Nie wazne czy milionów, czy miliardów (tylko nazwisko i wartość). Wyniki zapisz na standardowe wyjście błędów
grep -Ew "[2,5,9]\.99.$" yolo.csv | cut -d',' -f3,7 1>&2
echo "-------------------------------------------------------------------------------------------------------"

#Z pliku yolo.csv wypisz każdy numer IP, który w pierwszym i drugim oktecie ma po jednej cyfrze. Wyniki zapisz na standardowe wyjście błędów
grep -Ew "[0-9]{1}[\.][0-9]{1}[\.][0-9]{1,3}[\.][0-9]{1,3}" yolo.csv | cut -d',' -f6 1>&2
echo "-------------------------------------------------------------------------------------------------------"
