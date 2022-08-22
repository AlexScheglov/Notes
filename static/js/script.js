

let ws = new WebSocket("ws://localhost:8000/ws");

ws.onmessage = function (event) {
    let messages = document.getElementById('messages')
    let message = document.createElement('p')
    let json_response = JSON.parse(event.data)
    let content = document.createTextNode(`${json_response.id}. ${json_response.message}`)
    message.appendChild(content)
    messages.appendChild(message)
};

function sendMessage(event) {
    let input = document.getElementById("messageText")
    ws.send(JSON.stringify({'message': input.value}))
    input.value = ''
    event.preventDefault()
}
