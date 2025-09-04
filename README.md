# Hiragana Flashcard Learning System

A web-based flashcard application for learning Japanese Hiragana characters, built with FastHTML.

## Features

- **Summary View**: Visual grid of all 46 basic Hiragana characters organized by category
- **Flashcard Mode**: Large-format cards showing character, romaji, and pronunciation
- **Audio Support**: Click to hear authentic Japanese pronunciation for all 46 characters
- **Responsive Design**: Works on desktop and mobile devices

## Quick Start

1. **Initialize the database:**
   ```bash
   python seed_data.py
   ```

2. **Download audio files:**
   ```bash
   ./download_audio.sh
   ```

3. **Install dependencies:**
   ```bash
   pip install python-fasthtml uvicorn fastlite starlette
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```

5. **Open in browser:**
   Navigate to `http://localhost:5001`

## Project Structure

```
hiragana/
├── app.py              # Main FastHTML application
├── seed_data.py        # Database initialization
├── requirements.txt    # Python dependencies
├── data/
│   └── hiragana.db    # SQLite database (created by seed_data.py)
├── static/
│   ├── css/
│   │   └── styles.css  # Application styles
│   ├── js/
│   │   └── audio.js    # Audio and interaction handling
│   └── audio/          # MP3 pronunciation files (46 files)
├── download_audio.sh   # Script to download audio files
├── test_audio.py      # Audio file verification script
└── README.md
```

## Character Categories

The application organizes Hiragana into traditional categories:
- **Vowels**: あ い う え お
- **Ka-row**: か き く け こ
- **Sa-row**: さ し す せ そ
- **Ta-row**: た ち つ て と
- **Na-row**: な に ぬ ね の
- **Ha-row**: は ひ ふ へ ほ
- **Ma-row**: ま み む め も
- **Ya-row**: や ゆ よ
- **Ra-row**: ら り る れ ろ
- **Wa-row**: わ を ん

## Usage

### Summary View
- View all characters organized by category
- Click any character to view as a flashcard
- Click the audio button (🔊) to hear pronunciation

### Flashcard Mode
- Large character display with romaji and pronunciation
- Click "Play Sound" button for audio
- Use "Back to Overview" button to return to summary view

## Audio Integration

The application includes high-quality pronunciation audio for all 46 Hiragana characters:
- **Source**: Professional recordings from ThoughtCo.com
- **Format**: MP3 files optimized for web delivery
- **Coverage**: Complete set covering all basic Hiragana
- **Testing**: Use `python test_audio.py` to verify all files

## Future Enhancements

- [x] Audio file integration (MP3 files in static/audio/)
- [ ] Offline audio caching for mobile devices
- [ ] Progress tracking and statistics
- [ ] Spaced repetition algorithm
- [ ] Additional character sets (Katakana, Kanji)
- [ ] User accounts and learning history
- [ ] Quiz and testing modes

## Development

The application uses:
- **FastHTML**: Python web framework with HTMX integration
- **SQLite**: Database for character storage
- **Starlette**: ASGI web framework (underlying FastHTML)
- **HTMX**: Dynamic interactions without JavaScript frameworks

## License

This project is open source and available under the MIT License.
