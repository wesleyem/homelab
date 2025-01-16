# Homepage

Developed using `ghcr.io/gethomepage/homepage` docker image available at [gethomepage.dev](https://gethomepage.dev)

* workflow runs on changes to the configuration of homepage
* uses a self-hosted github runner to securly copy files to the directory where the container is mapped then restarts the container
* uses the a dockerproxy for security
* environment vars configured in [portainer](/docker/portainer/)
* secrets held in [1Password](https://1password.com) and used in GitHub Actions

```yaml title="Workflow"
--8<-- ".github/workflows/homepage-update-config.yml"
```

```yaml title="Compose"
--8<-- "docker/homepage/docker-compose.yml"
```