const express = require("express");
const cors = require("cors");
const axios = require("axios");
const multer = require("multer");
const FormData = require("form-data");

const app = express();

app.use(cors());
app.use(express.json());

const upload = multer({
    storage: multer.memoryStorage()
});

app.get("/", (req, res) => {
    res.json({
        message: "AI Resume Intelligence API is running"
    });
});

app.get("/api/health", (req, res) => {
    res.json({
        status: "ok",
        service: "resume-intelligence-api"
    });
});

// Resume analysis API
app.post("/api/analyze", upload.single("resume"), async (req, res) => {
    try {
        if (!req.file) {
            return res.status(400).json({
                error: "Resume PDF is required"
            });
        }

        const jobDesc = req.body.job_desc;

        if (!jobDesc) {
            return res.status(400).json({
                error: "Job description is required"
            });
        }

        // Create form data for Flask
        const formData = new FormData();

        formData.append(
            "resume",
            req.file.buffer,
            {
                filename: req.file.originalname,
                contentType: req.file.mimetype
            }
        );

        formData.append("job_desc", jobDesc);

        // Send request to Python Flask AI backend
        const response = await axios.post(
            "http://127.0.0.1:10000/api/analyze",
            formData,
            {
                headers: formData.getHeaders()
            }
        );

        // Send Flask's AI result back to the frontend
        res.json(response.data);

    } catch (error) {
        console.error("Analysis error:", error.message);

        if (error.response) {
            return res.status(error.response.status).json(
                error.response.data
            );
        }

        res.status(500).json({
            error: "Failed to analyze resume"
        });
    }
});

const PORT = 5000;

app.listen(PORT, () => {
    console.log(`Node.js server running on http://localhost:${PORT}`);
});