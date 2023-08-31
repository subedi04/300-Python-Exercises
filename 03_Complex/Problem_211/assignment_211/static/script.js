// static/script.js
document.addEventListener('DOMContentLoaded', () => {
    const buttons = document.querySelectorAll('button');
    const resultDiv = document.getElementById('result');
    const num1Input = document.getElementById('num1');
    const num2Input = document.getElementById('num2');

    buttons.forEach(button => {
        button.addEventListener('click', () => {
            const operation = button.id;
            const num1 = parseFloat(num1Input.value);
            const num2 = parseFloat(num2Input.value);

            if (!isNaN(num1) && !isNaN(num2)) {
                fetch('/calculate', {
                    method: 'POST',
                    body: new URLSearchParams({ num1, num2, operation }),
                })
                .then(response => response.json())
                .then(data => {
                    resultDiv.innerText = `Result: ${data.result}`;
                });
            } else {
                resultDiv.innerText = 'Invalid input';
            }
        });
    });
});
