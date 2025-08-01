const div1 = document.getElementById("div1");
const div2 = document.getElementById("div2");
const div3 = document.getElementById("div3");

div1.addEventListener("mouseenter", function() {
    div1.style.animation = "div-mouse-overlap 0.2s ease";

    div1.addEventListener("animationend", function() {
        div1.style.animation = '';
        div1.style.transform = "scale(1.04)";
        div1.style.boxShadow = "0px 0px 25px gray";
    })

    div1.addEventListener("mouseleave", function() {
        div1.style.animation = "div-mouse-overlap2 0.2s ease";

        div1.addEventListener("animationend", function() {
            div1.style.animation = '';
            div1.style.transform = "scale(1)";
            div1.style.boxShadow = '';
        })
    })
});

div2.addEventListener("mouseenter", function() {
    div2.style.animation = "div-mouse-overlap 0.2s ease";

    div2.addEventListener("animationend", function() {
        div2.style.animation = '';
        div2.style.transform = "scale(1.04)";
        div2.style.boxShadow = "0px 0px 25px gray";
    })

    div2.addEventListener("mouseleave", function() {
        div2.style.animation = "div-mouse-overlap2 0.2s ease";

        div2.addEventListener("animationend", function() {
            div2.style.animation = '';
            div2.style.transform = "scale(1)";
            div2.style.boxShadow = '';
        })
    })
});

div3.addEventListener("mouseenter", function() {
    div3.style.animation = "div-mouse-overlap 0.2s ease";

    div3.addEventListener("animationend", function() {
        div3.style.animation = '';
        div3.style.transform = "scale(1.04)";
        div3.style.boxShadow = "0px 0px 25px gray";
    })

    div3.addEventListener("mouseleave", function() {
        div3.style.animation = "div-mouse-overlap2 0.2s ease";

        div3.addEventListener("animationend", function() {
            div3.style.animation = '';
            div3.style.transform = "scale(1)";
            div3.style.boxShadow = '';
        })
    })
});

document.addEventListener("DOMContentLoaded", function () {
    const textElements = [
        document.getElementById("landing1"),
        document.getElementById("landing2"),
        document.getElementById("landing3")
    ];
    const image = document.getElementById("landing4");

    // Animate all text elements together
    textElements.forEach(el => {
        el.style.animation = "landing-text 0.8s ease forwards";
    });

    // Animate image after texts finish
    setTimeout(() => {
        image.style.animation = "landing-image 1s ease forwards";
    }, 800);
});
