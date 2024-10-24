// Function to show the popup with a custom message
function showPopup(message) {
    document.getElementById("popup-message").textContent = message;
    document.getElementById("popup").style.display = "block";
    document.getElementById("overlay").style.display = "block";
}

// Function to close the popup
function closePopup() {
    document.getElementById("popup").style.display = "none";
    document.getElementById("overlay").style.display = "none";
}