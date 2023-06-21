// JavaScript code to enable sliding functionality
const sliderContainer = document.querySelector('.slider-container');
const slides = document.querySelectorAll('.slide');
const slideWidth = slides[0].offsetWidth;

function slideNext() {
  sliderContainer.style.transform = `translateX(-${slideWidth}px)`;
  sliderContainer.appendChild(slides[0]);
}

function slidePrev() {
  sliderContainer.insertBefore(slides[slides.length - 1], slides[0]);
  sliderContainer.style.transform = `translateX(-${slideWidth}px)`;
  setTimeout(() => {
    sliderContainer.style.transform = 'translateX(0)';
  }, 10);
}

// Add event listeners for next and previous buttons
document.querySelector('.next-button').addEventListener('click', slideNext);
document.querySelector('.prev-button').addEventListener('click', slidePrev);
