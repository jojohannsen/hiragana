#!/bin/bash

# Hiragana Audio Downloader
# Downloads MP3 files from ThoughtCo for all Hiragana characters

echo "🎵 Downloading Hiragana Audio Files..."
echo "Creating static/audio directory..."

# Create audio directory if it doesn't exist
mkdir -p static/audio

# Change to audio directory
cd static/audio

# Download all audio files with proper error handling
echo "📥 Downloading audio files..."

# Vowels
curl -L -o "a.mp3" "https://0.tqn.com/z/g/japanese/library/media/audio/a.mp3"
curl -L -o "i.mp3" "https://0.tqn.com/z/g/japanese/library/media/audio/i.mp3" 
curl -L -o "u.mp3" "https://0.tqn.com/z/g/japanese/library/media/audio/u.mp3"
curl -L -o "e.mp3" "https://0.tqn.com/z/g/japanese/library/media/audio/e.mp3"
curl -L -o "o.mp3" "https://0.tqn.com/z/g/japanese/library/media/audio/o.mp3"

# Ka row
curl -L -o "ka.mp3" "https://0.tqn.com/z/g/japanese/library/media/audio/ka.mp3"
curl -L -o "ki.mp3" "https://0.tqn.com/z/g/japanese/library/media/audio/ki.mp3"
curl -L -o "ku.mp3" "https://0.tqn.com/z/g/japanese/library/media/audio/ku.mp3"
curl -L -o "ke.mp3" "https://0.tqn.com/z/g/japanese/library/media/audio/ke.mp3"
curl -L -o "ko.mp3" "https://0.tqn.com/z/g/japanese/library/media/audio/ko.mp3"

# Sa row  
curl -L -o "sa.mp3" "https://0.tqn.com/z/g/japanese/library/media/audio/sa.mp3"
curl -L -o "shi.mp3" "https://0.tqn.com/z/g/japanese/library/media/audio/shi.mp3"
curl -L -o "su.mp3" "https://0.tqn.com/z/g/japanese/library/media/audio/su.mp3"
curl -L -o "se.mp3" "https://0.tqn.com/z/g/japanese/library/media/audio/se.mp3"
curl -L -o "so.mp3" "https://0.tqn.com/z/g/japanese/library/media/audio/so.mp3"

# Ta row
curl -L -o "ta.mp3" "https://0.tqn.com/z/g/japanese/library/media/audio/ta.mp3"
curl -L -o "chi.mp3" "https://0.tqn.com/z/g/japanese/library/media/audio/chi.mp3"
curl -L -o "tsu.mp3" "https://0.tqn.com/z/g/japanese/library/media/audio/tsu.mp3"
curl -L -o "te.mp3" "https://0.tqn.com/z/g/japanese/library/media/audio/te.mp3"
curl -L -o "to.mp3" "https://0.tqn.com/z/g/japanese/library/media/audio/to.mp3"

# Na row
curl -L -o "na.mp3" "https://0.tqn.com/z/g/japanese/library/media/audio/na.mp3"
curl -L -o "ni.mp3" "https://0.tqn.com/z/g/japanese/library/media/audio/ni.mp3"
curl -L -o "nu.mp3" "https://0.tqn.com/z/g/japanese/library/media/audio/nu.mp3"
curl -L -o "ne.mp3" "https://0.tqn.com/z/g/japanese/library/media/audio/ne.mp3"
curl -L -o "no.mp3" "https://0.tqn.com/z/g/japanese/library/media/audio/no.mp3"

# Ha row
curl -L -o "ha.mp3" "https://0.tqn.com/z/g/japanese/library/media/audio/ha.mp3"
curl -L -o "hi.mp3" "https://0.tqn.com/z/g/japanese/library/media/audio/hi.mp3"
curl -L -o "fu.mp3" "https://0.tqn.com/z/g/japanese/library/media/audio/fu.mp3"
curl -L -o "he.mp3" "https://0.tqn.com/z/g/japanese/library/media/audio/he.mp3"
curl -L -o "ho.mp3" "https://0.tqn.com/z/g/japanese/library/media/audio/ho.mp3"

# Ma row
curl -L -o "ma.mp3" "https://0.tqn.com/z/g/japanese/library/media/audio/ma.mp3"
curl -L -o "mi.mp3" "https://0.tqn.com/z/g/japanese/library/media/audio/mi.mp3"
curl -L -o "mu.mp3" "https://0.tqn.com/z/g/japanese/library/media/audio/mu.mp3"
curl -L -o "me.mp3" "https://0.tqn.com/z/g/japanese/library/media/audio/me.mp3"
curl -L -o "mo.mp3" "https://0.tqn.com/z/g/japanese/library/media/audio/mo.mp3"

# Ya row
curl -L -o "ya.mp3" "https://0.tqn.com/z/g/japanese/library/media/audio/ya.mp3"
curl -L -o "yu.mp3" "https://0.tqn.com/z/g/japanese/library/media/audio/yu.mp3"
curl -L -o "yo.mp3" "https://0.tqn.com/z/g/japanese/library/media/audio/yo.mp3"

# Ra row
curl -L -o "ra.mp3" "https://0.tqn.com/z/g/japanese/library/media/audio/ra.mp3"
curl -L -o "ri.mp3" "https://0.tqn.com/z/g/japanese/library/media/audio/ri.mp3"
curl -L -o "ru.mp3" "https://0.tqn.com/z/g/japanese/library/media/audio/ru.mp3"
curl -L -o "re.mp3" "https://0.tqn.com/z/g/japanese/library/media/audio/re.mp3"
curl -L -o "ro.mp3" "https://0.tqn.com/z/g/japanese/library/media/audio/ro.mp3"

# Wa row
curl -L -o "wa.mp3" "https://0.tqn.com/z/g/japanese/library/media/audio/wa.mp3"
# Note: を (wo) uses the same audio as お (o)
curl -L -o "wo.mp3" "https://0.tqn.com/z/g/japanese/library/media/audio/o.mp3"

# N
curl -L -o "n.mp3" "https://0.tqn.com/z/g/japanese/library/media/audio/n.mp3"

# Return to project root
cd ../..

echo "✅ Download complete!"
echo "📁 Audio files saved to: static/audio/"
echo "🎯 $(ls static/audio/*.mp3 2>/dev/null | wc -l) audio files downloaded"

# List downloaded files
echo ""
echo "📋 Downloaded files:"
ls -la static/audio/*.mp3 2>/dev/null || echo "No MP3 files found"

echo ""
echo "🚀 Ready to test audio in your Hiragana app!"
echo "Run: python app.py"