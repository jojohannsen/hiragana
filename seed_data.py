#!/usr/bin/env python3
"""
Database initialization script for Hiragana flashcard application.
Run this script to populate the database with all basic Hiragana characters.
"""

import sqlite3
import os

# Comprehensive Hiragana data with all 46 basic characters
HIRAGANA_DATA = [
    # Vowels (a, i, u, e, o)
    {'character': 'あ', 'romaji': 'a', 'pronunciation': 'ah', 'category': 'vowels', 'order_index': 0},
    {'character': 'い', 'romaji': 'i', 'pronunciation': 'ee', 'category': 'vowels', 'order_index': 1},
    {'character': 'う', 'romaji': 'u', 'pronunciation': 'oo', 'category': 'vowels', 'order_index': 2},
    {'character': 'え', 'romaji': 'e', 'pronunciation': 'eh', 'category': 'vowels', 'order_index': 3},
    {'character': 'お', 'romaji': 'o', 'pronunciation': 'oh', 'category': 'vowels', 'order_index': 4},
    
    # Ka row (ka, ki, ku, ke, ko)
    {'character': 'か', 'romaji': 'ka', 'pronunciation': 'kah', 'category': 'ka-row', 'order_index': 5},
    {'character': 'き', 'romaji': 'ki', 'pronunciation': 'kee', 'category': 'ka-row', 'order_index': 6},
    {'character': 'く', 'romaji': 'ku', 'pronunciation': 'koo', 'category': 'ka-row', 'order_index': 7},
    {'character': 'け', 'romaji': 'ke', 'pronunciation': 'keh', 'category': 'ka-row', 'order_index': 8},
    {'character': 'こ', 'romaji': 'ko', 'pronunciation': 'koh', 'category': 'ka-row', 'order_index': 9},
    
    # Sa row (sa, shi, su, se, so)
    {'character': 'さ', 'romaji': 'sa', 'pronunciation': 'sah', 'category': 'sa-row', 'order_index': 10},
    {'character': 'し', 'romaji': 'shi', 'pronunciation': 'shee', 'category': 'sa-row', 'order_index': 11},
    {'character': 'す', 'romaji': 'su', 'pronunciation': 'soo', 'category': 'sa-row', 'order_index': 12},
    {'character': 'せ', 'romaji': 'se', 'pronunciation': 'seh', 'category': 'sa-row', 'order_index': 13},
    {'character': 'そ', 'romaji': 'so', 'pronunciation': 'soh', 'category': 'sa-row', 'order_index': 14},
    
    # Ta row (ta, chi, tsu, te, to)
    {'character': 'た', 'romaji': 'ta', 'pronunciation': 'tah', 'category': 'ta-row', 'order_index': 15},
    {'character': 'ち', 'romaji': 'chi', 'pronunciation': 'chee', 'category': 'ta-row', 'order_index': 16},
    {'character': 'つ', 'romaji': 'tsu', 'pronunciation': 'tsoo', 'category': 'ta-row', 'order_index': 17},
    {'character': 'て', 'romaji': 'te', 'pronunciation': 'teh', 'category': 'ta-row', 'order_index': 18},
    {'character': 'と', 'romaji': 'to', 'pronunciation': 'toh', 'category': 'ta-row', 'order_index': 19},
    
    # Na row (na, ni, nu, ne, no)
    {'character': 'な', 'romaji': 'na', 'pronunciation': 'nah', 'category': 'na-row', 'order_index': 20},
    {'character': 'に', 'romaji': 'ni', 'pronunciation': 'nee', 'category': 'na-row', 'order_index': 21},
    {'character': 'ぬ', 'romaji': 'nu', 'pronunciation': 'noo', 'category': 'na-row', 'order_index': 22},
    {'character': 'ね', 'romaji': 'ne', 'pronunciation': 'neh', 'category': 'na-row', 'order_index': 23},
    {'character': 'の', 'romaji': 'no', 'pronunciation': 'noh', 'category': 'na-row', 'order_index': 24},
    
    # Ha row (ha, hi, fu, he, ho)
    {'character': 'は', 'romaji': 'ha', 'pronunciation': 'hah', 'category': 'ha-row', 'order_index': 25},
    {'character': 'ひ', 'romaji': 'hi', 'pronunciation': 'hee', 'category': 'ha-row', 'order_index': 26},
    {'character': 'ふ', 'romaji': 'fu', 'pronunciation': 'foo', 'category': 'ha-row', 'order_index': 27},
    {'character': 'へ', 'romaji': 'he', 'pronunciation': 'heh', 'category': 'ha-row', 'order_index': 28},
    {'character': 'ほ', 'romaji': 'ho', 'pronunciation': 'hoh', 'category': 'ha-row', 'order_index': 29},
    
    # Ma row (ma, mi, mu, me, mo)
    {'character': 'ま', 'romaji': 'ma', 'pronunciation': 'mah', 'category': 'ma-row', 'order_index': 30},
    {'character': 'み', 'romaji': 'mi', 'pronunciation': 'mee', 'category': 'ma-row', 'order_index': 31},
    {'character': 'む', 'romaji': 'mu', 'pronunciation': 'moo', 'category': 'ma-row', 'order_index': 32},
    {'character': 'め', 'romaji': 'me', 'pronunciation': 'meh', 'category': 'ma-row', 'order_index': 33},
    {'character': 'も', 'romaji': 'mo', 'pronunciation': 'moh', 'category': 'ma-row', 'order_index': 34},
    
    # Ya row (ya, yu, yo) - note: no yi or ye in modern Japanese
    {'character': 'や', 'romaji': 'ya', 'pronunciation': 'yah', 'category': 'ya-row', 'order_index': 35},
    {'character': 'ゆ', 'romaji': 'yu', 'pronunciation': 'yoo', 'category': 'ya-row', 'order_index': 36},
    {'character': 'よ', 'romaji': 'yo', 'pronunciation': 'yoh', 'category': 'ya-row', 'order_index': 37},
    
    # Ra row (ra, ri, ru, re, ro)
    {'character': 'ら', 'romaji': 'ra', 'pronunciation': 'rah', 'category': 'ra-row', 'order_index': 38},
    {'character': 'り', 'romaji': 'ri', 'pronunciation': 'ree', 'category': 'ra-row', 'order_index': 39},
    {'character': 'る', 'romaji': 'ru', 'pronunciation': 'roo', 'category': 'ra-row', 'order_index': 40},
    {'character': 'れ', 'romaji': 're', 'pronunciation': 'reh', 'category': 'ra-row', 'order_index': 41},
    {'character': 'ろ', 'romaji': 'ro', 'pronunciation': 'roh', 'category': 'ra-row', 'order_index': 42},
    
    # Wa row (wa, wo) - note: modern wi and we are obsolete
    {'character': 'わ', 'romaji': 'wa', 'pronunciation': 'wah', 'category': 'wa-row', 'order_index': 43},
    {'character': 'を', 'romaji': 'wo', 'pronunciation': 'woh', 'category': 'wa-row', 'order_index': 44},
    
    # N (standalone n sound)
    {'character': 'ん', 'romaji': 'n', 'pronunciation': 'n', 'category': 'wa-row', 'order_index': 45},
]

def create_database():
    """Create the database and tables"""
    # Ensure data directory exists
    os.makedirs('data', exist_ok=True)
    
    # Connect to database (creates file if it doesn't exist)
    conn = sqlite3.connect('data/hiragana.db')
    cursor = conn.cursor()
    
    # Create the hiragana_characters table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS hiragana_characters (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            character TEXT NOT NULL UNIQUE,
            romaji TEXT NOT NULL,
            pronunciation TEXT NOT NULL,
            category TEXT DEFAULT 'basic',
            order_index INTEGER DEFAULT 0
        )
    ''')
    
    # Clear existing data (for fresh start)
    cursor.execute('DELETE FROM hiragana_characters')
    
    # Insert all hiragana data
    for char_data in HIRAGANA_DATA:
        cursor.execute('''
            INSERT INTO hiragana_characters 
            (character, romaji, pronunciation, category, order_index)
            VALUES (?, ?, ?, ?, ?)
        ''', (
            char_data['character'],
            char_data['romaji'], 
            char_data['pronunciation'],
            char_data['category'],
            char_data['order_index']
        ))
    
    # Commit changes and close
    conn.commit()
    conn.close()
    
    print(f"Database created successfully with {len(HIRAGANA_DATA)} characters!")
    print("Characters by category:")
    
    # Print summary by category
    categories = {}
    for char in HIRAGANA_DATA:
        cat = char['category']
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(char['character'])
    
    for category, chars in categories.items():
        print(f"  {category}: {''.join(chars)} ({len(chars)} characters)")

def verify_database():
    """Verify the database was created correctly"""
    if not os.path.exists('data/hiragana.db'):
        print("Database file not found!")
        return False
    
    conn = sqlite3.connect('data/hiragana.db')
    cursor = conn.cursor()
    
    # Check if table exists and has data
    cursor.execute("SELECT COUNT(*) FROM hiragana_characters")
    count = cursor.fetchone()[0]
    
    if count != len(HIRAGANA_DATA):
        print(f"Expected {len(HIRAGANA_DATA)} characters, found {count}")
        conn.close()
        return False
    
    # Sample a few characters
    cursor.execute("SELECT character, romaji, category FROM hiragana_characters LIMIT 5")
    sample = cursor.fetchall()
    print("\nSample characters:")
    for char, romaji, category in sample:
        print(f"  {char} ({romaji}) - {category}")
    
    conn.close()
    print(f"\nDatabase verification successful! {count} characters loaded.")
    return True

if __name__ == "__main__":
    print("Initializing Hiragana flashcard database...")
    create_database()
    verify_database()