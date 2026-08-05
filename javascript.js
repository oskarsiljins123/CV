const navTitle = document.getElementById("page_title");

window.addEventListener("scroll", () => {
        const scrollY = window.scrollY;

        if (scrollY < 500) {
            navTitle.textContent = "Home";
        } else if (scrollY < 1000) {
            navTitle.textContent = "Brief Description";
        } else if (scrollY < 1500) {
            navTitle.textContent = "Education";
        } else if (scrollY < 2000) {
            navTitle.textContent = "Work Experience";
        }
          else if (scrollY < 2500) {
            navTitle.textContent = "Skills";
        }
        else if (scrollY < 3000) {
            navTitle.textContent = "Projects";
        }
    });
const button = document.querySelector(".btn");
const menu = document.querySelector(".menu");
const sections = document.querySelectorAll("section");
const bookmark = document.querySelector(".bookmark")

button.addEventListener("click", () => {
    menu.classList.toggle("active");
    bookmark.classList.toggle("active")

    if (menu.classList.contains("active")) {
        button.textContent = "✕";

        sections.forEach(section => {
            section.style.paddingRight = "25%";
        });

    } else {
        button.textContent = "☰";

        sections.forEach(section => {
            section.style.paddingRight = "0";
        });
    }
});