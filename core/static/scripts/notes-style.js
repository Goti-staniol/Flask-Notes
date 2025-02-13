const photoUpload = document.getElementById('photo-upload');
const photosContainer = document.getElementById('photos-container');
let uploadedPhotos = []; // Массив для хранения данных фотографий

photoUpload.addEventListener('change', function(event) {
    const files = event.target.files;
    for (let i = 0; i < files.length; i++) {
        const file = files[i];
        const reader = new FileReader();
        reader.onload = function(e) {
            const img = document.createElement('img');
            img.src = e.target.result;
            img.className = 'photo-preview';
            photosContainer.appendChild(img);

            uploadedPhotos.push({
                name: file.name,
                data: e.target.result.split(',')[1]
            });
        };
        reader.readAsDataURL(file);
    }
});

async function saveNote() {
    const title = document.querySelector('.note-title').value;
    const description = document.querySelector('.note-description').value;

    const data = {
        title: title,
        description: description,
        photos: uploadedPhotos
    };

    try {
        const response = await fetch('/save_note', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
    } catch (error) {
        console.error('Ошибка:', error);
        alert('Произошла ошибка при отправке данных');
    }
}