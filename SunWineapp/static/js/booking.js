window.addEventListener("DOMContentLoaded", function () {
    const message = "{{ message|escapejs }}";
    if (message) {
        alert(message);
    }
});