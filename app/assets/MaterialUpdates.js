import React from "react";
import { Card, CardContent, Typography, Divider } from "@mui/material";

function MaterialUpdates({ updates }) {
    return (
        <div style={{ padding: '20px', maxWidth: '800px', margin: 'auto' }}>
            {updates.map((update, index) => (
                <Card key={index} variant="outlined" style={{ marginBottom: "20px" }}>
                    <CardContent>
                        <Typography variant="h5" component="div">
                            {update.title}
                        </Typography>
                        <Typography variant="body2" color="text.secondary">
                            {update.content}
                        </Typography>
                        <Divider style={{ margin: "10px 0" }} />
                        <Typography variant="caption" color="text.secondary">
                            Data: {update.date}
                        </Typography>
                    </CardContent>
                </Card>
            ))}
        </div>
    );
}

export default MaterialUpdates;
