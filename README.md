# Hiragana Flashcard Learning System

A web-based flashcard application for learning Japanese Hiragana characters, built with FastHTML.

## Features

- **Summary View**: Visual grid of all 46 basic Hiragana characters organized by category
- **Flashcard Mode**: Large-format cards showing character, romaji, and pronunciation
- **Audio Support**: Click to hear character pronunciation (placeholder for now)
- **Responsive Design**: Works on desktop and mobile devices

## Quick Start

1. **Initialize the database:**
   ```bash
   python seed_data.py
   ```

2. **Install dependencies:**
   ```bash
   pip install python-fasthtml uvicorn fastlite starlette
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```

4. **Open in browser:**
   Navigate to `http://localhost:5001`

## Project Structure

```
hiragana-flashcards/
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
│   └── audio/          # Audio files (for future use)
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

## Future Enhancements

- [ ] Audio file integration (MP3 files in static/audio/)
- [ ] Text-to-speech generation for missing audio
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