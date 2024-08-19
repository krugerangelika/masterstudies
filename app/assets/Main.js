import React from "react";
import ReactDOM from "react-dom";
import MaterialUpdates from "./MaterialUpdates";

// Przykład wykorzystania komponentu
const updates = [
    {
        title: "Zmiany w grafiku",
        content: "Grafik na najbliższy tydzień został zaktualizowany. Proszę sprawdzić swoje zmiany.",
        date: "2024-08-13 15:00"
    },
    {
        title: "Nowe procedury",
        content: "Od przyszłego tygodnia obowiązują nowe procedury dotyczące higieny na oddziale.",
        date: "2024-08-13 15:00"
    }
];

ReactDOM.render(
    <MaterialUpdates updates={updates} />,
    document.getElementById("updates-section")
);
