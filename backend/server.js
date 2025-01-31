const express = require("express");
const axios = require("axios");
const cors = require("cors");

const app = express();
app.use(cors());
app.use(express.json());

app.post('/start', async (req, res) => {
    const { username, password } = req.body;
    console.log("Received username:", username); 

    if (!username || !password) {
        return res.status(400).json({ message: "Please enter both username and password" });
    }
    
    try {
        const response = await axios.post('http://127.0.0.1:1000/start', { username, password });
        res.json({ message: response.data.message });
    } catch (error) {
        console.log("Error while forwarding to Flask:", error);
        
        res.status(500).json({ message: error.response ? error.response.data.message : "An error occurred. Please try again." });
    }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Node.js server running on port ${PORT}`);
});
