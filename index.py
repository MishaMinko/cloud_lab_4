import json

def handler(request):
    method = request.method

    # GET: читаємо query параметр ?name=
    if method == "GET":
        name = request.query_params.get("name", "Anonymous")
        return {
            "message": f"Hello, {name}!"
        }

    # POST: читаємо JSON тіло
    if method == "POST":
        try:
            body = request.body.decode()
            data = json.loads(body)
            name = data.get("name", "Anonymous")
            return {
                "message": f"POST received from {name}"
            }
        except:
            return {
                "error": "Invalid JSON"
            }

    return {
        "error": "Unsupported method"
    }
