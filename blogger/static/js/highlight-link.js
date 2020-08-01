window.onload = function() {
    const path = window.location.pathname;
    if (path.split("/")[1] == "") {
        document.getElementById("index").classList.add("current-link");
    } else if (path.split("/")[1] == "blog") {
        document.getElementById("blog").classList.add("current-link");
    } else if (path.split("/")[1] == "about") {
        document.getElementById("about").classList.add("current-link");
    } else if (path.split("/")[1] == "contact") {
        document.getElementById("contact").classList.add("current-link");
    }
};