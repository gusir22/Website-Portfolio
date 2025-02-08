function handleMouseOver(container) {
    container.classList.add("fp-card-mouseover"); // add 45px of margin bottom for clear separation

    let img = container.querySelector(".fp-thumbnail");
    img.classList.add("fp-thumbnail-mouseover");  // Apply grayscale transition to color

    let title = container.querySelector(".fp-title");
    title.classList.add("fp-title-mouseover");  // Apply border-bottom transition

    let description = container.querySelector(".fp-description");
    description.classList.add("fp-description-mouseover");  // Reveal and slide in description

    let date = container.querySelector(".fp-date");
    date.classList.add("fp-date-mouseover");  // Reveal and slide in date

    let button1 = container.querySelector(".fp-btn");
    button1.classList.add("fp-btn-mouseover");  // Reveal and slide in button 1

    let button2 = container.querySelector(".fp-btn-secondary");
    button2.classList.add("fp-btn-secondary-mouseover");  // Reveal and slide in button 2

}

function handleMouseOut(container) {
    container.classList.remove("fp-card-mouseover");  // restore normal margin bottom

    let img = container.querySelector(".fp-thumbnail");
    img.classList.remove("fp-thumbnail-mouseover");  // Revert grayscale effect

    let title = container.querySelector(".fp-title");
    title.classList.remove("fp-title-mouseover");  // Remove the border from the title

    let description = container.querySelector(".fp-description");
    description.classList.remove("fp-description-mouseover");  // Slide and hide the description

    let date = container.querySelector(".fp-date");
    date.classList.remove("fp-date-mouseover");  // Slide and hide the date

    let button1 = container.querySelector(".fp-btn");
    button1.classList.remove("fp-btn-mouseover");  // Slide and hide the button 1

    let button2 = container.querySelector(".fp-btn-secondary");
    button2.classList.remove("fp-btn-secondary-mouseover");  // Slide and hide the button 2
}

