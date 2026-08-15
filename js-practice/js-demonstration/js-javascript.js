//folower inside the div
const parent = document.querySelector(".folowing-div");
const folower = document.querySelector(".folower");

parent.addEventListener("mousemove", (event) => {
    const rect = parent.getBoundingClientRect();

    folower.style.left = (event.clientX - rect.left) + "px";
    folower.style.top = (event.clientY - rect.top) + "px";

    if (event.clientY >= rect.height){
        folower.classList.toggle("out")
    }
});
//folower outside the div
const eye = document.querySelector(".eye");
const pupil = document.querySelector(".pupil");

document.addEventListener("mousemove", (event) => {
    const rect = eye.getBoundingClientRect();

    let x = event.clientX - rect.left;
    let y = event.clientY - rect.top;

    const maxX = rect.width - pupil.offsetWidth;
    const maxY = rect.height - pupil.offsetHeight;

    x = Math.max(0, Math.min(x, maxX));
    y = Math.max(0, Math.min(y, maxY));

    pupil.style.left = x + "px";
    pupil.style.top = y + "px";
});
//switch
const toggle = document.querySelector("#switch");
const theme = document.querySelector("#theme");

toggle.addEventListener("click", () => {
    toggle.classList.toggle("on");
    theme.classList.toggle("on");
});
//trail

document.addEventListener("mousemove", (event) => {
    const trailArea = document.querySelector(".trail");
    const rect2 = trailArea.getBoundingClientRect();
    let xtrail = event.clientX - rect2.left;
    let ytrail = event.clientY - rect2.top;
        if (xtrail >= 0 && ytrail >= 0 && ytrail <= rect2.height) 
        {
        const mousetrail = document.createElement("div");

        mousetrail.classList.add("mousetrail");

        mousetrail.style.left = xtrail + "px";
        mousetrail.style.top = ytrail + "px";

        trailArea.appendChild(mousetrail);

        setTimeout(() => {
            mousetrail.remove();
        }, 1000);
    }
});

//sides changing color
const left = document.querySelector("#left");
const right = document.querySelector("#right");

document.addEventListener("mousemove", (event) => {

    const rectleft = left.getBoundingClientRect();
    const rectright = right.getBoundingClientRect();

    const mouseInLeft =
        event.clientX >= rectleft.left &&
        event.clientX <= rectleft.right &&
        event.clientY >= rectleft.top &&
        event.clientY <= rectleft.bottom;

    const mouseInRight =
        event.clientX >= rectright.left &&
        event.clientX <= rectright.right &&
        event.clientY >= rectright.top &&
        event.clientY <= rectright.bottom;


    if (mouseInLeft) {
        left.classList.add("on");
        right.classList.remove("on");
    }
    else if (mouseInRight) {
        right.classList.add("on");
        left.classList.remove("on");
    }
    else {
        left.classList.remove("on");
        right.classList.remove("on");
    }
});
//hold
const holdingtext = document.querySelector(".holdingtext");
const hold = document.querySelector(".hold")


document.addEventListener("mousedown", (event) => {
    if (event.button === 0) {
        holdingtext.textContent = "release the left mouse button";
        hold.classList.add("on")
    }
});

document.addEventListener("mouseup", (event) => {
    if (event.button === 0) {
        holdingtext.textContent = "hold the left mouse button";
        hold.classList.remove("on")
    }
});
//resolution
const restext = document.querySelector(".mode");

function checkMode() {
    if (window.innerHeight > window.innerWidth) {
        restext.textContent = ":vertical mode";
    } else {
        restext.textContent = ":horizontal mode";
    }
}

checkMode();

window.addEventListener("resize", checkMode);