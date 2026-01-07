import socket
from rpc_runtime import send_msg, recv_msg

# The actual functions to be called remotely
def add(a, b): return a + b
def multiply(a, b): return a * b

def handle_client(conn):
    while True:
        request = recv_msg(conn)
        if not request: break
        
        # Server Stub: Unmarshalling & Dispatching
        func_name = request.get("method")
        params = request.get("params")
        
        if func_name == "add":
            result = add(*params)
        elif func_name == "multiply":
            result = multiply(*params)
        
        send_msg(conn, {"result": result})
    conn.close()

# TODO: You must make this concurrent (Multi-threading)
