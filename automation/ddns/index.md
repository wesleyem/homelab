# Custom Cloudflare DNS Update

* Workflow runs every 30 min via self-hosted github runner, [octorunner](/docker/octorunner/)
* GitHub secrets passed through the workflow to the script via environment vars
* environment vars configured in [github](https://github.com/wesleyem/homelab/settings/secrets/actions)
* secrets held in [1Password](https://1password.com) and used in GitHub Actions
* **API Token** NOT **API Key** is used to initialize the client in the script
  * Token permissions: `All zones - DNS:Read, DNS:Edit`

```yaml title="Workflow"
--8<-- ".github/workflows/monitor-ip.yml"
```

```python title="Script"
--8<-- "automation/ddns/cloudflare-update.py"
```