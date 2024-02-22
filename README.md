<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/miltonarango">
    <img src="images/brand-logo.svg" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Test Assignment DevOps Milton</h3>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://github.com/miltonarango)

<!-- Architecture -->
## Architecture

[![System Architecture][system-architecture]](https://diagrams.mingrammer.com/)

### Assignment
For this assignment, I've completed the following tasks:

1. Set up a local Gitlab instance on your device using Docker and Docker Compose.
2. Within this Gitlab instance, create a web project that builds a Docker container serving static content.
3. Register a Gitlab runner instance on your device with your local Gitlab instance.
4. Write a `gitlab-ci.yml` file to automate the build and deployment of your service using the Gitlab runner connected in the previous step.

### Stretch Goals:
All the following goals have been completed as well:

- Test your service after each build and deploy only if the tests are successful.
- Serve the web content not directly through a port but using a reverse proxy, making it accessible through the URL http://mywebapp.localtest.me/.
  - Add a second static content service behind the proxy.
  - Enable secure HTTPS communication.
  - Provide detailed steps on how to automatically generate SSL certificates, as local generation is not possible.
- Connect your application to a Dockerized database and serve some content from it.
  - Explain how you manage the state of the database.
  - Describe your approach to running migrations.
- Implement a login mechanism for all your web services.
  - You can use Basic Auth.
  - Consider using a separate service.
  - Implement both of the above options on individual services.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Built With

* [![Gitlab][Gitlab.com]][Gitlab-url]
* [![postgres][postgres-badge]][postgres-url]
* [![fastapi][fastapi-badge]][fastapi-url]
* [![aws][aws-badge]][aws-url]
* [![vscode][vscode-badge]][vscode-url]
* [![go][go-badge]][go-url]
* [![python][python-badge]][python-url]
* [![docker][docker-badge]][docker-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

The project works with docker compose to spin up all the containers necessary to execute the services.

### Prerequisites

* Generating locally signed certificates for HTTPS using [mkcert](https://github.com/FiloSottile/mkcert)
  ```sh
  cd nginx/certs
  mkcert "mywebapp.localtest.me"
  mkcert "auth.localtest.me"
  mkcert "go.localtest.me"
  ```
* Install Docker 

### Installation

1. Configure an __OAuth__ application on a suitable provider (GitHub, Google, Facebook, ...).
2. Fill in the necessary environment variables in a .env file.
3. Run the Docker compose stack.
   ```sh
   docker compose up -d --build
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- Endpoints -->
## Endpoints

- **[mywebapp.localtest.me/docs](https://mywebapp.localtest.me/docs)** : OpenAPI specification for a sample python FastAPI web service.
- **[auth.localtest.me](https://auth.localtest.me)** : OAuth2 Proxy authentication provider.
- **[go.localtest.me](https://go.localtest.me)** : Basic go web server to test Basic HTTP Auth.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- SSL -->
## SSL Certificate Generation

1. For the SSL certificate generation we can add a **certbot** container to automatically create the SSL certificates using **Let's Encrypt**
2. Create a Cron job in the container to trigger a re-creation of the certificates when they are close to expire.
3. Reset the Nginx service once a certificate renewal is triggered by the Cron job.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- DB -->
## Database Management

1. The provisioning of the Database is handled by the docker compose file configuration, using environment variables to set the necessary configuration options for the database.
2. The connection and transactions to the database are handled by an ORM (SQLAlchemy) which acts as a repository interface to perform CRUD operations on the database.
3. Docker also provisions a volume to store the data of the database service, the volume is transitory and will be deleted when the compose stack is taken down. For a persistent volume there's an option for named volumes in docker.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- DB -->
## Database Migrations

1. When a change in the database schema is necessary we can use migrations to adapt to new schema requirements while also enabling rollbacks to a previous state.
2. In Python the migrations can be done by modifying the ORM model objects and initializing a migration tool like __Alembic__ for the __SQLAlchemy__ case.
3. Additional SQL code can be specified to deal with null values or data consistency issues.
<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Milton Arango - [@miltonarango](https://github.com/miltonarango) - milton.h.arango@gmail.com

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-url]: https://linkedin.com/in/milton-arango-giraldo
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[product-screenshot]: images/screenshot.png
[system-architecture]: docs/solution_architecture.png
[Gitlab.com]: https://img.shields.io/badge/gitlab%20ci-%23181717.svg?style=for-the-badge&logo=gitlab&logoColor=white
[Gitlab-url]: https://about.gitlab.com/
[postgres-badge]: https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white
[postgres-url]: https://www.postgresql.org/
[fastapi-badge]: https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi
[fastapi-url]: https://fastapi.tiangolo.com/
[aws-badge]: https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white
[aws-url]: https://aws.amazon.com/
[vscode-badge]: https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white
[vscode-url]: https://aws.amazon.com/
[go-badge]: https://img.shields.io/badge/go-%2300ADD8.svg?style=for-the-badge&logo=go&logoColor=white
[go-url]: https://go.dev/
[python-badge]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[python-url]: https://www.python.org/
[docker-badge]: https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white
[docker-url]: https://www.docker.com/
