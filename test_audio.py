#!/usr/bin/env python3
"""
<<<<<<< HEAD
Quick test script to verify all audio files are accessible
=======
Audio file test script for Hiragana flashcard application.
Tests existence and playability of audio files for all hiragana characters.
>>>>>>> origin/flashcards-for-hiragana
"""

import os
import sqlite3
<<<<<<< HEAD

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
=======
import subprocess
import sys
from pathlib import Path
from typing import List, Dict, Tuple

# Color codes for terminal output
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    END = '\033[0m'

def get_hiragana_characters() -> List[Dict]:
    """Get all hiragana characters from database"""
    if not os.path.exists('data/hiragana.db'):
        print(f"{Colors.RED}❌ Database not found: data/hiragana.db{Colors.END}")
        return []
    
    try:
        conn = sqlite3.connect('data/hiragana.db')
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT id, character, romaji, pronunciation, category, order_index 
            FROM hiragana_characters 
            ORDER BY order_index
        """)
        
        characters = []
        for row in cursor.fetchall():
            characters.append({
                'id': row[0],
                'character': row[1],
                'romaji': row[2],
                'pronunciation': row[3],
                'category': row[4],
                'order_index': row[5]
            })
        
        conn.close()
        return characters
        
    except Exception as e:
        print(f"{Colors.RED}❌ Database error: {e}{Colors.END}")
        return []

def check_audio_file_exists(romaji: str) -> bool:
    """Check if audio file exists for given romaji"""
    audio_path = Path(f"static/audio/{romaji}.mp3")
    return audio_path.exists()

def test_audio_playback(romaji: str) -> Tuple[bool, str]:
    """Test if audio file can be played (requires system audio tools)"""
    audio_path = Path(f"static/audio/{romaji}.mp3")
    
    if not audio_path.exists():
        return False, "File not found"
    
    try:
        # Try different audio players based on OS
        if sys.platform == "darwin":  # macOS
            result = subprocess.run(
                ["afplay", str(audio_path)], 
                capture_output=True, 
                timeout=5,
                check=True
            )
            return True, "Playback successful (afplay)"
            
        elif sys.platform.startswith("linux"):  # Linux
            # Try multiple players
            for player in ["aplay", "paplay", "mpg123", "ffplay"]:
                try:
                    result = subprocess.run(
                        [player, str(audio_path)], 
                        capture_output=True, 
                        timeout=5,
                        check=True
                    )
                    return True, f"Playback successful ({player})"
                except (subprocess.CalledProcessError, FileNotFoundError):
                    continue
            return False, "No compatible audio player found"
            
        elif sys.platform == "win32":  # Windows
            # Use Windows Media Player command line
            try:
                result = subprocess.run(
                    ["powershell", "-c", f"(New-Object Media.SoundPlayer '{audio_path}').PlaySync()"],
                    capture_output=True,
                    timeout=5,
                    check=True
                )
                return True, "Playback successful (Windows Media)"
            except subprocess.CalledProcessError:
                return False, "Windows Media playback failed"
        else:
            return False, f"Unsupported OS: {sys.platform}"
            
    except subprocess.TimeoutExpired:
        return False, "Playback timeout"
    except subprocess.CalledProcessError as e:
        return False, f"Playback error: {e.returncode}"
    except FileNotFoundError:
        return False, "Audio player not found"
    except Exception as e:
        return False, f"Unexpected error: {str(e)}"

def create_missing_directories():
    """Create static/audio directory if it doesn't exist"""
    audio_dir = Path("static/audio")
    audio_dir.mkdir(parents=True, exist_ok=True)
    print(f"{Colors.BLUE}📁 Created/verified directory: {audio_dir}{Colors.END}")

def print_header():
    """Print test header"""
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*80}")
    print(f"🎵 HIRAGANA AUDIO FILE TEST SUITE")
    print(f"{'='*80}{Colors.END}")
    print(f"{Colors.WHITE}Testing audio file existence and playability for all hiragana characters{Colors.END}\n")

def print_category_header(category: str):
    """Print category header"""
    category_name = category.replace('-', ' ').title()
    print(f"\n{Colors.BOLD}{Colors.PURPLE}📚 {category_name}{Colors.END}")
    print(f"{Colors.PURPLE}{'-' * (len(category_name) + 4)}{Colors.END}")

def print_character_result(char_data: Dict, exists: bool, playback_result: Tuple[bool, str]):
    """Print result for a single character"""
    char = char_data['character']
    romaji = char_data['romaji']
    
    # Existence check
    exist_symbol = f"{Colors.GREEN}✅" if exists else f"{Colors.RED}❌"
    
    # Playback check
    playback_success, playback_msg = playback_result
    if not exists:
        playback_symbol = f"{Colors.YELLOW}⏸️"
        playback_status = "Skipped (file missing)"
    elif playback_success:
        playback_symbol = f"{Colors.GREEN}🔊"
        playback_status = playback_msg
    else:
        playback_symbol = f"{Colors.RED}🔇"
        playback_status = playback_msg
    
    print(f"  {char} ({romaji:>3}) │ File: {exist_symbol} │ Audio: {playback_symbol} │ {playback_status}{Colors.END}")

def print_summary(results: List[Dict]):
    """Print test summary"""
    total = len(results)
    files_exist = sum(1 for r in results if r['file_exists'])
    playback_success = sum(1 for r in results if r['playback_success'])
    
    print(f"\n{Colors.BOLD}{Colors.CYAN}📊 TEST SUMMARY{Colors.END}")
    print(f"{Colors.CYAN}{'='*50}{Colors.END}")
    print(f"{Colors.WHITE}Total characters tested: {Colors.BOLD}{total}{Colors.END}")
    print(f"{Colors.WHITE}Audio files found:      {Colors.GREEN if files_exist == total else Colors.YELLOW}{files_exist}/{total} ({files_exist/total*100:.1f}%){Colors.END}")
    print(f"{Colors.WHITE}Playback successful:    {Colors.GREEN if playback_success == total else Colors.YELLOW}{playback_success}/{total} ({playback_success/total*100:.1f}%){Colors.END}")
    
    if files_exist < total:
        missing = total - files_exist
        print(f"\n{Colors.YELLOW}⚠️  {missing} audio file(s) missing{Colors.END}")
    
    if playback_success < files_exist:
        failed = files_exist - playback_success
        print(f"{Colors.RED}🚨 {failed} audio file(s) failed playback test{Colors.END}")
    
    if files_exist == total and playback_success == total:
        print(f"\n{Colors.GREEN}{Colors.BOLD}🎉 ALL TESTS PASSED! All audio files exist and can be played.{Colors.END}")

def generate_missing_files_list(results: List[Dict]):
    """Generate list of missing audio files"""
    missing = [r for r in results if not r['file_exists']]
    if missing:
        print(f"\n{Colors.BOLD}{Colors.YELLOW}📋 MISSING AUDIO FILES{Colors.END}")
        print(f"{Colors.YELLOW}{'='*30}{Colors.END}")
        for result in missing:
            romaji = result['character_data']['romaji']
            char = result['character_data']['character']
            print(f"{Colors.YELLOW}  📄 static/audio/{romaji}.mp3 (for {char}){Colors.END}")

def main():
    """Main test function"""
    print_header()
    
    # Create directories if needed
    create_missing_directories()
    
    # Get all characters from database
    characters = get_hiragana_characters()
    if not characters:
        print(f"{Colors.RED}❌ No characters found in database{Colors.END}")
        sys.exit(1)
    
    print(f"{Colors.WHITE}Found {len(characters)} hiragana characters in database{Colors.END}")
    
    # Test each character's audio file
    results = []
    current_category = None
    
    for char_data in characters:
        # Print category header when category changes
        if char_data['category'] != current_category:
            current_category = char_data['category']
            print_category_header(current_category)
        
        # Check file existence
        exists = check_audio_file_exists(char_data['romaji'])
        
        # Test playback (only if file exists)
        if exists:
            playback_result = test_audio_playback(char_data['romaji'])
        else:
            playback_result = (False, "File not found")
        
        # Store result
        result = {
            'character_data': char_data,
            'file_exists': exists,
            'playback_success': playback_result[0],
            'playback_message': playback_result[1]
        }
        results.append(result)
        
        # Print individual result
        print_character_result(char_data, exists, playback_result)
    
    # Print summary
    print_summary(results)
    generate_missing_files_list(results)
    
    print(f"\n{Colors.CYAN}Test completed!{Colors.END}")
    
    # Return appropriate exit code
    all_exist = all(r['file_exists'] for r in results)
    all_playable = all(r['playback_success'] for r in results if r['file_exists'])
    
    if all_exist and all_playable:
        sys.exit(0)  # Success
    else:
        sys.exit(1)  # Some tests failed

if __name__ == "__main__":
    main()
>>>>>>> origin/flashcards-for-hiragana
