// scroll button
function scrollToTop(){
    window.scrollTo({top: 0, behavior: 'smooth'})
}

window.onscroll = function (){
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop){
        document.getElementById('nav-btn').style.display = 'block';
    } else{
        document.getElementById('nav-btn').style.display = 'none';
    }
};

document.getElementById('nav-btn').addEventListener('click', scrollToTop);

// image animation

var images = ["img1.png", "img3.png", "bg4.jpg", "bg3.jpg"];
var currentImageIndex = 0;
var carouselElement = document.getElementById('hero-img');

function changeImage() {
    carouselElement.style.opacity = 0;
    setTimeout(function (){
        carouselElement.src = images[currentImageIndex];
        carouselElement.style.opacity = 1;   
    }, 200)
    currentImageIndex = (currentImageIndex + 1) % images.length;
}

setInterval(changeImage, 4000)