# Media Management

* Overseerr for media request management
* Prowlarr for tracker management
* Radarr as the middle-man from requests to viewing
* Sonarr as the middle-man from requests to viewing
* Readarr for managing books and audiobooks
* Plex for viewing media
* Tautulli for insight into Plex details
* environment var configured in [portainer](/docker/portainer/)

```yaml title="Compose"
--8<-- "docker/media-management/docker-compose.yml"
```