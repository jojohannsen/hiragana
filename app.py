from fasthtml.common import *
import random
import os
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import FileResponse

# Initialize FastHTML app with database and session middleware
app, rt, characters, HiraganaCharacter = fast_app(
    'data/hiragana.db',
    render=lambda char: Li(
        Span(char.character, cls='char'), 
        ' - ', 
        Span(char.romaji, cls='romaji'),
        cls='char-item'
    ),
    id=int,
    character=str,
    romaji=str,
    pronunciation=str,
    category=str,
    order_index=int,
    pk='id'
)

# Add session middleware
app.add_middleware(SessionMiddleware, secret_key="hiragana-flashcards-secret")

# Add CSS
app.hdrs = (
    Link(rel="stylesheet", href="/static/css/styles.css"),
    Script(src="/static/js/audio.js")
)



def character_card(char):
    """Small character card for summary view"""
    return Div(
        Div(char.character, cls='char-large'),
        Div(char.romaji, cls='romaji-small'),
        Button('🔊', 
               onclick=f"playAudio('/audio/{char.id}')",
               cls='audio-btn-small',
               type='button'),
        cls='char-card',
        hx_get=f'/flashcard/{char.id}',
        hx_target='#content-area',
        hx_swap='innerHTML'
    )

@rt("/")
def get():
    """Summary view with all characters organized by category"""
    categories = ['vowels', 'ka-row', 'sa-row', 'ta-row', 'na-row', 
                  'ha-row', 'ma-row', 'ya-row', 'ra-row', 'wa-row']
    
    # Get all characters and organize by category
    try:
        all_chars = list(characters())
        print(f"Found {len(all_chars)} total characters")
    except Exception as e:
        print(f"Error getting characters: {e}")
        all_chars = []
    
    content = []
    for category in categories:
        # Filter characters by category and sort by order_index
        chars = [c for c in all_chars if c.category == category]
        chars.sort(key=lambda x: x.order_index)
        
        if chars:  # Only show categories that have characters
            print(f"Category {category}: {len(chars)} characters")
            grid = Div(
                H3(category.replace('-', ' ').title()),
                Div(*[character_card(char) for char in chars], 
                    cls='char-grid'),
                cls='category-section'
            )
            content.append(grid)
    
    return Html(
        Head(
            Title("Hiragana Learning"),
            Link(rel="stylesheet", href="/static/css/styles.css"),
            Script(src="/static/js/audio.js")
        ),
        Body(
            Main(*content, id='content-area', cls='summary-view'),
            cls='summary-page'
        )
    )


@rt("/flashcard/{card_id}")
def get(card_id: int):
    """Show specific flashcard"""
    char = characters[card_id]
    return flashcard_content(char, 0, 1)

def flashcard_content(char, current_index, total_cards):
    """Generate flashcard content"""
    return Html(
        Head(
            Title(f"Hiragana: {char.character} - {char.romaji}"),
            Link(rel="stylesheet", href="/static/css/styles.css"),
            Script(src="/static/js/audio.js")
        ),
        Body(
            Main(
                Div(
                    Div(char.character, cls='flashcard-character'),
                    Div(char.romaji, cls='flashcard-romaji'), 
                    Div(char.pronunciation, cls='flashcard-pronunciation'),
                    Button('🔊 Play Sound', 
                           onclick=f"playAudio('/audio/{char.id}')",
                           cls='audio-button',
                           type='button'),
                    A('← Back to Overview', 
                       href='/',
                       cls='back-button'),
                    cls='flashcard-content'
                ),
                cls='flashcard-view'
            )
        )
    )


@rt("/audio/{char_id}")
def get(char_id: int):
    """Serve audio file for character pronunciation"""
    char = characters[char_id]
    audio_file = f"static/audio/{char.romaji}.mp3"
    
    if os.path.exists(audio_file):
        return FileResponse(audio_file, media_type="audio/mpeg")
    else:
        # For now, return a simple response - in production you'd implement TTS
        return Response(f"Audio for {char.character} ({char.romaji}) not available", 
                       media_type="text/plain")

# Static file serving
@rt("/static/{path:path}")
def get(path: str):
    """Serve static files"""
    file_path = f"static/{path}"
    if os.path.exists(file_path):
        # Determine media type based on extension
        if path.endswith('.css'):
            media_type = "text/css"
        elif path.endswith('.js'):
            media_type = "application/javascript"
        elif path.endswith('.mp3'):
            media_type = "audio/mpeg"
        else:
            media_type = "application/octet-stream"
        
        return FileResponse(file_path, media_type=media_type)
    else:
        return Response("File not found", status_code=404)

if __name__ == "__main__":
    serve()