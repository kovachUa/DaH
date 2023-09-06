document.addEventListener("DOMContentLoaded", function () {
    const fileInput = document.getElementById("fileInput");
    const showContentButton = document.getElementById("showContentButton");
    const fileList = document.getElementById("fileList");

    showContentButton.addEventListener("click", function () {
        fileList.innerHTML = ""; // Очищаємо попередній список

        const entries = fileInput.files[0].webkitEntries;
        if (entries) {
            displayEntries(entries, fileList);
        }
    });

    function displayEntries(entries, parentElement) {
        entries.forEach((entry) => {
            const listItem = document.createElement("li");
            listItem.textContent = entry.name;
            parentElement.appendChild(listItem);

            if (entry.isDirectory) {
                const reader = entry.createReader();
                reader.readEntries((subEntries) => {
                    const subList = document.createElement("ul");
                    listItem.appendChild(subList);
                    displayEntries(subEntries, subList);
                });
            }
        });
    }
});
