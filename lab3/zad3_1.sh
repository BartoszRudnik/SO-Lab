#!/bin/bash -eu


# Znajdź w pliku access_log zapytania, które mają frazę ""denied"" w linku
grep -o "\".*/denied.*\"" access_log
echo "-------------------------------------------------------------------------------------------------------"

# Znajdź w pliku access_log zapytania typu POST
grep -o "\"POST.*HTTP/.\..\"" access_log
echo "-------------------------------------------------------------------------------------------------------"

# Znajdź w pliku access_log zapytania wysłane z IP: 64.242.88.10
grep -w "64\.242\.88\.10.-.-" access_log | cut -d' ' -f1,6,7,8
echo "-------------------------------------------------------------------------------------------------------"

# Znajdź w pliku access_log wszystkie zapytania NIEWYSŁANE z adresu IP tylko z FQDN
grep "^[a-z]" access_log | cut -d' ' -f1,6,7,8
echo "-------------------------------------------------------------------------------------------------------"

# Znajdź w pliku access_log unikalne zapytania typu DELETE
grep -o "\"DELETE.*HTTP/.\..\"" access_log | sort -u
echo "-------------------------------------------------------------------------------------------------------"

# # Znajdź unikalnych 10 adresów IP w access_log
grep -E -o "^([0-9]{1,3}[\.]){3}[0-9]{1,3}" access_log | sort -u | sed 10q
echo "-------------------------------------------------------------------------------------------------------"

