document.getElementById('prediction-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const formData = new FormData();
    const files = document.getElementById('input-data').files;
    if (files.length !== 24) {
        alert('Please upload exactly 24 images.');
        return;
    }
    for (let i = 0; i < files.length; i++) {
        formData.append('images', files[i]);
    }
    fetch('/predict', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            document.getElementById('result').innerText = 'Predicted Class: ' + data.predicted_class;
        }
    });
});