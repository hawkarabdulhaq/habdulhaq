/* Set the default font to Courier for both themes */
* {
    font-family: "Courier", monospace;
}

/* Light theme styles */
:root {
    --bg-color: #FFFFFF;
    --text-color: #2C3E50;
    --section-title-color: #34495E;
    --highlight-color: #1ABC9C;
    --border-color: #34495E;
}

/* Dark theme styles */
@media (prefers-color-scheme: dark) {
    :root {
        --bg-color: #1E1E1E;
        --text-color: #F0F0F0;
        --section-title-color: #F0F0F0;
        --highlight-color: #4DC9B2;
        --border-color: #4DC9B2;
    }
}

/* Apply background and text color for body */
body {
    background-color: var(--bg-color);
    color: var(--text-color);
}

/* Styling the title */
.title {
    font-size: 2.5em;
    font-weight: bold;
    color: var(--text-color);
    text-align: center;
    margin-top: 20px;
    margin-bottom: 20px;
}

/* Styling for section titles */
.section-title {
    font-size: 1.7em;
    font-weight: bold;
    color: var(--section-title-color);
    margin-top: 30px;
    margin-bottom: 10px;
    border-bottom: 2px solid var(--border-color);
    padding-bottom: 5px;
}

/* General content styling */
.content {
    font-size: 1.1em;
    color: var(--text-color);
    line-height: 1.6;
    text-align: justify;
    margin-bottom: 20px;
}

/* Highlighting important sections */
.highlight {
    font-weight: bold;
    color: var(--highlight-color);
}

/* Style for video container */
.video-container {
    text-align: center;
    margin-top: 20px;
    margin-bottom: 20px;
    background-color: var(--bg-color); /* Ensure consistent background */
    padding: 10px;
    border-radius: 8px;
}

/* Adjust YouTube video iframe for better dark mode contrast */
iframe {
    border: 2px solid var(--border-color);
    border-radius: 8px;
}
