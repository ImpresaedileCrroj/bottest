document.addEventListener("DOMContentLoaded", () => {
    // Select elements
    const fileInput = document.getElementById("file");
    const uploadForm = document.querySelector(".upload-section form");
    const flashMessagesContainer = document.querySelector(".flash-messages");
    const reportSection = document.querySelector(".report-section");
    const reportContainer = document.querySelector(".report-container");

    // Function to display flash messages
    function displayFlashMessage(message, type = "error") {
        if (flashMessagesContainer) {
            flashMessagesContainer.innerHTML = `
                <p class="${type === "success" ? "success-message" : "error-message"}">${message}</p>
            `;
            setTimeout(() => {
                flashMessagesContainer.innerHTML = "";
            }, 5000); // Clear message after 5 seconds
        }
    }

    // Drag-and-drop functionality
    uploadForm.addEventListener("dragover", (event) => {
        event.preventDefault();
        uploadForm.classList.add("drag-over");
    });

    uploadForm.addEventListener("dragleave", () => {
        uploadForm.classList.remove("drag-over");
    });

    uploadForm.addEventListener("drop", (event) => {
        event.preventDefault();
        uploadForm.classList.remove("drag-over");

        const files = event.dataTransfer.files;
        if (files.length > 0) {
            const file = files[0];
            if (file.type === "text/plain") {
                fileInput.files = files;
                uploadForm.classList.add("valid-file"); // Add visual feedback for valid file
                displayFlashMessage("File ready for upload. Click 'Upload' to proceed.", "success");
            } else {
                uploadForm.classList.add("invalid-file"); // Add visual feedback for invalid file
                displayFlashMessage("Invalid file type. Please upload a .txt file.");
            }
            setTimeout(() => {
                uploadForm.classList.remove("valid-file", "invalid-file"); // Remove feedback after 2 seconds
            }, 2000);
        }
    });

    // Dynamic report display
    function updateReportSection(reports) {
        if (reportContainer) {
            reportContainer.innerHTML = ""; // Clear existing reports

            if (Object.keys(reports).length === 0) {
                reportContainer.innerHTML = "<p>No reports available. Upload a file to generate a report.</p>";
                return;
            }

            for (const [month, stats] of Object.entries(reports)) {
                const reportCard = document.createElement("div");
                reportCard.classList.add("report-card");

                reportCard.innerHTML = `
                    <h3>${month}</h3>
                    <p><strong>Joined:</strong> ${stats.joined}</p>
                    <p><strong>Left:</strong> ${stats.left}</p>
                    <p><strong>Active Workers:</strong> ${stats.workers_count}</p>
                `;

                reportContainer.appendChild(reportCard);
            }
        }
    }

    // Example: Simulate dynamic report update (replace with actual API call if needed)
    const exampleReports = {
        "October 2023": { joined: 5, left: 2, workers_count: 3 },
        "November 2023": { joined: 3, left: 1, workers_count: 5 },
    };

    // Simulate report update after 2 seconds
    setTimeout(() => {
        updateReportSection(exampleReports);
    }, 2000);
});