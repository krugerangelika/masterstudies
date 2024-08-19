import React from "react";
import Button from "@mui/material/Button";

function MaterialButton(props) {
    return (
        <Button variant={props.variant} color={props.color} onClick={props.onClick}>
            {props.label}
        </Button>
    );
}

export default MaterialButton;
