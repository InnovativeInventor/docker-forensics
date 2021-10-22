## Docker-forensics 
In the real-world, sometimes you're given a Docker image of dubious provenance.
This repo aims to house some useful scripts/tools I've made to analyze and verify untrusted Docker images for backdoors or malware.

## Example usage

Fetching [nginx](https://hub.docker.com/_/nginx) images:
```bash
python fetch.py nginx
```

Unpacking:
```bash
bash unpack.sh
```

From here, you can inspect the filesystems normally. For example:
```bash
rg [some string]
fd [some filename]
```

You can also run `clamav` or other static analyzers to look for suspicious files.
