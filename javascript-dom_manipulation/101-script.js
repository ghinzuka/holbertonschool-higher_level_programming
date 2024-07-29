document.addEventListener('DOMContentLoaded', function() {
    const translateButton = document.getElementById('btn_translate');
    const languageSelect = document.getElementById('language_code');
    const helloDiv = document.getElementById('hello');

    translateButton.addEventListener('click', function() {
        const languageCode = languageSelect.value;
        if (languageCode) {
            fetch(`https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`)
                .then(response => response.json())
                .then(data => {
                    helloDiv.textContent = data.hello;
                })
                .catch(error => {
                    console.error('Error:', error);
                    helloDiv.textContent = 'Translation failed!';
                });
        } else {
            helloDiv.textContent = 'Please select a language code.';
        }
    });
});