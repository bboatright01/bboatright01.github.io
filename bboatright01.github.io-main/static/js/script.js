// Waits for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Get the campaign row and carousel arrows
    const campaignRow = document.querySelector('.campaign-row');
    const leftArrow = document.querySelector('.left-arrow');
    const rightArrow = document.querySelector('.right-arrow');
    const cards = document.querySelectorAll('.campaign-card');
    
    // Base card width to help with calculations
    const baseCardWidth = 300;
    
    // Calculates the scroll amount dynamically
    function getScrollAmount() {
        // Gets the actual width of a card including the margins
        const cardStyle = window.getComputedStyle(cards[0]);
        const cardWidth = cards[0].offsetWidth;
        const cardMarginLeft = parseInt(cardStyle.marginLeft) || 0;
        const cardMarginRight = parseInt(cardStyle.marginRight) || 0;
        const gapSize = parseInt(window.getComputedStyle(campaignRow).gap) || 40;
        
        return cardWidth + gapSize;
    }
    
    // Adds a click event for the right arrow
    rightArrow.addEventListener('click', function() {
        campaignRow.scrollBy({
            left: getScrollAmount(),
            behavior: 'smooth'
        });
    });
    
    // Adds a click event for the left arrow
    leftArrow.addEventListener('click', function() {
        campaignRow.scrollBy({
            left: -getScrollAmount(),
            behavior: 'smooth'
        });
    });
    
    // A function to distribute the cards in the available space
    function distributeCards() {
        const containerWidth = campaignRow.offsetWidth;
        const totalCards = cards.length;
        
        // Gets the current card width from CSS file
        const cardStyle = window.getComputedStyle(cards[0]);
        const cardWidth = parseInt(cardStyle.width) || baseCardWidth;
        
        // Calculates the total width needed for all of the cards
        const totalCardsWidth = cardWidth * totalCards;
        
        // Gets the available space for the gaps
        const availableSpace = containerWidth - totalCardsWidth;
        
        // Shows all of the cards if there is enough screen space
        if (availableSpace > 0 && totalCards > 1) {
            // Calculates the optimal gap size to distribute the cards evenly
            const optimalGap = availableSpace / (totalCards - 1);
            
            // For ultra-wide screens, this allows larger gaps
            const screenWidth = window.innerWidth;
            let maxGap = 80; // Default max gap
            
            if (screenWidth >= 2000) {
                maxGap = 200; // Adds a much larger gaps for very wide screens
            } else if (screenWidth >= 1600) {
                maxGap = 150; // Adds a much larger gaps for very wide screens
            } else if (screenWidth >= 1200) {
                maxGap = 100; // Adds a much medium gaps for very wide screens
            }
            
            const finalGap = Math.min(optimalGap, maxGap);
            campaignRow.style.gap = finalGap + 'px';
            
            // Adjusts the padding to center the content
            if (optimalGap > maxGap) {
                const extraSpace = availableSpace - (finalGap * (totalCards - 1));
                const sidePadding = extraSpace / 2;
                campaignRow.style.paddingLeft = sidePadding + 'px';
                campaignRow.style.paddingRight = sidePadding + 'px';
            }
        }
    }
    
    distributeCards();
    window.addEventListener('resize', distributeCards);
});