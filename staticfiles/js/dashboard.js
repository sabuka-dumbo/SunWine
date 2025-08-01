document.addEventListener("DOMContentLoaded", function() {
  fetch("{% url 'booking' %}", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': '{{ csrf_token }}'
        },
        body: JSON.stringify({
            check_in: "2025-07-30",
            check_out: "2025-08-01",
            guests: "2 Adults, 1 Kid"
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log("Success:", data);
        // Optionally update the DOM here
    })
    .catch((error) => {
        console.error("Error:", error);
    });
})

const ctx = document.getElementById('myChart');

  new Chart(ctx, {
    type: 'pie',
    data: {
      labels: ['Not available', 'Available', 'Reserved'],
      datasets: [{
        label: 'Room:',
        data: [5, 10, 5],
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });