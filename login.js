// LMS Login Page Script
document.addEventListener("DOMContentLoaded", () => {
    const loginForm = document.getElementById("login-form");
    const usernameInput = document.getElementById("username");
    const passwordInput = document.getElementById("password");
    const statusMessage = document.getElementById("status-message");

    loginForm.addEventListener("submit", (e) => {
        e.preventDefault();

        const username = usernameInput.value.trim();
        const password = passwordInput.value;

        // Reset status message
        statusMessage.className = "";
        statusMessage.style.display = "none";
        statusMessage.textContent = "";

        // Simulate backend authentication request with a short delay (350ms)
        // This simulates real-world latency and verifies explicit waits in test automation
        setTimeout(() => {
            if (username === "librarian" && password === "LMS@pass2026") {
                statusMessage.className = "success-msg";
                statusMessage.textContent = "Login successful! Welcome to the Library Management System.";
            } else {
                statusMessage.className = "error-msg";
                statusMessage.textContent = "Invalid credentials. Please check your username or password.";
            }
        }, 350);
    });
});
