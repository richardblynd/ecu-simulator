import socket

PORT = 35000

def golf_mqb_final_fix():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('0.0.0.0', PORT))
        s.listen(1)
        print(f"Golf MK7 MQB Simulator - waiting connection on 10.0.2.2:{PORT}")
        
        conn, addr = s.accept()
        with conn:
            conn.send(b"ELM327 v2.1\r\r>")
            
            while True:
                data = conn.recv(1024)
                if not data: break
                
                raw_input = data.decode().strip().replace(" ", "").upper()
                print(f"APP -> {raw_input}")

                if raw_input.startswith("AT"):
                    resp = b"OK"
                
                elif raw_input == "0100":
                    resp = b"7E8 06 41 00 BE 1F B8 11"
                
                # temperature before throttle
                elif "2215C1" in raw_input:
                    resp = b"7E8 04 62 15 C1 73"
                
                # oil temperature
                elif "2211BD" in raw_input:
                    resp = b"7E8 05 62 11 BD 0E 93"

                # fuel temperature
                elif "22128A" in raw_input:
                    resp = b"7E8 04 62 12 8A C5"

                # coolant temperature radiator outlet
                elif "2215CD" in raw_input:
                    resp = b"7E8 05 62 15 CD 0E 93"

                # boost pressure regulator commanded
                elif "2211A3" in raw_input:
                    resp = b"7E8 05 62 11 A3 CC 50"

                # boost pressure commanded (hpa)
                elif "2211F1" in raw_input:
                    resp = b"7E8 05 62 11 F1 7D 00"

                else:
                    resp = b"OK"

                conn.send(resp + b"\r\r>")

                if resp:
                    print(f"SIM -> {resp.decode().strip()}")

golf_mqb_final_fix()