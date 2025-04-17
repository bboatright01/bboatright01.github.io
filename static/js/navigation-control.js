document.addEventListener('DOMContentLoaded', () => {
    console.log("Navigation control script loaded");

    const buttonsContainer = document.querySelector('.buttons');
    if (!buttonsContainer) return console.log("No buttons container found");

    fixNavigationLinks();

    let isLoggedIn = localStorage.getItem('isLoggedIn') === 'true';
    let userType = localStorage.getItem('userType') || '';

    if (!isLoggedIn) {
        const path = window.location.pathname;
        const isDashboard = path.includes('dashboard') || path.includes('profile');
        const userWelcome = document.querySelector('h1')?.textContent.includes('Welcome') || false;
        const logoutLink = document.querySelector('a[href="/logout"]');

        isLoggedIn = !!logoutLink || isDashboard || userWelcome;

        if (isLoggedIn) {
            localStorage.setItem('isLoggedIn', 'true');
            if (!userType) {
                if (path.includes('ngo')) userType = 'ngo';
                else if (path.includes('donor')) userType = 'donor';
                if (userType) localStorage.setItem('userType', userType);
            }
        }
    }

    console.log("Is logged in:", isLoggedIn);
    console.log("User type:", userType);

    const loginForm = document.querySelector('form.login-form');
    const accountTypeRadios = document.querySelectorAll('input[name="accountType"]');

    if (loginForm && accountTypeRadios.length > 0) {
        console.log("Login form with account type selection found");
        loginForm.addEventListener('submit', () => {
            const selectedType = document.querySelector('input[name="accountType"]:checked')?.value;
            if (selectedType) {
                console.log("Form submitted with account type:", selectedType);
                sessionStorage.setItem('pending_login_type', selectedType);
                sessionStorage.setItem('login_attempted', 'true');
            }
        });
    }

    const successFlash = document.querySelector('.flash.success');
    if (successFlash?.textContent.includes('Login successful')) {
        const pendingType = sessionStorage.getItem('pending_login_type');
        const loginAttempted = sessionStorage.getItem('login_attempted');

        if (pendingType && loginAttempted) {
            console.log("Login success detected! User type:", pendingType);
            localStorage.setItem('isLoggedIn', 'true');
            localStorage.setItem('userType', pendingType);
            userType = pendingType;

            sessionStorage.removeItem('pending_login_type');
            sessionStorage.removeItem('login_attempted');

            const path = window.location.pathname;
            if (pendingType === 'ngo' && !path.includes('ngo-dashboard')) {
                window.location.href = '/ngo-dashboard';
            } else if (pendingType === 'donor' && !path.includes('donor-dashboard')) {
                window.location.href = '/donor-dashboard';
            }
        }
    }

    updateNavigation(isLoggedIn, userType);
    updateNavLinks(isLoggedIn, userType);

    document.addEventListener('click', e => {
        if (e.target?.href?.includes('/logout')) {
            localStorage.removeItem('isLoggedIn');
            localStorage.removeItem('userType');
        }
    });

    function updateNavigation(isLoggedIn, userType) {
        if (!buttonsContainer || !isLoggedIn) return;

        const loginButton = buttonsContainer.querySelector('a[href="/donor-login"]');
        const registerButton = buttonsContainer.querySelector('a[href="/donor-registration"]');

        if (!loginButton && !registerButton) return;

        buttonsContainer.innerHTML = '';

        const profileLink = document.createElement('a');
        profileLink.className = 'btn-login';
        styleButton(profileLink);
        profileLink.href = userType === 'ngo' ? '/ngo-dashboard' : '/donor-dashboard';
        profileLink.textContent = 'Profile';

        const logoutLink = document.createElement('a');
        logoutLink.href = '/logout';
        logoutLink.className = 'btn-login';
        logoutLink.textContent = 'Logout';
        styleButton(logoutLink);

        buttonsContainer.append(profileLink, logoutLink);
    }

    function updateNavLinks(isLoggedIn, userType) {
        const navLinks = document.querySelector('.nav-links');
        if (!navLinks) return;

        console.log("Updating nav links for user type:", userType);

        const donateLinks = Array.from(navLinks.querySelectorAll('a[href="donate.html"], a[href="/donate"]'));
        const createLinks = Array.from(navLinks.querySelectorAll('a[href="/create"]'));

        donateLinks.forEach(link => {
            link.parentElement.style.display = (isLoggedIn && userType === 'donor') ? '' : 'none';
        });

        if (isLoggedIn && userType === 'donor' && donateLinks.length === 0) {
            const donateItem = document.createElement('li');
            donateItem.innerHTML = '<a href="/donate">Donate</a>';
            navLinks.appendChild(donateItem);
        }

        createLinks.forEach(link => {
            link.parentElement.style.display = (isLoggedIn && userType === 'ngo') ? '' : 'none';
        });

        if (isLoggedIn && userType === 'ngo' && createLinks.length === 0) {
            const createItem = document.createElement('li');
            createItem.innerHTML = '<a href="/create">Create Campaign</a>';
            navLinks.appendChild(createItem);
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

    function styleButton(button) {
        Object.assign(button.style, {
            display: 'inline-block',
            padding: '10px 20px',
            backgroundColor: '#4CAF50',
            color: 'white',
            textDecoration: 'none',
            border: '2px solid white',
            borderRadius: '5px',
            margin: '0 5px'
        });
    }
});
