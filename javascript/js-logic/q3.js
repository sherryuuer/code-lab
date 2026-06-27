// Question 3: Write a function that converts HEX to RGB. Then Make that function auto-dect the formats so that if you enter HEX color format it returns RGB and if you enter RGB color format it returns HEX.
function convertColorFormat(color) {
    // Check if the input color is in HEX format (#RRGGBB)
    if (/^#([0-9a-f]{3}){1,2}$/i.test(color)) {
        return hexToRgb(color);
    }

    // Check if the input color is in RGB format (rgb(r, g, b))
    if (/^rgb\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)$/i.test(color)) {
        return rgbToHex(color);
    }

    // If the format is not recognized, return null or handle it as needed
    return null;
}

function hexToRgb(hex) {
    hex = hex.replace(/^#/, '');
    const bigint = parseInt(hex, 16);
    const r = (bigint >> 16) & 255;
    const g = (bigint >> 8) & 255;
    const b = bigint & 255;
    return { r, g, b };
}

function rgbToHex(rgb) {
    const match = rgb.match(/^rgb\((\d+),\s*(\d+),\s*(\d+)\)$/);
    if (!match) {
        return null;
    }
    const r = parseInt(match[1]);
    const g = parseInt(match[2]);
    const b = parseInt(match[3]);
    return `#${(1 << 24 | r << 16 | g << 8 | b).toString(16).slice(1)}`;
}

// Example usage:
const hexColor = "#1a2b3c";
const rgbColor = "rgb(26, 43, 60)";

const convertedHex = convertColorFormat(hexColor);
const convertedRgb = convertColorFormat(rgbColor);

console.log(`HEX to RGB: ${convertedHex.r}, ${convertedHex.g}, ${convertedHex.b}`);
console.log(`RGB to HEX: ${convertedRgb}`);
