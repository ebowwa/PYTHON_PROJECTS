const openApiSpec = {
  openapi: "3.0.0",
  info: {
    title: "Simple API",
    version: "1.0.0",
    description: "A basic API for demonstration purposes"
  },
  servers: [
    {
      url: "https://your-server-url.com/api/",
      description: "Primary server"
    }
  ],
  paths: {
    "/hello": {
      "get": {
        "summary": "Hello World",
        "operationId": "getHelloWorld",
        "responses": {
          "200": {
            "description": "Returns a Hello World message",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "message": {
                      "type": "string",
                      "example": "Hello, World!"
                    }
                  }
                }
              }
            }
          },
          "500": {
            "description": "Internal Server Error"
          }
        }
      }
    }
  }
};

export default function handler(req, res) {
  if (req.method === 'GET' && req.url === '/api/hello') {
    res.status(200).json({ message: "Hello, World!" });
  } else {
    res.status(404).send('Not Found');
  }
}
