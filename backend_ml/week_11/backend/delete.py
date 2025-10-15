from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# database
data = [
    {
        "id": 1,
        "name": "Sam Larry",
        "track": "AI Developer"
    },
    {
        "id": 2,
        "name": "Wole Tunji",
        "track": "Backend Developer"
    }
]

class BaseAPI(BaseHTTPRequestHandler):
    def send_data(self, payload, status = 200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(payload).encode())

    # PUT methods to update data
    def do_DELETE(self):
        content_size = int(self.headers.get("content-length", 0))
        put_data = self.rfile.read(content_size)
        remove_data = json.loads(put_data)
        user_id = remove_data.get("id") # Extracting the id from the data sent

        for record in data:
            if record["id"] == user_id:
                data.remove(record)
                self.send_data({
                    "message": "Record removed successfully",
                    "data": record
                })
                return
            
        # If record not found
        self.send_data({"error":"record not found"}, status=404)

def run():
    HTTPServer(('localhost', 8000), BaseAPI).serve_forever()

print("Application running....")
run()