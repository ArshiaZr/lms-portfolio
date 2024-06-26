setInterval(controlSlider, 5000);

const slider = document.querySelector(".wrapper");
const sliderItems = document.querySelectorAll(".hobbyWrapper");
const sliderLength = sliderItems.length;
const sliderWidth = sliderItems[0].clientWidth;

let index = 0;

function controlSlider() {
  index++;
  if (index === sliderLength) {
    index = 0;
  }
  slider.style.transform = `translateX(-${index * sliderWidth}px)`;
}
