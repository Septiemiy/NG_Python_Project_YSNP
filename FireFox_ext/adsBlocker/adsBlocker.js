const currentUrl = window.location.href;

const socket = new WebSocket("ws://localhost:8765");

socket.addEventListener("open", (event) => {
    socket.send(currentUrl);
});

socket.addEventListener("message", (event) => {
    console.log(`Message from server: ${event.data}`);
});

socket.addEventListener("close", (event) => {
    console.log("Connection closed");
});