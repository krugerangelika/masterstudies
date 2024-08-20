import React from "react";
import Button from "@mui/material/Button";

function MaterialButton(props) {
    const handleClick = () => {
        // Emitowanie niestandardowego zdarzenia
        const event = new CustomEvent('patient-registration-click', {
            detail: {
                // Możesz przekazać dodatkowe dane tutaj, jeśli potrzebujesz
                message: 'Patient registration button clicked'
            }
        });
        window.dispatchEvent(event);
    };

    return (
        <Button variant={props.variant} color={props.color} onClick={handleClick}>
            {props.label}
        </Button>
    );
}

export default MaterialButton;
