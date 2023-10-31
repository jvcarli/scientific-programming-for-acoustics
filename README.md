# Scientific Programming for Acoustics

**WARN:** This project is in its early stages.

The website can be accessed at
[https://jvcarli.github.io/scientific-programming-for-acoustics/en](https://jvcarli.github.io/scientific-programming-for-acoustics/en)

## Developing

### Building the website locally

For building the website locally you'll need these dependencies installed:

- Python >= 3.9
- git

Then follow the steps bellow:

<details>
<summary>Unix like systems (macOS, Linux) <em>(Click to expand)</em>:</summary>

Clone the repository:

```sh
$ git clone https://github.com/jvcarli/scientific-programming-for-acoustics
```

Go to the cloned repository directory:

```sh
$ cd scientific-programming-for-acoustics
```

It is **strongly recommended** to create a virtual environment for installing the dependencies.

First check your python version and make it sure that it is the correct one:

```sh
$ python --version
```

It MUST output **at least Python 3.9.0**.

Then create the virtual environment using:

```sh
$ python -m venv venv
```

Activate the environment:

```sh
$ source venv/bin/activate
```

Then install Python dependencies using:

```sh
$ pip install -r dev_requirements.txt
```

Install the project [git hooks](https://git-scm.com/docs/githooks) using
[pre-commit](https://pre-commit.com/):

<details>
<summary>Security disclaimer <em>(Click to expand)</em> :</summary>

`pre-commit` tool was installed in the step above with `pip install -r dev_requirements.txt`.

Please note that when we run `pre-commit install` we are
installing custom git hooks defined in [.pre-commit-config.yaml](/.pre-commit-config.yaml/).

The scripts defined there are safe. You can check their entrypoint by
reading the file. [Example](https://github.com/jvcarli/scientific-programming-for-acoustics/blob/main/.pre-commit-config.yaml#L6)

Local scripts are in `tools/bin/git_hooks` directory.
</details>

```sh
$ pre-commit install
```

Finally build the website locally using:

```sh
$ make html
```

The website will be located at `build` diretory.

You can view it in your browser by serving it locally with:

```sh
$ python -m http.server --directory build/html
```

Then opening the link: [http://localhost:8000](http://localhost:8000)
</details>
