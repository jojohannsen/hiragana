#!/usr/bin/env python3
"""
Quick test script to verify all audio files are accessible
"""

import os
import sqlite3

def test_audio_files():
    """Test that all expected audio files exist"""
    
    # Connect to database
    conn = sqlite3.connect('data/hiragana.db')
    cursor = conn.cursor()
    
    # Get all characters and their romaji
    cursor.execute("SELECT romaji FROM items ORDER BY order_index")
    characters = cursor.fetchall()
    conn.close()
    
    print("🎵 Testing Hiragana Audio Files")
    print("=" * 50)
    
    missing_files = []
    found_files = []
    
    for (romaji,) in characters:
        audio_file = f"static/audio/{romaji}.mp3"
        if os.path.exists(audio_file):
            size = os.path.getsize(audio_file)
            found_files.append(f"✅ {romaji}.mp3 ({size:,} bytes)")
        else:
            missing_files.append(f"❌ {romaji}.mp3 (missing)")
    
    # Print results
    print(f"📊 Results: {len(found_files)} found, {len(missing_files)} missing")
    print()
    
    if found_files:
        print("Found files:")
        for file_info in found_files[:10]:  # Show first 10
            print(f"  {file_info}")
        if len(found_files) > 10:
            print(f"  ... and {len(found_files) - 10} more")
        print()
    
    if missing_files:
        print("Missing files:")
        for file_info in missing_files:
            print(f"  {file_info}")
        print()
    
    print(f"🎯 Total audio files available: {len(found_files)}/46")
    
    if len(found_files) == 46:
        print("🎉 All audio files are ready!")
        return True
    else:
        print(f"⚠️  {len(missing_files)} audio files are missing")
        return False

if __name__ == "__main__":
    test_audio_files()