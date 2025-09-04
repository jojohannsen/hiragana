#!/bin/bash

# Improved Hiragana Audio Downloader
# Downloads MP3 files from ThoughtCo with rate limiting and skip existing files

echo "🎵 Downloading Hiragana Audio Files (Smart Version)"
echo "Features: Skip existing files, random delays, better error handling"
echo "============================================================"

# Create audio directory if it doesn't exist
mkdir -p static/audio
cd static/audio

# Function to download a file with smart checking
download_file() {
    local filename="$1"
    local url="$2"
    local character="$3"
    
    if [[ -f "$filename" ]]; then
        local size=$(stat -f%z "$filename" 2>/dev/null || stat -c%s "$filename" 2>/dev/null || echo "unknown")
        echo "✅ $filename already exists ($size bytes) - skipping $character"
        return 0
    fi
    
    echo "📥 Downloading $filename for $character..."
    
    # Download with better error handling
    if curl -L --fail --silent --show-error -o "$filename" "$url"; then
        local size=$(stat -f%z "$filename" 2>/dev/null || stat -c%s "$filename" 2>/dev/null || echo "unknown")
        echo "✅ Downloaded $filename ($size bytes)"
        
        # Random delay between 3-9 seconds to avoid rate limiting
        local delay=$((RANDOM % 7 + 3))
        echo "⏳ Waiting $delay seconds to avoid rate limiting..."
        sleep $delay
        return 0
    else
        echo "❌ Failed to download $filename for $character"
        return 1
    fi
}

# Counter for tracking
total_files=46
downloaded=0
skipped=0
failed=0

echo ""
echo "🎯 Processing $total_files Hiragana characters..."
echo ""

# Array of all downloads (filename, URL, character description)
declare -a downloads=(
    # Vowels
    "a.mp3|https://0.tqn.com/z/g/japanese/library/media/audio/a.mp3|あ (a)"
    "i.mp3|https://0.tqn.com/z/g/japanese/library/media/audio/i.mp3|い (i)"
    "u.mp3|https://0.tqn.com/z/g/japanese/library/media/audio/u.mp3|う (u)"
    "e.mp3|https://0.tqn.com/z/g/japanese/library/media/audio/e.mp3|え (e)"
    "o.mp3|https://0.tqn.com/z/g/japanese/library/media/audio/o.mp3|お (o)"
    
    # Ka row
    "ka.mp3|https://0.tqn.com/z/g/japanese/library/media/audio/ka.mp3|か (ka)"
    "ki.mp3|https://0.tqn.com/z/g/japanese/library/media/audio/ki.mp3|き (ki)"
    "ku.mp3|https://0.tqn.com/z/g/japanese/library/media/audio/ku.mp3|く (ku)"
    "ke.mp3|https://0.tqn.com/z/g/japanese/library/media/audio/ke.mp3|け (ke)"
    "ko.mp3|https://0.tqn.com/z/g/japanese/library/media/audio/ko.mp3|こ (ko)"
    
    # Sa row
    "sa.mp3|https://0.tqn.com/z/g/japanese/library/media/audio/sa.mp3|さ (sa)"
    "shi.mp3|https://0.tqn.com/z/g/japanese/library/media/audio/shi.mp3|し (shi)"
    "su.mp3|https://0.tqn.com/z/g/japanese/library/media/audio/su.mp3|す (su)"
    "se.mp3|https://0.tqn.com/z/g/japanese/library/media/audio/se.mp3|せ (se)"
    "so.mp3|https://0.tqn.com/z/g/japanese/library/media/audio/so.mp3|そ (so)"
    
    # Ta row
    "ta.mp3|https://0.tqn.com/z/g/japanese/library/media/audio/ta.mp3|た (ta)"
    "chi.mp3|https://0.tqn.com/z/g/japanese/library/media/audio/chi.mp3|ち (chi)"
    "tsu.mp3|https://0.tqn.com/z/g/japanese/library/media/audio/tsu.mp3|つ (tsu)"
    "te.mp3|https://0.tqn.com/z/g/japanese/library/media/audio/te.mp3|て (te)"
    "to.mp3|https://0.tqn.com/z/g/japanese/library/media/audio/to.mp3|と (to)"
    
    # Na row
    "na.mp3|https://0.tqn.com/z/g/japanese/library/media/audio/na.mp3|な (na)"
    "ni.mp3|https://0.tqn.com/z/g/japanese/library/media/audio/ni.mp3|に (ni)"
    "nu.mp3|https://0.tqn.com/z/g/japanese/library/media/audio/nu.mp3|ぬ (nu)"
    "ne.mp3|https://0.tqn.com/z/g/japanese/library/media/audio/ne.mp3|ね (ne)"
    "no.mp3|https://0.tqn.com/z/g/japanese/library/media/audio/no.mp3|の (no)"
    
    # Ha row
    "ha.mp3|https://0.tqn.com/z/g/japanese/library/media/audio/ha.mp3|は (ha)"
    "hi.mp3|https://0.tqn.com/z/g/japanese/library/media/audio/hi.mp3|ひ (hi)"
    "fu.mp3|https://0.tqn.com/z/g/japanese/library/media/audio/fu.mp3|ふ (fu)"
    "he.mp3|https://0.tqn.com/z/g/japanese/library/media/audio/he.mp3|へ (he)"
    "ho.mp3|https://0.tqn.com/z/g/japanese/library/media/audio/ho.mp3|ほ (ho)"
    
    # Ma row
    "ma.mp3|https://0.tqn.com/z/g/japanese/library/media/audio/ma.mp3|ま (ma)"
    "mi.mp3|https://0.tqn.com/z/g/japanese/library/media/audio/mi.mp3|み (mi)"
    "mu.mp3|https://0.tqn.com/z/g/japanese/library/media/audio/mu.mp3|む (mu)"
    "me.mp3|https://0.tqn.com/z/g/japanese/library/media/audio/me.mp3|め (me)"
    "mo.mp3|https://0.tqn.com/z/g/japanese/library/media/audio/mo.mp3|も (mo)"
    
    # Ya row
    "ya.mp3|https://0.tqn.com/z/g/japanese/library/media/audio/ya.mp3|や (ya)"
    "yu.mp3|https://0.tqn.com/z/g/japanese/library/media/audio/yu.mp3|ゆ (yu)"
    "yo.mp3|https://0.tqn.com/z/g/japanese/library/media/audio/yo.mp3|よ (yo)"
    
    # Ra row
    "ra.mp3|https://0.tqn.com/z/g/japanese/library/media/audio/ra.mp3|ら (ra)"
    "ri.mp3|https://0.tqn.com/z/g/japanese/library/media/audio/ri.mp3|り (ri)"
    "ru.mp3|https://0.tqn.com/z/g/japanese/library/media/audio/ru.mp3|る (ru)"
    "re.mp3|https://0.tqn.com/z/g/japanese/library/media/audio/re.mp3|れ (re)"
    "ro.mp3|https://0.tqn.com/z/g/japanese/library/media/audio/ro.mp3|ろ (ro)"
    
    # Wa row + N
    "wa.mp3|https://0.tqn.com/z/g/japanese/library/media/audio/wa.mp3|わ (wa)"
    "wo.mp3|https://0.tqn.com/z/g/japanese/library/media/audio/o.mp3|を (wo)"
    "n.mp3|https://0.tqn.com/z/g/japanese/library/media/audio/n.mp3|ん (n)"
)

# Process each download
for download in "${downloads[@]}"; do
    IFS='|' read -r filename url character <<< "$download"
    
    if download_file "$filename" "$url" "$character"; then
        if [[ -f "$filename" ]]; then
            if [[ $(stat -f%z "$filename" 2>/dev/null || stat -c%s "$filename" 2>/dev/null) -gt 0 ]]; then
                ((downloaded++))
            else
                ((skipped++))
            fi
        else
            ((skipped++))
        fi
    else
        ((failed++))
    fi
done

# Return to project root
cd ../..

echo ""
echo "============================================================"
echo "🎉 Download Summary"
echo "============================================================"
echo "📊 Total files processed: $total_files"
echo "📥 Downloaded: $downloaded"
echo "⏭️  Skipped (already exist): $skipped"
echo "❌ Failed: $failed"
echo ""

# Final verification
actual_files=$(ls static/audio/*.mp3 2>/dev/null | wc -l | tr -d ' ')
echo "🎯 Audio files in directory: $actual_files/46"

if [[ $actual_files -eq 46 ]]; then
    echo "✅ All Hiragana audio files are ready!"
    echo "🚀 Run: python app.py"
else
    echo "⚠️  Missing $(( 46 - actual_files )) audio files"
    echo "💡 Run this script again to download missing files"
fi

echo ""
echo "🔧 Test audio files: python test_audio.py"