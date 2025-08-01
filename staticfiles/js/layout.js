const burger_menu = document.getElementById("navbar-burger");
const navbar = document.getElementById("navbar");
const span1 = document.getElementById("span1");
const span2 = document.getElementById("span2");
const span3 = document.getElementById("span3");

let cooldown = false;
let open = false;

burger_menu.addEventListener("click", function () {
    if (cooldown) return;
    cooldown = true;

    if (!open) {
        navbar.style.display = "block";
        navbar.style.animation = "navbar-open ease 1s";
        span1.style.animation = "span1-open ease 1s";
        span2.style.animation = "span2-open ease 1s";
        span3.style.animation = "span3-open ease 1s";
        
        const onOpenEnd = () => {
            navbar.style.left = "0%";
            navbar.style.animation = "";

            span1.style.animation = "";
            span2.style.animation = "";
            span3.style.animation = "";

            span1.style.top = "14px";
            span2.style.opacity = "0";
            span3.style.top = "-14px";

            span1.style.rotate = "45deg";
            span3.style.rotate = "-45deg";
            open = true;
            cooldown = false;
            navbar.removeEventListener("animationend", onOpenEnd);
        };

        navbar.addEventListener("animationend", onOpenEnd);

    } else {
        navbar.style.animation = "navbar-close ease 1s";
        span1.style.animation = "span1-close ease 1s";
        span2.style.animation = "span2-close ease 1s";
        span3.style.animation = "span3-close ease 1s";

        const onCloseEnd = () => {
            navbar.style.left = "-100%";
            navbar.style.animation = "";
            navbar.style.display = "none";

            span1.style.animation = "";
            span2.style.animation = "";
            span3.style.animation = "";

            span1.style.top = "0px";
            span2.style.opacity = "1";
            span3.style.top = "0px";

            span1.style.rotate = "0deg";
            span3.style.rotate = "0deg";
            open = false;
            cooldown = false;
            navbar.removeEventListener("animationend", onCloseEnd);
        };

        navbar.addEventListener("animationend", onCloseEnd);
    }
});


mapboxgl.accessToken = 'pk.eyJ1IjoiaWFqYWlhbmkiLCJhIjoiY21kazdobnA2MHc2YjJpc2RkOXU1cXA3MCJ9.8AmyHL9M4JyllWDYFwohiw';


const map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v12',
    center: [41.7023, 41.6784],
    zoom: 15
});

// Create popup content with HTML for big and small text
const popupContent = `
    <div style="font-family: sans-serif;">
        <strong style="font-size: 16px;">Sun Wine Hotel</strong><br>
        <h1 style="font-size: 13px; color: #555;">მახინაჯაური, ახალგაზრდობის 22ა</h1>
        <a href="https://www.google.com/maps/place/Sun+Wine+Hotel/@41.6783983,41.6996034,17z/data=!3m1!4b1!4m9!3m8!1s0x406787277a3c813b:0xaaf1374149bbb950!5m2!4m1!1i2!8m2!3d41.6783943!4d41.7021837!16s%2Fg%2F11y7b5jxhk!5m1!1e2?entry=ttu&g_ep=EgoyMDI1MDcyMy4wIKXMDSoASAFQAw%3D%3D" target="_blank"
           style="display: block; width: calc(100% - 20px); font-family: 'Itim', cursive; font-size: small; padding: 10px; text-align: center; background-color: #eee; color: #000; text-decoration: none; border-radius: 6px; margin-top: 10px;">
           Visit Google maps
        </a>
    </div>
    <link href="https://fonts.googleapis.com/css2?family=Itim&display=swap" rel="stylesheet">
`;


const marker = new mapboxgl.Marker({ color: 'red' })
    .setLngLat([41.7023, 41.6784])
    .setPopup(new mapboxgl.Popup({ offset: 25 }).setHTML(popupContent))
    .addTo(map);

marker.getPopup().addTo(map);

window.scrollTo(0, document.body.scrollHeight);