import docker
import typer
import os
import tqdm

from typing import Optional

def main(repository: Optional[str] = None):
    client = docker.from_env()

    if repository:
        client.images.pull(repository, all_tags=True)
        images = client.images.list(repository, all=True)
    else:
        images = client.images.list(all=True)

    if not os.path.isdir("images"):
        os.mkdir("images")

    for image in tqdm.tqdm(images):
        fname = "images/" + "-".join([x.split(":")[1] for x in image.tags]) + "-" + image.short_id.split(":")[1]
        if not os.path.isdir(fname):
            os.mkdir(fname)

        with open(f"{fname}/image.tar", "wb") as f:
            for chunk in image.save():
                f.write(chunk)

if __name__ == "__main__":
    typer.run(main)


