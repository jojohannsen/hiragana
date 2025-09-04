# Hiragana Audio Testing Suite

This directory contains comprehensive testing tools for verifying audio file functionality in the hiragana flashcard application.

## Files

- **`test_audio.py`** - Main test script that checks all hiragana characters
- **`create_sample_audio.py`** - Utility to create sample audio files for testing
- **`AUDIO_TEST_README.md`** - This documentation file

## Audio Test Script (`test_audio.py`)

### Purpose
Tests the existence and playability of audio files for all 46 hiragana characters in the database.

### Features
- ✅ **File Existence Check**: Verifies each expected audio file exists
- 🔊 **Playback Testing**: Actually attempts to play each audio file
- 📊 **Comprehensive Reporting**: Detailed results by character and category
- 🎨 **Color-coded Output**: Easy visual identification of issues
- 📋 **Missing Files List**: Complete list of missing audio files
- 🌍 **Cross-platform**: Supports macOS, Linux, and Windows

### Usage
```bash
# Make executable (first time only)
chmod +x test_audio.py

# Run the test
python3 test_audio.py
```

### Expected Audio File Format
- **Location**: `static/audio/{romaji}.mp3`
- **Format**: MP3 audio files
- **Naming**: Based on the romaji transliteration (e.g., `a.mp3`, `ka.mp3`, `shi.mp3`)

### Sample Output
```
🎵 HIRAGANA AUDIO FILE TEST SUITE
================================================================================
Testing audio file existence and playability for all hiragana characters

📚 Vowels
----------
  あ (  a) │ File: ✅ │ Audio: 🔊 │ Playback successful (afplay)
  い (  i) │ File: ❌ │ Audio: ⏸️ │ Skipped (file missing)
  う (  u) │ File: ✅ │ Audio: 🔇 │ Playback error: 1
```

### Exit Codes
- **0**: All tests passed (all files exist and can be played)
- **1**: Some tests failed (missing files or playback issues)

## Sample Audio Creator (`create_sample_audio.py`)

### Purpose
Creates sample audio files for testing purposes. Useful for development and demonstration.

### Features
- 🎯 **macOS Integration**: Uses built-in `say` command with Japanese voice
- 🔧 **FFmpeg Conversion**: Converts to MP3 format if FFmpeg is available
- 📝 **Cross-platform Fallback**: Creates dummy files on other platforms
- ⚡ **Quick Testing**: Creates files for first few characters only

### Usage
```bash
# Make executable (first time only)
chmod +x create_sample_audio.py

# Create sample files
python3 create_sample_audio.py
```

### macOS Requirements
- Built-in `say` command (standard on macOS)
- Optional: `ffmpeg` for MP3 conversion (install via Homebrew: `brew install ffmpeg`)
- Japanese voice "Kyoko" (usually available by default)

## Integration with Application

The audio files are served by the Flask application through the `/audio/{char_id}` endpoint:

```python
@rt("/audio/{char_id}")
def get(char_id: int):
    char = characters[char_id]
    audio_file = f"static/audio/{char.romaji}.mp3"
    if os.path.exists(audio_file):
        return FileResponse(audio_file, media_type="audio/mpeg")
    else:
        return Response(f"Audio for {char.character} ({char.romaji}) not available")
```

## Expected Audio Files List

The following 46 audio files should exist for complete functionality:

### Vowels (5 files)
- `a.mp3` (あ), `i.mp3` (い), `u.mp3` (う), `e.mp3` (え), `o.mp3` (お)

### Consonant Rows (41 files)
- **Ka-row**: `ka.mp3`, `ki.mp3`, `ku.mp3`, `ke.mp3`, `ko.mp3`
- **Sa-row**: `sa.mp3`, `shi.mp3`, `su.mp3`, `se.mp3`, `so.mp3`
- **Ta-row**: `ta.mp3`, `chi.mp3`, `tsu.mp3`, `te.mp3`, `to.mp3`
- **Na-row**: `na.mp3`, `ni.mp3`, `nu.mp3`, `ne.mp3`, `no.mp3`
- **Ha-row**: `ha.mp3`, `hi.mp3`, `fu.mp3`, `he.mp3`, `ho.mp3`
- **Ma-row**: `ma.mp3`, `mi.mp3`, `mu.mp3`, `me.mp3`, `mo.mp3`
- **Ya-row**: `ya.mp3`, `yu.mp3`, `yo.mp3`
- **Ra-row**: `ra.mp3`, `ri.mp3`, `ru.mp3`, `re.mp3`, `ro.mp3`
- **Wa-row**: `wa.mp3`, `wo.mp3`, `n.mp3`

## Troubleshooting

### Common Issues

1. **No audio player found**
   - **macOS**: Install XCode command line tools: `xcode-select --install`
   - **Linux**: Install audio player: `sudo apt install alsa-utils` or `sudo apt install pulseaudio-utils`
   - **Windows**: Usually works with built-in Windows Media Player

2. **Permission denied**
   - Make scripts executable: `chmod +x test_audio.py create_sample_audio.py`

3. **Database not found**
   - Run the database seeder: `python3 seed_data.py`
   - Ensure you're in the correct directory with `data/hiragana.db`

4. **FFmpeg not found (macOS)**
   - Install FFmpeg: `brew install ffmpeg`
   - Or run without FFmpeg (creates AIFF files instead)

### Testing Workflow

1. **Initial Setup**:
   ```bash
   python3 seed_data.py          # Ensure database exists
   python3 test_audio.py         # Check current state
   ```

2. **Add Sample Files**:
   ```bash
   python3 create_sample_audio.py  # Create test files
   python3 test_audio.py           # Verify samples work
   ```

3. **Production Verification**:
   ```bash
   python3 test_audio.py > audio_test_results.txt  # Save results
   ```

## Development Notes

- The test script is designed to be non-destructive and can be run safely in any environment
- Audio playback tests are brief (5-second timeout) to avoid hanging on problematic files  
- The script provides detailed error messages to help diagnose specific issues
- Color output can be disabled by redirecting to a file or piping through tools that strip ANSI codes

## License & Usage

These testing tools are part of the hiragana flashcard application and follow the same licensing terms. They're designed for development, testing, and educational purposes.