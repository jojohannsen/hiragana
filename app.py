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

def get_current_session(session):
    """Get or create learning session"""
    if 'current_cards' not in session:
        # Create randomized list of all characters
        all_chars = list(characters())
        random.shuffle(all_chars)
        session['current_cards'] = [c.id for c in all_chars]
        session['current_index'] = 0
    return session

def get_current_card(session):
    """Get current card from session"""
    session_data = get_current_session(session)
    if not session_data['current_cards']:
        return None
    card_id = session_data['current_cards'][session_data['current_index']]
    return characters[card_id]

def navigation_buttons(show_begin=False, show_nav=False, show_exit=False, current_index=0, total_cards=0):
    """Context-aware navigation buttons"""
    buttons = []
    
    if show_begin:
        buttons.append(Button('BEGIN', 
            hx_post='/begin', 
            hx_target='#content-area',
            hx_swap='innerHTML',
            cls='nav-btn begin-btn',
            id='begin-btn'))
    
    if show_nav:
        # Previous button (disabled if at start)
        prev_disabled = current_index == 0
        buttons.append(Button('PREVIOUS', 
            hx_post='/previous', 
            hx_target='#content-area',
            hx_swap='innerHTML',
            cls=f'nav-btn prev-btn {"disabled" if prev_disabled else ""}',
            disabled=prev_disabled,
            id='previous-btn'))
        
        # Next button (disabled if at end)
        next_disabled = current_index >= total_cards - 1
        buttons.append(Button('NEXT', 
            hx_post='/next', 
            hx_target='#content-area',
            hx_swap='innerHTML',
            cls=f'nav-btn next-btn {"disabled" if next_disabled else ""}',
            disabled=next_disabled,
            id='next-btn'))
    
    if show_exit:
        buttons.append(Button('EXIT', 
            hx_get='/', 
            hx_target='body',
            hx_swap='innerHTML',
            cls='nav-btn exit-btn',
            id='exit-btn'))
    
    return Div(*buttons, cls='nav-controls', id='nav-controls')

def character_card(char):
    """Small character card for summary view"""
    return Div(
        Div(char.character, cls='char-large'),
        Div(char.romaji, cls='romaji-small'),
        cls='char-card',
        onclick=f"playAudio('/audio/{char.id}')",
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
            navigation_buttons(show_begin=True),
            Main(*content, id='content-area', cls='summary-view'),
            cls='summary-page'
        )
    )

@rt("/flashcard")
def get(session):
    """Show current flashcard from session"""
    char = get_current_card(session)
    if not char:
        return RedirectResponse('/')
    
    session_data = get_current_session(session)
    current_index = session_data['current_index']
    total_cards = len(session_data['current_cards'])
    
    return flashcard_content(char, current_index, total_cards)

@rt("/flashcard/{card_id}")
def get(card_id: int, session):
    """Show specific flashcard and update session"""
    char = characters[card_id]
    
    # Update session to reflect current card
    session_data = get_current_session(session)
    try:
        session_data['current_index'] = session_data['current_cards'].index(card_id)
    except ValueError:
        # Card not in current session, add it
        session_data['current_cards'] = [card_id]
        session_data['current_index'] = 0
    
    current_index = session_data['current_index']
    total_cards = len(session_data['current_cards'])
    
    return flashcard_content(char, current_index, total_cards)

def flashcard_content(char, current_index, total_cards):
    """Generate flashcard content"""
    return Div(
        navigation_buttons(show_nav=True, show_exit=True, 
                          current_index=current_index, total_cards=total_cards),
        Div(
            Div(char.character, cls='flashcard-character'),
            Div(char.romaji, cls='flashcard-romaji'), 
            Div(char.pronunciation, cls='flashcard-pronunciation'),
            Div(f"Card {current_index + 1} of {total_cards}", cls='card-counter'),
            cls='flashcard-content',
            onclick=f"playAudio('/audio/{char.id}')"
        ),
        cls='flashcard-view'
    )

@rt("/begin")
def post(session):
    """Start new random learning session"""
    # Reset session
    session.pop('current_cards', None)
    session.pop('current_index', None)
    
    # Get first card from new session
    char = get_current_card(session)
    if not char:
        return Div(P("No characters available"), cls='error')
    
    session_data = get_current_session(session)
    return flashcard_content(char, 0, len(session_data['current_cards']))

@rt("/next")
def post(session):
    """Navigate to next card"""
    session_data = get_current_session(session)
    if session_data['current_index'] < len(session_data['current_cards']) - 1:
        session_data['current_index'] += 1
    
    char = get_current_card(session)
    return flashcard_content(char, session_data['current_index'], len(session_data['current_cards']))

@rt("/previous")
def post(session):
    """Navigate to previous card"""
    session_data = get_current_session(session)
    if session_data['current_index'] > 0:
        session_data['current_index'] -= 1
    
    char = get_current_card(session)
    return flashcard_content(char, session_data['current_index'], len(session_data['current_cards']))

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