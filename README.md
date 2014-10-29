# Zdalne logowanie

## Zadanie

Pierwsze zadanie programistyczne polega na implementacji protokołu zdalnego logowania się użytkownika klienta do serwera. W tym celu należy zaimplementować osobne moduły klienta i serwera, które będą pozwalały na zdalną komunikację przez sieć. Serwer powinien być wielowątkowy, aby mógł jednocześnie odbierać i realizować żądania od kilku klientów. Serwer powinien posiadać pewne symulowane "zasoby": bazę użytkowników, ich bazę haseł (odpowiednio skonfigurowaną), dodatkowo zasoby "systemu plikowego", aby klient mógł zażądać odczytania niektórych, ewentualnie ich modyfikacji.

Klient musi mieć możliwość zdalnego zalogowania się poprzez jeden z protokołów typu wyzwanie-odpowiedź, jednak bez użycia szyfrowania asymetrycznego. Po zalogowaniu, klient powinien mieć możliwość odczytania/modyfikacji niektórych (dostępnych dla niego) zasobów, także zmiany swojego hasła, na koniec wylogowania się. Pomysłowość będzie tu mile widziana.

Cały projekt ma być wykonany w języku Python w wersji 2.7x, nie wyżej, nie niżej. Oceniane będą poprawność protokołu bezpieczeństwa, poprawność architektury sieciowej, styl napisania rozwiązania, czystość kodu (tu wykorzystane będzie narzędzie pylint), niezbędne komentarze w kodzie, dokumentacja (krótka w postaci osobnego pliku pdf, najlepiej generowana w sposób automatyczny). Projekty w innych językach nie będą przyjmowane.

Warto jest dobrze zaimplementować architekturę klienta i serwera, bo wszelkie ich funkcjonalności na pewno przydadzą się w kolejnych zadaniach.

Do programowania w Pythonie polecam bardzo wygodne środowisko PyCharm w wersji Community. Jeśli ktoś chce ułatwić sobie instalację Pythona, to polecam pakiet anaconda zawierający większość pakietów związanych z naukami ścisłymi.

Oczywiście sprawdzana będzie unikalność kodu.