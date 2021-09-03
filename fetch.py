import docker
import typer
import os
import tqdm

def main(repository: str):
    client = docker.from_env()
    client.images.pull(repository, all_tags=True)

    if not os.path.isdir("images"):
        os.mkdir("images")

    for image in tqdm.tqdm(client.images.list(repository, all=True)):
        fname = "images/" + "-".join([x.split(":")[1] for x in image.tags]) + "-" + image.short_id.split(":")[1]
        if not os.path.isdir(fname):
            os.mkdir(fname)

        with open(f"{fname}/image.tar", "wb") as f:
            for chunk in image.save():
                f.write(chunk)

if __name__ == "__main__":
    typer.run(main)


