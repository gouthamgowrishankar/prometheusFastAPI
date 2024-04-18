from fastapi import FastAPI
from prometheus_client import make_asgi_app, Counter
from prometheus_fastapi_instrumentator import Instrumentator

# Create app
app = FastAPI(debug=False)
Instrumentator().instrument(app).expose(app)
"""c = Counter('my_requests_total', 'HTTP Failures', ['method', 'endpoint'])
c.labels('get', '/').inc()
c.labels('post', '/submit').inc()"""
# Add prometheus asgi middleware to route /metrics requests
#metrics_app = make_asgi_app()
#app.mount("/metrics", metrics_app)

@app.get("/")
def root():
    return "Hello World"