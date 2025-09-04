#!/usr/bin/env python3
"""
Sample audio file generator for testing the audio test script.
Creates dummy MP3 files for demonstration purposes.
"""

import os
import subprocess
import sys
from pathlib import Path

def create_sample_audio_file(romaji: str, character: str):
    """Create a sample MP3 file using text-to-speech (macOS only for demo)"""
    audio_dir = Path("static/audio")
    audio_dir.mkdir(parents=True, exist_ok=True)
    
    output_path = audio_dir / f"{romaji}.mp3"
    
    if sys.platform == "darwin":  # macOS
        try:
            # Use macOS built-in text-to-speech to create audio file
            # First create a temporary wave file
            temp_path = audio_dir / f"{romaji}_temp.aiff"
            
            # Create speech file (Japanese pronunciation would be better but this is for demo)
            subprocess.run([
                "say", "-v", "Kyoko", "-o", str(temp_path), romaji
            ], check=True, capture_output=True)
            
            # Convert to MP3 if ffmpeg is available
            try:
                subprocess.run([
                    "ffmpeg", "-i", str(temp_path), "-codec:a", "libmp3lame", 
                    "-b:a", "128k", str(output_path), "-y"
                ], check=True, capture_output=True)
                
                # Remove temporary file
                temp_path.unlink()
                return True, "Created with say + ffmpeg"
                
            except (subprocess.CalledProcessError, FileNotFoundError):
                # If ffmpeg not available, just rename the AIFF file
                temp_path.rename(output_path.with_suffix('.aiff'))
                return True, "Created with say (AIFF format)"
                
        except subprocess.CalledProcessError as e:
            return False, f"Failed to create audio: {e}"
        except Exception as e:
            return False, f"Unexpected error: {e}"
    else:
        # For other platforms, create a small dummy MP3 file
        try:
            # Create a minimal MP3 header (this won't actually play, just for testing file existence)
            dummy_mp3_header = b'\xff\xfb\x90\x00' + b'\x00' * 100
            with open(output_path, 'wb') as f:
                f.write(dummy_mp3_header)
            return True, "Created dummy MP3 file"
        except Exception as e:
            return False, f"Failed to create dummy file: {e}"

def main():
    """Create sample audio files for first few characters"""
    print("🎵 Creating sample audio files for testing...")
    
    # Create sample files for the first 5 vowels
    test_characters = [
        ("a", "あ"),
        ("i", "い"), 
        ("u", "う"),
        ("ka", "か"),
        ("sa", "さ")
    ]
    
    success_count = 0
    for romaji, char in test_characters:
        success, message = create_sample_audio_file(romaji, char)
        status = "✅" if success else "❌"
        print(f"  {char} ({romaji}): {status} {message}")
        if success:
            success_count += 1
    
    print(f"\n📊 Created {success_count}/{len(test_characters)} sample audio files")
    print("🧪 Run 'python3 test_audio.py' to test the audio files!")

if __name__ == "__main__":
    main()