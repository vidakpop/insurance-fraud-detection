document.addEventListener('DOMContentLoaded', function() {
    const proceedButton = document.getElementById('proceedButton');
    const insuranceType = document.getElementById('insuranceType');
    const insuranceForm = document.getElementById('insuranceForm');

    proceedButton.addEventListener('click', function(event) {
        event.preventDefault();
        const selectedType = insuranceType.value;
        if (selectedType) {
            const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

            fetch('/profile/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken
                },
                body: JSON.stringify({
                    insuranceType: selectedType
                })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert(`You have selected ${selectedType} insurance.`);
                    window.location.href = `/${selectedType}/`;
                } else {
                    alert('Error: ' + data.error);
                }
            })
            .catch(error => console.error('Error:', error));
        } else {
            alert('Please select an insurance type.');
        }
    });
});
