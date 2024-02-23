from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.auth import Oauth2Proxy
from diagrams.onprem.ci import GitlabCI
from diagrams.onprem.client import Client, Users
from diagrams.onprem.container import Docker
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.vcs import Github
from diagrams.onprem.network import Nginx
from diagrams.programming.framework import FastAPI
from diagrams.programming.language import Go


with Diagram(name="Solution Architecture", show=False):
    ingress = Nginx("Reverse Proxy")
    devops_admin = Client("Developer")
    users = Users("External Users")

    with Cluster("Containerized Web Services"):
        fast_api = FastAPI("FastAPI App")
        go_service = Go("Go App")

    with Cluster("Containerized Database"):
        db = PostgreSQL("App DB")

    with Cluster("Containerized Auth"):
        auth = Oauth2Proxy("auth2-proxy")
        oauth_provider = Github("OAuth2 Provider")

    with Cluster("AWS EC2"):
        ci_server = GitlabCI("Gitlab Server")
        ci_runner = Docker("Gitlab Runner")

    fast_api << ingress
    go_service << ingress

    auth >> Edge(label="Start OAuth Flow") >> ingress
    ingress >> Edge(label="Set Auth Cookie") >> auth
    auth >> Edge(label="Request Auth") >> oauth_provider

    fast_api >> db
    db >> fast_api

    ci_runner >> Edge(label="Run Jobs") >> ci_server

    devops_admin >> Edge(label="Push To") >> ci_server

    users >> ingress

