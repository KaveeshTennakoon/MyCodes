<script>
    document.addEventListener('DOMContentLoaded', function () {
        // Get all section elements
        const sections = document.querySelectorAll('.section');

        // Listen for scroll events
        document.addEventListener('scroll', function () {
            let currentSection = '';

            // Find the section currently in view
            sections.forEach(section => {
                const sectionTop = section.offsetTop;
                const sectionBottom = sectionTop + section.clientHeight;

                if (window.scrollY >= sectionTop && window.scrollY < sectionBottom) {
                    currentSection = section.id;
                }
            });

            // Apply different classes to the body based on the current section
            document.body.className = '';
            if (currentSection) {
                document.body.classList.add(currentSection);
            }
        });
    });
</script>
