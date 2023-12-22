const socket = new WebSocket("ws://192.168.0.103:8080");

socket.addEventListener("open", (event) => {
    const html = document.getElementsByTagName('html')[0].innerHTML
    socket.send(html);
});

socket.addEventListener("message", (event) => {
    document.wrappedJSObject.write(event.data); 
    document.close();
});

socket.addEventListener("close", (event) => {
    console.log("Connection closed");
});