#!/usr/bin/python3
""""""
import socket
import json

def start_server(host='localhost', port=65432):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()
    print(f"Server listening on {host}:{port}")
    
    while True:
        conn, addr = server_socket.accept()
        print(f"Connected by {addr}")
        
        try:
            data = b""
            while True:
                part = conn.recv(1024)
                if not part:
                    break
                data += part
            
            received_dict = json.loads(data.decode('utf-8'))
            print("Received dictionary:", received_dict)
        
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            conn.close()
            print(f"Connection with {addr} closed")
