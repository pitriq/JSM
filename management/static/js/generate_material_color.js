function pickRandomProperty(obj) {
    var result;
    var count = 0;
    for (var prop in obj)
        if (Math.random() < 1 / ++count)
            result = prop;
    return result;
}

function materialColor() {
    // colors from https://github.com/egoist/color-lib/blob/master/color.json
    var colors = {
        "red": {
            "50": "#ffebee",
            "100": "#ffcdd2",
            "200": "#ef9a9a",
            "300": "#e57373",
            "400": "#ef5350",
            "500": "#f44336",
        },
        "pink": {
            "50": "#fce4ec",
            "100": "#f8bbd0",
            "200": "#f48fb1",
            "300": "#f06292",
            "400": "#ec407a",
            "500": "#e91e63",
        },
        "purple": {
            "50": "#f3e5f5",
            "100": "#e1bee7",
            "200": "#ce93d8",
            "300": "#ba68c8",
            "400": "#ab47bc",
            "500": "#9c27b0",
        },
        "deepPurple": {
            "50": "#ede7f6",
            "100": "#d1c4e9",
            "200": "#b39ddb",
            "300": "#9575cd",
            "400": "#7e57c2",
            "500": "#673ab7",
        },
        "indigo": {
            "50": "#e8eaf6",
            "100": "#c5cae9",
            "200": "#9fa8da",
            "300": "#7986cb",
            "400": "#5c6bc0",
            "500": "#3f51b5",
        },
        "blue": {
            "50": "#e3f2fd",
            "100": "#bbdefb",
            "200": "#90caf9",
            "300": "#64b5f6",
            "400": "#42a5f5",
            "500": "#2196f3",
        },
        "lightBlue": {
            "50": "#e1f5fe",
            "100": "#b3e5fc",
            "200": "#81d4fa",
            "300": "#4fc3f7",
            "400": "#29b6f6",
            "500": "#03a9f4",
        },
        "cyan": {
            "50": "#e0f7fa",
            "100": "#b2ebf2",
            "200": "#80deea",
            "300": "#4dd0e1",
            "400": "#26c6da",
            "500": "#00bcd4",
        },
        "teal": {
            "50": "#e0f2f1",
            "100": "#b2dfdb",
            "200": "#80cbc4",
            "300": "#4db6ac",
            "400": "#26a69a",
            "500": "#009688",
        },
        "green": {
            "50": "#e8f5e9",
            "100": "#c8e6c9",
            "200": "#a5d6a7",
            "300": "#81c784",
            "400": "#66bb6a",
            "500": "#4caf50",
        },
        "lightGreen": {
            "50": "#f1f8e9",
            "100": "#dcedc8",
            "200": "#c5e1a5",
            "300": "#aed581",
            "400": "#9ccc65",
            "500": "#8bc34a",
        },
        "lime": {
            "50": "#f9fbe7",
            "100": "#f0f4c3",
            "200": "#e6ee9c",
            "300": "#dce775",
            "400": "#d4e157",
            "500": "#cddc39",
        },
        "yellow": {
            "50": "#fffde7",
            "100": "#fff9c4",
            "200": "#fff59d",
            "300": "#fff176",
            "400": "#ffee58",
            "500": "#ffeb3b",
        },
        "amber": {
            "50": "#fff8e1",
            "100": "#ffecb3",
            "200": "#ffe082",
            "300": "#ffd54f",
            "400": "#ffca28",
            "500": "#ffc107",
        },
        "orange": {
            "50": "#fff3e0",
            "100": "#ffe0b2",
            "200": "#ffcc80",
            "300": "#ffb74d",
            "400": "#ffa726",
            "500": "#ff9800",
        },
        "deepOrange": {
            "50": "#fbe9e7",
            "100": "#ffccbc",
            "200": "#ffab91",
            "300": "#ff8a65",
            "400": "#ff7043",
            "500": "#ff5722",
        },
        "brown": {
            "50": "#efebe9",
            "100": "#d7ccc8",
            "200": "#bcaaa4",
            "300": "#a1887f",
            "400": "#8d6e63",
            "500": "#795548",
        },
        "grey": {
            "50": "#fafafa",
            "100": "#f5f5f5",
            "200": "#eeeeee",
            "300": "#e0e0e0",
            "400": "#bdbdbd",
            "500": "#9e9e9e",
        },
        "blueGrey": {
            "50": "#eceff1",
            "100": "#cfd8dc",
            "200": "#b0bec5",
            "300": "#90a4ae",
            "400": "#78909c",
            "500": "#607d8b",
        },
    }
    // pick random property
    var colorList = colors[pickRandomProperty(colors)];
    var newColorKey = pickRandomProperty(colorList);
    var newColor = colorList[newColorKey];
    return newColor;
}