BASE_PATTERN = "^[A-Z]{1,2}[0-9][A-Z0-9]? ?[0-9][A-Z]{2}$"
WITH_SPECIAL_CASES_PATTERN = "^(([A-Z]{1,2}[0-9][A-Z0-9]?|ASCN|STHL|TDCU|BBND|[BFS]IQQ|PCRN|TKCA) ?[0-9][A-Z]{2}|BFPO ?[0-9]{1,4}|(KY[0-9]|MSR|VG|AI)[ -]?[0-9]{4}|[A-Z]{2} ?[0-9]{2}|GE ?CX|GIR ?0A{2}|SAN ?TA1)$"

LIMITED_POST_CODES_CHUNKS = (
    ("AI", "2640"),  # Anguilla
    ("ASCN", "1ZZ"),  # Ascension Island
    ("BBND", "1ZZ"),  # British Indian Ocean Territory
    ("BFPO", "57"),  # Akrotiri And Dhekelia
    ("BFPO", "58"),  # Akrotiri And Dhekelia
    ("BF1", "2AT"),  # Akrotiri And Dhekelia
    ("BF1", "2AU"),  # Akrotiri And Dhekelia
    ("BIQQ", "1ZZ"),  # British Antarctic Territory
    ("FIQQ", "1ZZ"),  # Falklands
    ("PCRN", "1ZZ"),  # Pitcairn Islands
    ("SIQQ", "1ZZ"),  # South Georgia South Sandwich Islands
    ("STHL", "1ZZ"),  # Saint Helena
    ("TDCU", "1ZZ"),  # Tristan da Cunha
    ("TKCA", "1ZZ"),  # Turks Caicos Islands
    ("VG", "1110"),  # Tortola Central
    ("VG", "1120"),  # Tortola East
    ("VG", "1130"),  # Tortola West
    ("VG", "1140"),  # Anegada
    ("VG", "1150"),  # Virgin Gorda
    ("VG", "1160"),  # Jost Van Dyke
)
