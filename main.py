import click
import typer
import requests
import json
app = typer.Typer()


def getdata():
    return requests.get("https://newssource.pythonanywhere.com/api").text


@app.command()
def api():
    data = getdata()
    data = json.loads(data)
    keys_list = data[0].keys()
    for i in data:
        click.echo(typer.style("API Data: ", fg=typer.colors.GREEN, bold=True))
        for j in keys_list:
            click.echo(f"{j} : {i[j]}")


@app.command()
def webtemp():
    web_content = ["index.html", "style.css", "index.js"]
    for item in web_content:
        url = 'https://github.com/m0hit-kumar/Web-template/blob/main/' + item
        r = requests.get(url, allow_redirects=True)
        open(item, 'wb').write(r.content)


if __name__ == "__main__":
    app()
