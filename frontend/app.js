document.getElementById("login-form").addEventListener("submit", function(event) {
    event.preventDefault();

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    axios.post('/start', { username, password })
        .then(function (response) {
            document.getElementById("status").innerText = response.data.message;
        })
        .catch(function (error) {
            console.error('Error:', error);
            document.getElementById("status").innerText = "An error occurred. Please try again.";
        });
});
