window.onload = function() {
    const menuIconContainer = document.querySelector(".gn-header .menu-icon-container");
    const navContainer = document.querySelector(".nav-container");

    menuIconContainer.addEventListener("click", () => {
        navContainer.classList.toggle("active");
    })
}

