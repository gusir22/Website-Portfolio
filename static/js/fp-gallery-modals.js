function closeGalleryModal() {
    let overlay = document.getElementById("overlay")  // get overlay object
    overlay.style.display = "none";  // deactivate modal layout blackscreen

    overlay.innerHTML = "";  // delete modalHTML
}

function openGalleryModal (img) {
    let overlay = document.getElementById("overlay")  // get overlay object
    
    overlay.style.display = "block";  // activate modal layout blackscreen

    modalHTML = `
        <div id="gallery-modal">
            <div id="gallery-img-container">
                <img src="${img.src}" alt="${img.alt}" id="gallery-img">
            </div>
            <p id="gallery-modal-text">${img.alt}</p>
        </div>
    `;

    overlay.innerHTML = modalHTML;  // insert modalHTML into overlay innerHTML
    
}