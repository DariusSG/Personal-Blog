let currentlyActiveToc = "";
window.addEventListener('DOMContentLoaded', () => {
    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            const id = entry.target.getAttribute("id");
            if (entry.isIntersecting) {
                if (currentlyActiveToc !== "") {
                    document.querySelector(`div[class="markdown_toc"] li a[href="#${currentlyActiveToc}"]`).parentElement.classList.remove('active');
                }
                currentlyActiveToc = id;
                document.querySelector(`div[class="markdown_toc"] li a[href="#${id}"]`).parentElement.classList.add('active');
            }
        });
    });

    // Track all sections that have an `id` applied
    document
        .querySelectorAll(".markdown h2[id], .markdown h3[id]")
        .forEach(section => {
            observer.observe(section);
        });
});