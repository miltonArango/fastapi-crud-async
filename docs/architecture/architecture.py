from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.analytics import Spark
from diagrams.onprem.auth import Oauth2Proxy
from diagrams.onprem.ci import GitlabCI
from diagrams.onprem.client import Client
from diagrams.onprem.compute import Server
from diagrams.onprem.container import Docker
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.vcs import Github
from diagrams.onprem.network import Nginx

with Diagram(name="Solution Architecture", show=False):
    ingress = Nginx("ingress")
    devops_admin = Client("Developer")

    with Cluster("Web Services"):
        fast_api = Docker("FastAPI App")
        go_service = Docker("Go App")

    with Cluster("Database"):
        db = PostgreSQL("fastapi db")

    with Cluster("Auth"):
        auth = Oauth2Proxy("auth2-proxy")
        oauth_provider = Github("OAuth2 Provider")

    with Cluster("AWS EC2"):
        ci_server = GitlabCI("Gitlab Server")
        ci_runner = Docker("Gitlab Runner")

    fast_api << ingress
    go_service << ingress

    auth >> Edge(label="Start OAuth Flow") >> ingress
    ingress >> Edge(label="Set Auth Cookie") >> auth
    auth >> Edge(label="OAuth Provider") >> oauth_provider

    fast_api >> db
    db >> fast_api

    ci_runner >> Edge(label="run jobs") >> ci_server

    devops_admin >> Edge(label="pushes") >> ci_server

