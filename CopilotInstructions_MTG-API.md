# Copilot Instructions: Magic: The Gathering APIs

## Übersicht

Dieses Dokument bietet eine umfassende Anleitung für AI Copilots zur Arbeit mit Magic: The Gathering APIs. Es enthält Entscheidungsbäume, Code-Beispiele und Best Practices für die drei verfügbaren API-Systeme.

---

## 📋 Inhaltsverzeichnis

1. [API-Auswahllogik](#api-auswahllogik)
2. [Scryfall API](#scryfall-api)
3. [magicthegathering.io API](#magicthegatheringio-api)
4. [Moxfield API (inoffiziell)](#moxfield-api-inoffiziell)
5. [Best Practices](#best-practices)
6. [Fehlerbehandlung](#fehlerbehandlung)

---

## API-Auswahllogik

### Entscheidungsbaum: Welche API soll verwendet werden?

```
User-Anfrage analysieren
│
├─ Sucht nach DECK-Daten von Moxfield?
│  └─ JA → Moxfield API (inoffiziell)
│
├─ Benötigt BULK-Download aller Karten?
│  └─ JA → Scryfall Bulk Data
│
├─ Benötigt BILDSUCHE oder hochauflösende Card Images?
│  └─ JA → Scryfall API
│
├─ Benötigt PREISE (TCGPlayer, Cardmarket)?
│  └─ JA → Scryfall API (Preise mit 24h Aktualität)
│
├─ Entwickelt mit PYTHON/RUBY/JS SDK?
│  └─ JA → magicthegathering.io API (offizielle SDKs)
│
├─ Benötigt BOOSTER-Pack Simulation?
│  └─ JA → magicthegathering.io API (/sets/:id/booster)
│
├─ Benötigt ERWEITERTE Such-Syntax (komplexe Queries)?
│  └─ JA → Scryfall API (mächtigere Suchsyntax)
│
└─ Standard-Kartensuche / Set-Informationen?
   └─ BEIDE möglich → Bevorzuge Scryfall API (bessere Performance)
```

### Quick Reference: API-Stärken

| Feature | Scryfall | magicthegathering.io | Moxfield |
|---------|----------|---------------------|----------|
| **Kartensuche** | ⭐⭐⭐ | ⭐⭐ | ⭐ |
| **Preisdaten** | ⭐⭐⭐ | ❌ | ⭐⭐ |
| **Bulk Downloads** | ⭐⭐⭐ | ❌ | ❌ |
| **SDKs** | ⭐⭐ | ⭐⭐⭐ | ⭐ |
| **Deck Import** | ❌ | ❌ | ⭐⭐⭐ |
| **Dokumentation** | ⭐⭐⭐ | ⭐⭐ | ⭐ (inoffiziell) |
| **Rate Limits** | 10/sec | 5000/hour | Unbekannt |
| **Stabilität** | ⭐⭐⭐ | ⭐⭐⭐ | ⭐ (inoffiziell) |

---

## Scryfall API

### Base Information

```python
BASE_URL = "https://api.scryfall.com"
RATE_LIMIT = 10  # requests per second
DELAY_MS = 100  # recommended delay between requests
```

### Erforderliche Headers

```python
HEADERS = {
    "User-Agent": "YourAppName/1.0",
    "Accept": "application/json"
}
```

### 🎯 Anwendungsfälle

1. **Kartensuche mit erweiterten Filtern**
2. **Preisabfragen (TCGPlayer, Cardmarket, etc.)**
3. **Hochauflösende Kartenbilder**
4. **Bulk-Downloads der gesamten Datenbank**
5. **Set-Informationen**
6. **Autocomplete für Kartennamen**

---

### 1. Kartensuche (`/cards/search`)

#### Grundlegende Suche

```python
import requests
import time

def search_scryfall_cards(query, unique="cards", order="name"):
    """
    Sucht Karten auf Scryfall mit erweiterten Optionen.
    
    Args:
        query: Scryfall-Suchsyntax (z.B. "c:red type:creature")
        unique: "cards", "art", "prints" (default: "cards")
        order: "name", "released", "usd", "tix", "eur", "cmc" (default: "name")
    
    Returns:
        Liste von Karten-Dictionaries
    """
    url = "https://api.scryfall.com/cards/search"
    params = {
        "q": query,
        "unique": unique,
        "order": order
    }
    headers = {
        "User-Agent": "MTGApp/1.0",
        "Accept": "application/json"
    }
    
    all_cards = []
    
    while url:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        all_cards.extend(data.get("data", []))
        
        # Pagination
        url = data.get("next_page")
        params = None  # Nach erster Anfrage keine params mehr
        
        if url:
            time.sleep(0.1)  # Rate limit beachten
    
    return all_cards


# Beispiele für Queries
examples = {
    "Rote Kreaturen mit Power 3+": "c:red t:creature pow>=3",
    "Legendäre Kommander (Izzet)": "c:UR t:legendary t:creature",
    "Karten unter 1€": "eur<1",
    "Standard-legale Planeswalker": "f:standard t:planeswalker",
    "Karten aus bestimmtem Set": "s:neo",
    "Suche nach Kartentext": "o:\"draw a card\"",
    "Mythic Rares": "r:mythic",
}

# Verwendung
red_creatures = search_scryfall_cards("c:red t:creature pow>=3")
for card in red_creatures[:5]:
    print(f"{card['name']} - Power: {card.get('power')}")
```

#### Erweiterte Scryfall-Suchsyntax

```
Farbfilter:
  c:w / c:u / c:b / c:r / c:g  (Farben)
  c:wu (mehrfarbig: Weiß UND Blau)
  c<=urg (maximal diese Farben)
  
Kartentypen:
  t:creature / t:instant / t:sorcery / t:artifact / t:enchantment
  t:legendary (Supertypes)
  
Stats:
  pow>=3 (Power >= 3)
  tou<=2 (Toughness <= 2)
  cmc=3 (Converted Mana Cost)
  
Preis:
  usd<5 (USD Preis unter 5$)
  eur<10 (Euro Preis unter 10€)
  tix<1 (MTGO Tickets)
  
Format:
  f:standard / f:modern / f:commander / f:legacy / f:vintage
  banned:standard (in Standard verboten)
  
Set:
  s:neo (Set-Code: Kamigawa Neon Dynasty)
  s:khm (Kaldheim)
  
Text:
  o:"draw a card" (Oracle Text)
  ft:"flavor text" (Flavor Text)
  
Kombinationen:
  c:r t:creature pow>=4 f:standard (Standard-legale rote Kreaturen mit Power 4+)
```

---

### 2. Einzelne Karte abrufen

```python
def get_card_by_name(card_name, exact=True):
    """
    Ruft eine Karte nach Namen ab.
    
    Args:
        card_name: Name der Karte
        exact: True für exakte Suche, False für fuzzy search
    """
    endpoint = "exact" if exact else "fuzzy"
    url = f"https://api.scryfall.com/cards/named"
    params = {endpoint: card_name}
    headers = {"User-Agent": "MTGApp/1.0"}
    
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    return response.json()


# Beispiel
lightning_bolt = get_card_by_name("Lightning Bolt")
print(f"Name: {lightning_bolt['name']}")
print(f"Mana Cost: {lightning_bolt['mana_cost']}")
print(f"Type: {lightning_bolt['type_line']}")
print(f"Oracle Text: {lightning_bolt['oracle_text']}")
print(f"USD Price: ${lightning_bolt['prices']['usd']}")
```

---

### 3. Kartenbilder abrufen

```python
def get_card_image(card_name, image_type="normal"):
    """
    Ruft Karten-Bild URL ab.
    
    Args:
        card_name: Name der Karte
        image_type: "small", "normal", "large", "png", "art_crop", "border_crop"
    
    Returns:
        URL zum Bild
    """
    card = get_card_by_name(card_name)
    return card["image_uris"][image_type]


# Verfügbare Bildtypen
image_types = {
    "small": "Thumbnail (146x204)",
    "normal": "Normal (488x680)",
    "large": "Large (672x936)",
    "png": "Full PNG (745x1040)",
    "art_crop": "Nur Artwork",
    "border_crop": "Karte mit schwarzem Rand"
}

# Verwendung
image_url = get_card_image("Black Lotus", "png")
print(f"Image URL: {image_url}")

# Download Bild
import requests
response = requests.get(image_url)
with open("black_lotus.png", "wb") as f:
    f.write(response.content)
```

---

### 4. Preisabfragen

```python
def get_card_prices(card_name):
    """
    Ruft aktuelle Preise für eine Karte ab.
    
    Returns:
        Dict mit Preisen in verschiedenen Währungen/Plattformen
    """
    card = get_card_by_name(card_name)
    prices = card.get("prices", {})
    
    return {
        "usd": prices.get("usd"),  # TCGPlayer Normal
        "usd_foil": prices.get("usd_foil"),  # TCGPlayer Foil
        "eur": prices.get("eur"),  # Cardmarket Normal
        "eur_foil": prices.get("eur_foil"),  # Cardmarket Foil
        "tix": prices.get("tix")  # MTGO Tickets
    }


# Beispiel
prices = get_card_prices("Ragavan, Nimble Pilferer")
print(f"USD: ${prices['usd']}")
print(f"EUR: €{prices['eur']}")
print(f"MTGO: {prices['tix']} tix")

# WICHTIG: Preise sind max. 24 Stunden gültig!
```

---

### 5. Bulk Data Download

```python
def download_bulk_data(bulk_type="default_cards"):
    """
    Lädt komplette Scryfall-Datenbank herunter.
    
    Args:
        bulk_type: 
            - "oracle_cards": Einzigartige Karten (Oracle IDs)
            - "unique_artwork": Einzigartige Artworks
            - "default_cards": Alle Karten (empfohlen)
            - "all_cards": Alle Karten inkl. Tokens
            - "rulings": Alle Rulings
    
    Returns:
        Liste aller Karten
    """
    # 1. Liste der verfügbaren Bulk-Dateien abrufen
    url = "https://api.scryfall.com/bulk-data"
    headers = {"User-Agent": "MTGApp/1.0"}
    response = requests.get(url, headers=headers)
    bulk_data_list = response.json()["data"]
    
    # 2. Gewünschte Bulk-Datei finden
    bulk_file = next(
        (item for item in bulk_data_list if item["type"] == bulk_type),
        None
    )
    
    if not bulk_file:
        raise ValueError(f"Bulk type '{bulk_type}' not found")
    
    # 3. Bulk-Datei herunterladen (kann groß sein!)
    download_url = bulk_file["download_uri"]
    print(f"Downloading {bulk_file['size'] / 1024 / 1024:.2f} MB...")
    
    response = requests.get(download_url)
    cards = response.json()
    
    print(f"Downloaded {len(cards)} cards")
    return cards


# Verwendung (Vorsicht: ~100MB+ Download!)
# all_cards = download_bulk_data("default_cards")

# Für lokale Datenbank empfohlen:
# 1. Einmal täglich bulk data downloaden
# 2. In lokaler Datenbank speichern
# 3. Für Abfragen lokale DB verwenden
```

---

### 6. Set-Informationen

```python
def get_all_sets():
    """Ruft alle MTG Sets ab."""
    url = "https://api.scryfall.com/sets"
    headers = {"User-Agent": "MTGApp/1.0"}
    response = requests.get(url, headers=headers)
    return response.json()["data"]


def get_set_by_code(set_code):
    """Ruft spezifisches Set nach Code ab (z.B. 'neo', 'mid')."""
    url = f"https://api.scryfall.com/sets/{set_code}"
    headers = {"User-Agent": "MTGApp/1.0"}
    response = requests.get(url, headers=headers)
    return response.json()


# Beispiel: Neueste Sets
sets = get_all_sets()
latest_sets = sorted(sets, key=lambda x: x["released_at"], reverse=True)[:5]

for s in latest_sets:
    print(f"{s['name']} ({s['code']}) - {s['released_at']}")
    print(f"  Cards: {s['card_count']}")
```

---

### 7. Autocomplete für Kartennamen

```python
def autocomplete_card_name(partial_name):
    """
    Gibt Kartenname-Vorschläge für teilweise Eingabe.
    
    Args:
        partial_name: Teilweise eingegebener Kartenname (min. 2 Zeichen)
    
    Returns:
        Liste von bis zu 20 Kartenname-Vorschlägen
    """
    url = "https://api.scryfall.com/cards/autocomplete"
    params = {"q": partial_name}
    headers = {"User-Agent": "MTGApp/1.0"}
    
    response = requests.get(url, params=params, headers=headers)
    return response.json()["data"]


# Beispiel für Autocomplete-UI
suggestions = autocomplete_card_name("light")
print("Suggestions:", suggestions[:10])
# Output: ['Light Up the Night', 'Lightning Bolt', 'Lightning Helix', ...]
```

---

### 8. Zufällige Karte

```python
def get_random_card(query=None):
    """
    Ruft zufällige Karte ab, optional mit Filter.
    
    Args:
        query: Optional Scryfall-Query für Filter (z.B. "c:red t:creature")
    """
    url = "https://api.scryfall.com/cards/random"
    params = {"q": query} if query else {}
    headers = {"User-Agent": "MTGApp/1.0"}
    
    response = requests.get(url, params=params, headers=headers)
    return response.json()


# Beispiele
random_card = get_random_card()
random_red_creature = get_random_card("c:red t:creature")
```

---

## magicthegathering.io API

### Base Information

```python
BASE_URL = "https://api.magicthegathering.io/v1"
RATE_LIMIT = 5000  # requests per hour
MAX_PAGE_SIZE = 100
```

### 🎯 Anwendungsfälle

1. **Standard-Kartensuche mit einfachen Filtern**
2. **SDK-basierte Entwicklung (Python, Ruby, JS, etc.)**
3. **Booster-Pack Simulation**
4. **Set-Informationen**
5. **Type/Subtype/Supertype Listen**

---

### 1. Kartensuche mit Filtern

```python
def search_mtgio_cards(filters=None, page=1, page_size=100):
    """
    Sucht Karten auf magicthegathering.io.
    
    Args:
        filters: Dict mit Filterparametern
        page: Seitennummer (default: 1)
        page_size: Anzahl Ergebnisse pro Seite (max: 100)
    
    Returns:
        Dict mit 'cards' und 'headers' (für Pagination)
    """
    url = f"{BASE_URL}/cards"
    params = filters or {}
    params.update({"page": page, "pageSize": page_size})
    
    response = requests.get(url, params=params)
    response.raise_for_status()
    
    return {
        "cards": response.json().get("cards", []),
        "headers": {
            "total_count": response.headers.get("Total-Count"),
            "page_size": response.headers.get("Page-Size"),
            "ratelimit_remaining": response.headers.get("Ratelimit-Remaining")
        }
    }


# Verfügbare Filter
available_filters = {
    # Einfache Felder (OR-Logik mit |)
    "name": "Lightning Bolt",
    "rarity": "rare|mythic",  # Rare ODER Mythic
    "set": "neo",
    "artist": "John Avon",
    
    # Multi-Value Felder (AND mit , / OR mit |)
    "colors": "red,white",  # Rot UND Weiß
    "types": "creature",
    "subtypes": "goblin|elf",  # Goblin ODER Elf
    
    # Numerische Felder
    "cmc": "3",
    "power": "4",
    "toughness": "4",
    
    # Text-Suche
    "text": "draw a card",
    
    # Format & Legalität
    "gameFormat": "commander",
    "legality": "legal",
    
    # Sonstiges
    "language": "German",
    "orderBy": "name"  # Sortierung
}

# Beispiele
result = search_mtgio_cards({"colors": "red,white", "types": "creature"})
print(f"Found {len(result['cards'])} cards")
print(f"Total in DB: {result['headers']['total_count']}")

for card in result['cards'][:5]:
    print(f"- {card['name']} ({card['manaCost']})")
```

---

### 2. Einzelne Karte nach ID/Multiverseid

```python
def get_card_by_id(card_id):
    """Ruft Karte nach ID oder Multiverseid ab."""
    url = f"{BASE_URL}/cards/{card_id}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()["card"]


# Beispiel
card = get_card_by_id(386616)  # Narset, Enlightened Master
print(f"{card['name']} - {card['type']}")
```

---

### 3. Suche nach ausländischen Kartennamen

```python
def search_by_foreign_name(foreign_name, language):
    """
    Sucht Karten nach ausländischem Namen.
    
    Args:
        foreign_name: Name in der Fremdsprache
        language: "Spanish", "German", "French", "Italian", "Japanese", etc.
    """
    filters = {
        "name": foreign_name,
        "language": language
    }
    result = search_mtgio_cards(filters)
    return result["cards"]


# Beispiel
spanish_cards = search_by_foreign_name("Arcángel Avacyn", "Spanish")
```

---

### 4. Booster-Pack Generierung

```python
def generate_booster_pack(set_code):
    """
    Generiert ein zufälliges Booster-Pack für ein Set.
    
    Args:
        set_code: Set-Code (z.B. 'ktk', 'neo', 'mid')
    
    Returns:
        Liste von Karten wie in echtem Booster
    """
    url = f"{BASE_URL}/sets/{set_code}/booster"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()["cards"]


# Beispiel: Draft-Simulator
set_code = "neo"  # Kamigawa: Neon Dynasty
pack1 = generate_booster_pack(set_code)
pack2 = generate_booster_pack(set_code)
pack3 = generate_booster_pack(set_code)

print(f"Pack 1: {len(pack1)} cards")
for card in pack1:
    print(f"  {card['rarity']}: {card['name']}")
```

---

### 5. Set-Informationen

```python
def get_all_sets_mtgio():
    """Ruft alle Sets ab."""
    url = f"{BASE_URL}/sets"
    response = requests.get(url)
    return response.json()["sets"]


def get_set_by_code_mtgio(set_code):
    """Ruft spezifisches Set ab."""
    url = f"{BASE_URL}/sets/{set_code}"
    response = requests.get(url)
    return response.json()["set"]


# Beispiel: Sets eines Blocks
all_sets = get_all_sets_mtgio()
khans_block = [s for s in all_sets if s.get("block") == "Khans of Tarkir"]

for s in khans_block:
    print(f"{s['name']} ({s['code']}) - {s['releaseDate']}")
```

---

### 6. Types, Subtypes, Supertypes

```python
def get_all_types():
    """Alle Kartentypen."""
    url = f"{BASE_URL}/types"
    response = requests.get(url)
    return response.json()["types"]


def get_all_subtypes():
    """Alle Subtypes."""
    url = f"{BASE_URL}/subtypes"
    response = requests.get(url)
    return response.json()["subtypes"]


def get_all_supertypes():
    """Alle Supertypes."""
    url = f"{BASE_URL}/supertypes"
    response = requests.get(url)
    return response.json()["supertypes"]


def get_all_formats():
    """Alle Spielformate."""
    url = f"{BASE_URL}/formats"
    response = requests.get(url)
    return response.json()["formats"]


# Beispiel: Validierung
valid_types = get_all_types()
valid_formats = get_all_formats()

print("Valid Types:", valid_types)
print("Valid Formats:", valid_formats)
```

---

### 7. Python SDK Verwendung

```python
# Installation: pip install mtgsdk

from mtgsdk import Card, Set

# Kartensuche mit SDK
cards = Card.where(supertypes='legendary') \
            .where(types='creature') \
            .where(colors='red,white') \
            .all()

for card in cards[:5]:
    print(f"{card.name} - {card.mana_cost}")

# Set-Informationen
khans = Set.find('ktk')
print(f"{khans.name} released on {khans.release_date}")

# Pagination
page_1 = Card.where(page=1, pageSize=50).all()
page_2 = Card.where(page=2, pageSize=50).all()
```

---

## Moxfield API (inoffiziell)

### ⚠️ WARNUNG
Diese API ist **nicht offiziell dokumentiert** und kann sich jederzeit ändern. Für Produktions-Anwendungen mit Vorsicht verwenden.

### Base Information

```python
BASE_URL = "https://api2.moxfield.com"
# Rate Limits: Unbekannt (vorsichtig verwenden!)
```

### 🎯 Anwendungsfälle

1. **Abrufen von Moxfield-Decks**
2. **Kartensuche auf Moxfield**
3. **Deck-Preise**

---

### 1. Deck abrufen

```python
def get_moxfield_deck(deck_id):
    """
    Ruft ein Moxfield-Deck ab.
    
    Args:
        deck_id: Moxfield Deck-ID (aus URL: moxfield.com/decks/DECK_ID)
    
    Returns:
        Deck-Daten mit Kartenliste
    """
    url = f"{BASE_URL}/v2/decks/all/{deck_id}"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json"
    }
    
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()


# Beispiel
deck_id = "oEWXWHM5eEGMmopExLWRCA"
deck = get_moxfield_deck(deck_id)

print(f"Deck Name: {deck['name']}")
print(f"Format: {deck['format']}")
print(f"Commander: {deck.get('commanders', [])}")
print(f"\nMainboard ({len(deck['mainboard'])} cards):")

for card_id, card_info in list(deck['mainboard'].items())[:10]:
    print(f"  {card_info['quantity']}x {card_info['card']['name']}")
```

---

### 2. Kartensuche auf Moxfield

```python
def search_moxfield_cards(query, page=0, page_size=20):
    """
    Sucht Karten auf Moxfield.
    
    Args:
        query: Suchbegriff (Kartenname)
        page: Seitennummer (0-basiert)
        page_size: Anzahl Ergebnisse
    """
    url = f"{BASE_URL}/v2/cards/search"
    params = {
        "q": query,
        "page": page,
        "pageSize": page_size
    }
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json"
    }
    
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    return response.json()


# Beispiel
results = search_moxfield_cards("Lightning Bolt")
for card in results.get("data", [])[:5]:
    print(f"{card['name']} - {card.get('set', 'N/A')}")
```

---

### 3. JavaScript/TypeScript SDK

```javascript
// Installation: npm install moxfield-api

import MoxfieldApi from 'moxfield-api';

const moxfield = new MoxfieldApi();

// Deck abrufen
const deckId = 'oEWXWHM5eEGMmopExLWRCA';
const deck = await moxfield.decklist.findById(deckId);

console.log(`Deck: ${deck.name}`);
console.log(`Format: ${deck.format}`);
console.log(`Cards: ${deck.mainboard.length}`);

// Karten durchgehen
deck.mainboard.forEach(card => {
    console.log(`${card.quantity}x ${card.card.name}`);
});
```

---

## Best Practices

### 1. Rate Limiting

```python
import time
from functools import wraps

def rate_limit(min_interval=0.1):
    """Decorator für Rate Limiting."""
    def decorator(func):
        last_called = [0.0]
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            elapsed = time.time() - last_called[0]
            wait_time = min_interval - elapsed
            if wait_time > 0:
                time.sleep(wait_time)
            result = func(*args, **kwargs)
            last_called[0] = time.time()
            return result
        return wrapper
    return decorator


# Verwendung
@rate_limit(0.1)  # Max 10 requests/sec
def get_card(card_name):
    return get_card_by_name(card_name)
```

---

### 2. Caching

```python
from functools import lru_cache
import json

@lru_cache(maxsize=1000)
def cached_card_search(card_name):
    """Cached version of card search."""
    return get_card_by_name(card_name)


# Oder: Persistent Cache mit Datei
class CardCache:
    def __init__(self, cache_file="card_cache.json"):
        self.cache_file = cache_file
        self.cache = self._load_cache()
    
    def _load_cache(self):
        try:
            with open(self.cache_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
    
    def _save_cache(self):
        with open(self.cache_file, 'w') as f:
            json.dump(self.cache, f)
    
    def get_card(self, card_name):
        if card_name in self.cache:
            return self.cache[card_name]
        
        card = get_card_by_name(card_name)
        self.cache[card_name] = card
        self._save_cache()
        return card


# Verwendung
cache = CardCache()
card = cache.get_card("Lightning Bolt")
```

---

### 3. Bulk Data für lokale DB

```python
import sqlite3
import json

def create_card_database():
    """Erstellt lokale SQLite-Datenbank mit Scryfall Bulk Data."""
    
    # 1. Bulk Data herunterladen
    print("Downloading bulk data...")
    cards = download_bulk_data("default_cards")
    
    # 2. SQLite-Datenbank erstellen
    conn = sqlite3.connect('mtg_cards.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cards (
            id TEXT PRIMARY KEY,
            name TEXT,
            mana_cost TEXT,
            cmc REAL,
            type_line TEXT,
            oracle_text TEXT,
            colors TEXT,
            set_code TEXT,
            rarity TEXT,
            usd_price REAL,
            eur_price REAL,
            image_url TEXT,
            data JSON
        )
    ''')
    
    # 3. Karten einfügen
    print(f"Inserting {len(cards)} cards...")
    for card in cards:
        cursor.execute('''
            INSERT OR REPLACE INTO cards VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            card['id'],
            card['name'],
            card.get('mana_cost', ''),
            card.get('cmc', 0),
            card.get('type_line', ''),
            card.get('oracle_text', ''),
            ','.join(card.get('colors', [])),
            card.get('set', ''),
            card.get('rarity', ''),
            float(card['prices'].get('usd') or 0),
            float(card['prices'].get('eur') or 0),
            card.get('image_uris', {}).get('normal', ''),
            json.dumps(card)
        ))
    
    conn.commit()
    conn.close()
    print("Database created successfully!")


def search_local_cards(name_query):
    """Sucht Karten in lokaler Datenbank."""
    conn = sqlite3.connect('mtg_cards.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT name, mana_cost, type_line, oracle_text
        FROM cards
        WHERE name LIKE ?
        ORDER BY name
    ''', (f'%{name_query}%',))
    
    results = cursor.fetchall()
    conn.close()
    return results
```

---

### 4. Error Handling

```python
from requests.exceptions import RequestException, HTTPError
import time

def robust_api_call(func, max_retries=3, backoff=2):
    """Robuster API-Call mit Retry-Logik."""
    for attempt in range(max_retries):
        try:
            return func()
        except HTTPError as e:
            if e.response.status_code == 429:  # Rate limit
                wait_time = backoff ** attempt
                print(f"Rate limited. Waiting {wait_time}s...")
                time.sleep(wait_time)
            elif e.response.status_code == 404:
                raise ValueError("Card not found")
            elif 500 <= e.response.status_code < 600:
                if attempt < max_retries - 1:
                    time.sleep(backoff ** attempt)
                else:
                    raise
            else:
                raise
        except RequestException as e:
            if attempt < max_retries - 1:
                time.sleep(backoff ** attempt)
            else:
                raise
    
    raise Exception("Max retries exceeded")


# Verwendung
def search_safely(card_name):
    return robust_api_call(
        lambda: get_card_by_name(card_name),
        max_retries=3
    )
```

---

## Fehlerbehandlung

### Scryfall API Errors

```python
def handle_scryfall_error(response):
    """Behandelt Scryfall-spezifische Fehler."""
    if response.status_code == 404:
        error = response.json()
        return {
            "error": "Not Found",
            "details": error.get("details", "Card not found")
        }
    elif response.status_code == 429:
        return {
            "error": "Rate Limit",
            "details": "Too many requests. Wait before retrying."
        }
    else:
        response.raise_for_status()
```

### magicthegathering.io API Errors

```python
def handle_mtgio_error(response):
    """Behandelt mtgio-spezifische Fehler."""
    error_codes = {
        400: "Bad Request - Invalid parameters",
        403: "Forbidden - Rate limit exceeded (5000/hour)",
        404: "Not Found - Resource doesn't exist",
        500: "Internal Server Error",
        503: "Service Unavailable - Maintenance"
    }
    
    if response.status_code in error_codes:
        return {
            "error": error_codes[response.status_code],
            "status_code": response.status_code
        }
    response.raise_for_status()
```

---

## Komplettes Beispielprojekt: Deck Price Checker

```python
import requests
import time

class MTGDeckPriceChecker:
    """Überprüft Preise für MTG-Decks."""
    
    def __init__(self):
        self.scryfall_base = "https://api.scryfall.com"
        self.headers = {"User-Agent": "DeckPriceChecker/1.0"}
    
    def parse_decklist(self, decklist_text):
        """
        Parst Deckliste im Format:
        4 Lightning Bolt
        2 Snapcaster Mage
        1 Jace, the Mind Sculptor
        """
        cards = []
        for line in decklist_text.strip().split('\n'):
            if line.strip():
                parts = line.strip().split(' ', 1)
                if len(parts) == 2:
                    quantity = int(parts[0])
                    card_name = parts[1]
                    cards.append({"name": card_name, "quantity": quantity})
        return cards
    
    def get_card_price(self, card_name):
        """Ruft Preis für einzelne Karte ab."""
        url = f"{self.scryfall_base}/cards/named"
        params = {"fuzzy": card_name}
        
        response = requests.get(url, params=params, headers=self.headers)
        response.raise_for_status()
        card = response.json()
        
        prices = card.get("prices", {})
        return {
            "name": card["name"],
            "usd": float(prices.get("usd") or 0),
            "eur": float(prices.get("eur") or 0),
            "image": card.get("image_uris", {}).get("small", "")
        }
    
    def calculate_deck_price(self, decklist_text, currency="usd"):
        """Berechnet Gesamtpreis eines Decks."""
        cards = self.parse_decklist(decklist_text)
        total_price = 0
        card_prices = []
        
        for card_info in cards:
            try:
                price_info = self.get_card_price(card_info["name"])
                card_price = price_info[currency] * card_info["quantity"]
                total_price += card_price
                
                card_prices.append({
                    **price_info,
                    "quantity": card_info["quantity"],
                    "total": card_price
                })
                
                time.sleep(0.1)  # Rate limiting
                
            except Exception as e:
                print(f"Error fetching {card_info['name']}: {e}")
        
        return {
            "cards": card_prices,
            "total": total_price,
            "currency": currency.upper()
        }
    
    def print_deck_report(self, deck_result):
        """Gibt übersichtlichen Bericht aus."""
        print(f"\n{'='*60}")
        print(f"DECK PRICE REPORT ({deck_result['currency']})")
        print(f"{'='*60}\n")
        
        for card in sorted(deck_result['cards'], key=lambda x: x['total'], reverse=True):
            symbol = "$" if deck_result['currency'] == "USD" else "€"
            print(f"{card['quantity']}x {card['name']:<40} {symbol}{card['total']:.2f}")
        
        print(f"\n{'-'*60}")
        print(f"TOTAL: {symbol}{deck_result['total']:.2f}")
        print(f"{'='*60}\n")


# Verwendung
checker = MTGDeckPriceChecker()

decklist = """
4 Lightning Bolt
4 Snapcaster Mage
2 Jace, the Mind Sculptor
4 Scalding Tarn
4 Misty Rainforest
20 Island
10 Mountain
"""

result = checker.calculate_deck_price(decklist, currency="usd")
checker.print_deck_report(result)
```

---

## Quick Reference: API-Entscheidungsmatrix

```python
def choose_api_for_task(task_description):
    """
    Hilft bei der Auswahl der richtigen API basierend auf der Aufgabe.
    
    Returns:
        Empfohlene API und Begründung
    """
    
    task_lower = task_description.lower()
    
    # Moxfield-spezifisch
    if "moxfield" in task_lower or "deck import" in task_lower:
        return {
            "api": "Moxfield API (inoffiziell)",
            "reason": "Einzige Option für Moxfield-Decks",
            "caution": "Inoffizielle API - kann sich ändern"
        }
    
    # Bulk Download
    if "bulk" in task_lower or "download all" in task_lower or "database" in task_lower:
        return {
            "api": "Scryfall API",
            "endpoint": "/bulk-data",
            "reason": "Optimiert für Massen-Downloads"
        }
    
    # Preise
    if "price" in task_lower or "cost" in task_lower or "value" in task_lower:
        return {
            "api": "Scryfall API",
            "reason": "Umfassende Preisdaten (TCGPlayer, Cardmarket, etc.)"
        }
    
    # Bilder
    if "image" in task_lower or "picture" in task_lower or "art" in task_lower:
        return {
            "api": "Scryfall API",
            "reason": "Hochauflösende Bilder in verschiedenen Formaten"
        }
    
    # Booster Simulation
    if "booster" in task_lower or "draft" in task_lower or "pack" in task_lower:
        return {
            "api": "magicthegathering.io API",
            "endpoint": "/sets/:id/booster",
            "reason": "Einzige API mit Booster-Pack Generierung"
        }
    
    # SDK-Entwicklung
    if "sdk" in task_lower or any(lang in task_lower for lang in ["python", "ruby", "java", "php"]):
        return {
            "api": "magicthegathering.io API",
            "reason": "Offizielle SDKs für viele Sprachen verfügbar"
        }
    
    # Standard-Suche
    return {
        "api": "Scryfall API",
        "reason": "Beste Performance und mächtigste Suchsyntax",
        "alternative": "magicthegathering.io für SDK-Entwicklung"
    }


# Beispiele
print(choose_api_for_task("Find all red creatures with power 5"))
print(choose_api_for_task("Download entire card database"))
print(choose_api_for_task("Get current price of card"))
print(choose_api_for_task("Simulate opening a booster pack"))
print(choose_api_for_task("Import deck from Moxfield"))
```

---

## Zusammenfassung für AI Copilots

### Wann welche API?

1. **Scryfall API** → Default für:
   - Kartensuche (erweitert)
   - Preisabfragen
   - Bilder
   - Bulk Downloads
   - Moderne Features

2. **magicthegathering.io API** → Verwenden für:
   - SDK-basierte Entwicklung
   - Booster-Pack Simulation
   - Einfache Suchen mit SDKs
   - Legacy-Projekte

3. **Moxfield API** → Nur für:
   - Moxfield-Deck Import/Export
   - Moxfield-spezifische Features
   - ⚠️ Mit Vorsicht (inoffiziell)

### Rate Limits beachten!
- Scryfall: 10 req/sec → 100ms delay
- mtgio: 5000 req/hour → ~1.4 req/sec
- Moxfield: Unbekannt → konservativ sein

### Best Practices:
1. ✅ Immer User-Agent setzen
2. ✅ Rate Limiting implementieren
3. ✅ Caching verwenden
4. ✅ Error Handling mit Retries
5. ✅ Für Produktions-Apps: Bulk Data → lokale DB

---

**Letzte Aktualisierung**: November 2025  
**Version**: 1.0  
**Autor**: AI Assistant für Lester
