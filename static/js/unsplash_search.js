document.addEventListener("DOMContentLoaded", function () {
    const searchField = document.querySelector("#id_search_unsplash");
    const unsplashField = document.querySelector("#id_unsplash_image_url");
    const resultsContainer = document.createElement("div");
    resultsContainer.id = "unsplash-results";
    resultsContainer.style.display = "flex";
    resultsContainer.style.flexWrap = "wrap";
    resultsContainer.style.marginTop = "10px";
    searchField.parentNode.appendChild(resultsContainer);

    const fetchUnsplashResults = async (query) => {
        const response = await fetch(`/unsplash-search/?q=${query}`);
        if (response.ok) {
            const results = await response.json();
            displayResults(results);
        } else {
            console.error("Error fetching Unsplash results");
        }
    };

    const displayResults = (images) => {
        resultsContainer.innerHTML = ""; // Clear existing results
        images.forEach((image) => {
            const img = document.createElement("img");
            img.src = image.thumbnail;
            img.alt = image.description || "Unsplash Image";
            img.style.cursor = "pointer";
            img.style.margin = "5px";
            img.style.border = "2px solid transparent";
            img.style.width = "100px";
            img.style.height = "100px";

            img.addEventListener("click", () => {
                // Highlight the selected image
                Array.from(resultsContainer.children).forEach((child) => {
                    child.style.border = "2px solid transparent";
                });
                img.style.border = "2px solid #007bff";

                // Update the Unsplash image URL field
                unsplashField.value = image.url;
            });

            resultsContainer.appendChild(img);
        });
    };

    searchField.addEventListener("change", (e) => {
        const query = e.target.value.trim();
        if (query) {
            fetchUnsplashResults(query);
        } else {
            resultsContainer.innerHTML = ""; // Clear results if query is empty
        }
    });
});