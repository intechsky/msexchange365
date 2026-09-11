// Create the website using JavaScript

document.body.style.margin = "0";
document.body.style.fontFamily = "Arial, sans-serif";

// Header
const header = document.createElement("header");
header.style.background = "#1e293b";
header.style.color = "white";
header.style.padding = "20px";
header.style.display = "flex";
header.style.justifyContent = "space-between";

const logo = document.createElement("h2");
logo.innerText = "MyWebsite";

const nav = document.createElement("nav");
nav.innerHTML = `
<a href="#" style="color:white;margin-right:20px;text-decoration:none;">Home</a>

<a href="#" style="color:white;text-decoration:none;">Contact</a>
`;

header.appendChild(logo);
header.appendChild(nav);
document.body.appendChild(header);

// Hero Section
const hero = document.createElement("section");
hero.style.height = "80vh";
hero.style.display = "flex";
hero.style.flexDirection = "column";
hero.style.justifyContent = "center";
hero.style.alignItems = "center";
hero.style.background = "#0ea5e9";
hero.style.color = "white";

hero.innerHTML = `
<h1 style="font-size:50px;">Welcome to My Website</h1>
<p style="font-size:20px;">A website created completely with JavaScript.</p>
<button id="btn" style="padding:12px 30px;font-size:18px;border:none;border-radius:5px;cursor:pointer;">
Click Me
</button>
`;

document.body.appendChild(hero);

// Services
const services = document.createElement("section");
services.style.padding = "50px";
services.style.textAlign = "center";

services.innerHTML = `
<h2>Our Services</h2>

<div style="display:flex;justify-content:center;gap:20px;flex-wrap:wrap;margin-top:30px;">

<div style="width:250px;padding:20px;background:#f1f5f9;border-radius:10px;">
<h3>Web Development</h3>
<p>Modern responsive websites.</p>
</div>

<div style="width:250px;padding:20px;background:#f1f5f9;border-radius:10px;">
<h3>UI/UX Design</h3>
<p>Beautiful user interfaces.</p>
</div>

<div style="width:250px;padding:20px;background:#f1f5f9;border-radius:10px;">
<h3>SEO</h3>
<p>Improve your search rankings.</p>
</div>

</div>
`;

document.body.appendChild(services);

// Footer
const footer = document.createElement("footer");
footer.style.background = "#1e293b";
footer.style.color = "white";
footer.style.textAlign = "center";
footer.style.padding = "20px";
footer.innerHTML = "© 2026 MyWebsite. All Rights Reserved.";

document.body.appendChild(footer);

// Button Event
document.getElementById("btn").addEventListener("click", () => {
    alert("Thanks for visiting my website!");
});
