# Waveshare Modbus PoE Ethernet Relay — Home Assistant

Integracja lokalna do sterowania modułami przekaźnikowymi Waveshare przez Modbus TCP. Obsługuje moduły 8-, 16- i 30-kanałowe, w tym Waveshare 24964 (8 kanałów).

## Instalacja przez HACS

1. W HACS otwórz menu ⋮ → **Repozytoria niestandardowe**.
2. Dodaj `https://github.com/geogarden/ha-waveshare-relay` jako **Integracja**.
3. Pobierz integrację i uruchom ponownie Home Assistant.
4. Otwórz **Ustawienia → Urządzenia i usługi → Dodaj integrację** i wyszukaj **Waveshare Modbus PoE Ethernet Relay**.
5. Podaj adres IP modułu, jego port Modbus TCP, adres urządzenia (Unit ID), odstęp odczytów i liczbę przekaźników. Wartości muszą odpowiadać konfiguracji modułu.

## Język polski

W profilu użytkownika Home Assistant ustaw język **Polski**. Formularze, tryby kanałów, przyciski, nazwy statystyk i opisy akcji będą dostępne po polsku. Po aktualizacji uruchom ponownie Home Assistant i odśwież przeglądarkę.

Własne nazwy kanałów, identyfikatory encji i identyfikatory akcji pozostają bez zmian. Domyślne nazwy kanałów zapisane wcześniej jako „Relais 1” itp. możesz zmienić w opcjach integracji. Nazwy nadpisane ręcznie w rejestrze encji mają pierwszeństwo przed tłumaczeniem.

## Tryby kanałów

- **Przełącznik** — przekaźnik pozostaje włączony do otrzymania polecenia wyłączenia.
- **Impuls** — moduł sam wyłącza przekaźnik po ustawionym czasie impulsu.

Tryb i czas impulsu ustawisz w opcjach integracji. Zmiana trybu zachowuje identyfikator encji.

## Akcje

- **Uruchom test działania** — włącza kolejno przekaźniki; uruchamiaj dopiero po sprawdzeniu podłączonych odbiorników.
- **Zatrzymaj test działania** — zatrzymuje test i wyłącza przekaźniki.
- **Wyłącz wszystkie przekaźniki** — wyłącza wszystkie kanały wybranego modułu.
- **Wyzeruj statystyki** — zeruje liczniki i czasy.

Bez wskazania urządzenia akcje dotyczą wszystkich skonfigurowanych modułów.

Pełna dokumentacja techniczna: [README.md](README.md), [sprzęt i połączenie](docs/HARDWARE.md).

## Wersja 1.1.9

- Dodano język polski oraz polską instrukcję instalacji.
- Nazwy encji i etykiety trybów korzystają z mechanizmu tłumaczeń Home Assistant.
- Stan testu ma wartości `idle` / `running`, wyświetlane po polsku jako „Nieaktywny” / „W trakcie”; numer bieżącego kanału pozostaje w atrybucie `aktueller_kanal`.
