document.addEventListener("DOMContentLoaded", function () {
    // Form Validation
    function validateForm() {
        let price = document.getElementsByName("price")[0].value;

        if (price <= 0) {
            showAlert("Price must be greater than 0!", "error");
            return false;
        }

        showAlert("Processing your request...", "success");
        return true;
    }

    // Display Alerts
    function showAlert(message, type) {
        let alertBox = document.createElement("div");
        alertBox.className = `alert ${type}`;
        alertBox.innerText = message;
        document.body.appendChild(alertBox);

        setTimeout(() => {
            alertBox.style.opacity = "0";
            setTimeout(() => alertBox.remove(), 500);
        }, 2000);
    }

    // Add animation to car cards
    let carCards = document.querySelectorAll(".car-card");
    carCards.forEach((card, index) => {
        setTimeout(() => {
            card.classList.add("fade-in");
        }, index * 150);
    });

    // Expose validateForm globally
    window.validateForm = validateForm;
});
