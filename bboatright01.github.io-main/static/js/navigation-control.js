document.addEventListener('DOMContentLoaded', () => {
    console.log("Navigation control script loaded");

    const userTypeElement = document.getElementById('user-type-data');
    const userType = userTypeElement ? userTypeElement.value : 'none';
    const isLoggedIn = userType !== 'none';

    console.log("Is logged in:", isLoggedIn);
    console.log("User type:", userType);

    // Fix navigation links if needed
    fixNavigationLinks();

    // Listen for logout clicks to clear any stored data
    document.addEventListener('click', e => {
        if (e.target?.href?.includes('/logout')) {
            console.log("Logout detected, clearing storage");
            sessionStorage.clear();
            localStorage.clear();
        }
    });

    // Handle flash messages for NGO login success
    const successFlash = document.querySelector('.flash.success');
    if (successFlash?.textContent.includes('NGO login successful')) {
        console.log("NGO login success detected!");
        localStorage.setItem('userType', 'ngo');
        
        // Redirect to NGO dashboard if needed
        const path = window.location.pathname;
        if (!path.includes('ngo-dashboard')) {
            window.location.href = '/ngo-dashboard';
        }
    }

    function fixNavigationLinks() {
        const linkFixes = [
            { selector: 'a[href="search.html"]', newHref: '/search' },
            { selector: 'a[href="about.html"]', newHref: '/about' },
            { selector: 'a[href="donate.html"]', newHref: '/donate' }
        ];

        linkFixes.forEach(({ selector, newHref }) => {
            document.querySelectorAll(selector).forEach(link => link.href = newHref);
        });
    }
});