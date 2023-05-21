
    function showActiveLink(menu) {
        const pageURL = document.location.href;
        const links = document.getElementById(menu).querySelectorAll("a");
        for (const link of links) {
            if (link.href === pageURL) {
                    link.classList.add("active");
             }
        }
    }
    showActiveLink("menu");