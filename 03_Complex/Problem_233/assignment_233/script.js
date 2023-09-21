document.addEventListener('DOMContentLoaded', function () {
    const analyzeBtn = document.getElementById('analyzeBtn');
    analyzeBtn.addEventListener('click', analyzeSentence);
});

function analyzeSentence() {
    const sentenceInput = document.getElementById('sentence');
    const uppercaseSentence = document.getElementById('uppercaseSentence');
    const sentenceLength = document.getElementById('sentenceLength');
    const totalWords = document.getElementById('totalWords');
    const totalSpaces = document.getElementById('totalSpaces');

    const sentence = sentenceInput.value;

    // Convert the sentence to uppercase
    const uppercased = sentence.toUpperCase();

    // Calculate sentence length, total words, and total spaces
    const length = sentence.length;
    const words = sentence.split(' ').filter(word => word !== '').length;
    const spaces = sentence.split(' ').length - 1;

    // Update the result elements
    uppercaseSentence.textContent = uppercased;
    sentenceLength.textContent = length;
    totalWords.textContent = words;
    totalSpaces.textContent = spaces;
}
