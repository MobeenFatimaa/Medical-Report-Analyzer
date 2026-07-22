// Navbar

const navbar = document.querySelector(".navbar");

window.addEventListener("scroll",()=>{

if(window.scrollY>40){

navbar.classList.add("scrolled");

}else{

navbar.classList.remove("scrolled");

}

});

// Dashboard

const dashboard = document.querySelector(".medical-dashboard");

if(dashboard){

document.addEventListener("mousemove",(e)=>{

const x=(window.innerWidth/2-e.clientX)/45;

const y=(window.innerHeight/2-e.clientY)/45;

dashboard.style.transform=
`rotateY(${x}deg) rotateX(${-y}deg)`;

});

}

// Counters

const counters=document.querySelectorAll(".counter");

function startCounter(counter){

const target=Number(counter.dataset.target);

let current=0;

const increment=target/100;

function update(){

current+=increment;

if(current<target){

counter.textContent=Math.floor(current);

requestAnimationFrame(update);

}else{

if(target>=1000){

counter.textContent=target.toLocaleString()+"+";

}else if(target==98){

counter.textContent=target+"%";

}else if(target==5){

counter.textContent=target+"s";

}else{

counter.textContent=target;

}

}

}

update();

}

const observer=new IntersectionObserver((entries)=>{

entries.forEach(entry=>{

if(entry.isIntersecting){

startCounter(entry.target);

observer.unobserve(entry.target);

}

});

},{threshold:0.3});

counters.forEach(counter=>observer.observe(counter));
/*==============================
FAQ
==============================*/

const faqItems = document.querySelectorAll(".faq-item");

faqItems.forEach(item => {

    const question = item.querySelector(".faq-question");

    question.addEventListener("click", () => {

        faqItems.forEach(faq => {

            if(faq !== item){

                faq.classList.remove("active");

            }

        });

        item.classList.toggle("active");

    });

});
const uploadInput = document.getElementById("fileInput");
const fileName = document.getElementById("fileName");

if (uploadInput && fileName) {

    uploadInput.addEventListener("change", () => {

        if (uploadInput.files.length > 0) {

            fileName.textContent = uploadInput.files[0].name;

        }

    });

}
/*============================
SUCCESS POPUP
============================*/

const popup = document.getElementById("popup");
const closePopup = document.getElementById("closePopup");

const params = new URLSearchParams(window.location.search);

if(params.get("success") === "true"){

    popup.classList.add("show");

    window.history.replaceState({}, document.title, window.location.pathname);

}

if(closePopup){

closePopup.addEventListener("click",()=>{

popup.classList.remove("show");

});

}

if(popup){

popup.addEventListener("click",(e)=>{

if(e.target===popup){

popup.classList.remove("show");

}

});

}
