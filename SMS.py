import nexmo

client = nexmo.Clinet(key= 'ed320a43', secret ='OlUMCY1dswQYQ9FD',

client.send_message({
        "from": "Vonage APIs",
        "to": "447594594211",
        "text": "Hi Ali", 
})