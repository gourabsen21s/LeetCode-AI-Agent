document.getElementById("login-form").addEventListener("submit", function(event) {
    event.preventDefault();

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    document.getElementById("status").innerText = "Logging in and starting automation... Please wait.";

    axios.post('http://localhost:3000/start', { username, password })
        .then(function (response) {
            if (response.data.message) {
                document.getElementById("status").innerText = response.data.message;
            } else {
                document.getElementById("status").innerText = "Something went wrong. Please try again.";
            }
        })
        .catch(function (error) {
            console.error('Error:', error);
            document.getElementById("status").innerText = "An error occurred. Please try again.";
        });
});
