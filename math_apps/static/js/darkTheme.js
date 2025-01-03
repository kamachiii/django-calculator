let docElement = document.documentElement
        let icon = document.getElementById('theme-toggler')
        const colorMode = window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";

        function updateTheme() {
            document.querySelector("html").setAttribute("data-bs-theme", colorMode);
            if (colorMode == 'dark') {
                icon.classList.remove('fa-moon')
                icon.classList.add('fa-sun')
            }
            document.body.style.transition = 'background-color 0.5s, color 0.5s';
          }

          // Set theme on load
          updateTheme()

          function toggleTheme() {
            const currentTheme = document.querySelector("html").getAttribute("data-bs-theme");
            const newTheme = currentTheme === "dark" ? "light" : "dark";
            document.querySelector("html").setAttribute("data-bs-theme", newTheme);
            if (newTheme == 'dark') {
              icon.classList.remove('fa-moon')
              icon.classList.add('fa-sun')
            } else {
              icon.classList.remove('fa-sun')
              icon.classList.add('fa-moon')
            }
          }
