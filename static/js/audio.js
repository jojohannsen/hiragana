// Audio handling for Hiragana flashcard application

// Simple audio playback function
function playAudio(url) {
    // Create new audio element
    const audio = new Audio(url);
    
    // Set volume and playback rate for learning
    audio.volume = 0.8;
    audio.playbackRate = 0.9; // Slightly slower for learning
    
    // Play the audio with error handling
    audio.play().catch(error => {
        console.error('Audio playback failed:', error);
        
        // Show a brief visual feedback if audio fails
        showAudioError();
    });
    
    // Optional: show loading state while audio loads
    audio.addEventListener('loadstart', () => {
        console.log('Loading audio...');
    });
    
    audio.addEventListener('canplay', () => {
        console.log('Audio ready to play');
    });
}

// Show visual feedback when audio fails
function showAudioError() {
    // Create temporary message
    const message = document.createElement('div');
    message.textContent = '🔇 Audio not available';
    message.style.cssText = `
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background: #ff6b6b;
        color: white;
        padding: 1rem 2rem;
        border-radius: 8px;
        z-index: 10000;
        font-size: 1rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    `;
    
    document.body.appendChild(message);
    
    // Remove message after 2 seconds
    setTimeout(() => {
        if (message.parentNode) {
            message.parentNode.removeChild(message);
        }
    }, 2000);
}

// Optional: Preload audio for better performance
function preloadAudio(urls) {
    urls.forEach(url => {
        const audio = new Audio(url);
        audio.preload = 'metadata';
    });
}

// Keyboard shortcuts for navigation
document.addEventListener('keydown', (event) => {
    // Only handle shortcuts when not in an input field
    if (event.target.tagName === 'INPUT' || event.target.tagName === 'TEXTAREA') {
        return;
    }
    
    switch(event.key) {
        case 'ArrowRight':
        case ' ': // Spacebar
            event.preventDefault();
            const nextBtn = document.getElementById('next-btn');
            if (nextBtn && !nextBtn.disabled) {
                nextBtn.click();
            }
            break;
            
        case 'ArrowLeft':
            event.preventDefault();
            const prevBtn = document.getElementById('previous-btn');
            if (prevBtn && !prevBtn.disabled) {
                prevBtn.click();
            }
            break;
            
        case 'Enter':
            event.preventDefault();
            // Try to play audio if we're on a flashcard
            const flashcard = document.querySelector('.flashcard-content');
            if (flashcard && flashcard.onclick) {
                flashcard.click();
            }
            break;
            
        case 'Escape':
            event.preventDefault();
            const exitBtn = document.getElementById('exit-btn');
            if (exitBtn) {
                exitBtn.click();
            }
            break;
            
        case 'b':
        case 'B':
            event.preventDefault();
            const beginBtn = document.getElementById('begin-btn');
            if (beginBtn) {
                beginBtn.click();
            }
            break;
    }
});

// Show keyboard shortcuts help on page load (optional)
function showKeyboardHelp() {
    console.log(`
🎹 Keyboard Shortcuts:
→ / Space  - Next card
←          - Previous card  
Enter      - Play audio
Escape     - Exit to summary
B          - Begin session
    `);
}

// Initialize when page loads
document.addEventListener('DOMContentLoaded', () => {
    showKeyboardHelp();
    
    // Add visual feedback to buttons on hover
    const buttons = document.querySelectorAll('.nav-btn');
    buttons.forEach(button => {
        button.addEventListener('mouseenter', () => {
            button.style.transform = button.disabled ? 'none' : 'translateY(-2px)';
        });
        
        button.addEventListener('mouseleave', () => {
            button.style.transform = 'translateY(0)';
        });
    });
});

// Handle HTMX events for smooth transitions
document.body.addEventListener('htmx:beforeSwap', (event) => {
    // Add fade effect before content swap
    const contentArea = document.getElementById('content-area');
    if (contentArea) {
        contentArea.style.opacity = '0.7';
    }
});

document.body.addEventListener('htmx:afterSwap', (event) => {
    // Restore opacity after content swap
    const contentArea = document.getElementById('content-area');
    if (contentArea) {
        contentArea.style.opacity = '1';
        
        // Re-initialize button event listeners for new content
        const buttons = contentArea.querySelectorAll('.nav-btn');
        buttons.forEach(button => {
            button.addEventListener('mouseenter', () => {
                button.style.transform = button.disabled ? 'none' : 'translateY(-2px)';
            });
            
            button.addEventListener('mouseleave', () => {
                button.style.transform = 'translateY(0)';
            });
        });
    }
});