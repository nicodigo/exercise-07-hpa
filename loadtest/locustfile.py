# TODO: Locust load test
# from locust import HttpUser, task
# Hit /health and /api/nodes endpoints
from locust import HttpUser, between, task
from random import randint


class MiUsuario(HttpUser):
    wait_time = between(1, 3) # espera entre 1 y 3 segundos entre tasks

    @task(3)
    def get_nodes(self):
        self.client.get('/api/nodes')

    @task(5)
    def get_health(self):
        self.client.get('/health')

    @task(1)
    def post_node(self):
        host_counter = randint(1,254)
        self.client.post(
            '/api/nodes', 
            json={
                "name": f"node-{host_counter}",
                "host": f"10.0.0.{host_counter}",
                "port": 8000,
        },)
