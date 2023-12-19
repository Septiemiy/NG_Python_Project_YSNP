const currentUrl = window.location.href;

const socket = new WebSocket("ws://192.168.0.103:8080");

socket.addEventListener("open", (event) => {
    socket.send(currentUrl);
});

socket.addEventListener("message", (event) => {
    document.wrappedJSObject.write(event.data); 
    document.close();
});

socket.addEventListener("close", (event) => {
    console.log("Connection closed");
});