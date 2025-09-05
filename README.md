# Your-Chat
<img src="https://raw.githubusercontent.com/NewDevOrgin/your-chat/main/Your-Chat.png" width="128"/> 
Your-chat is a simple chat app using websockets, I made it for educational purposes. Your-Chat has no other function other than real-time chatting function (On your network).

# How does the server work?
The server has 2 main functions, one to send all the messages to the client when requested and one to handle new messages. When a client makes a connection with the server it responds with all the messages which is stored in a json file handled by TinyDB. When a new message is sent it stores it in **messages.json** file.

# How does the client work?
The client relies on nicegui which opens in the browser but can be a native window. The client is always recving messages even when the messages are the same so it will be an immediate update and also sends immediate messages, but this is on local host, I will attempt to host the server somewhere after I update it a bit.
