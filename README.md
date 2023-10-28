# Scientific Programming for Acoustics

**WARN:** This guide is in its early stages.

The website can be accessed at
[https://jvcarli.github.io/scientific-programming-for-acoustics/en](https://jvcarli.github.io/scientific-programming-for-acoustics/en)

## Building the website locally

For building the website locally you'll need these dependencies installed:

- Python >= 3.9
- git

Then follow the steps bellow (_Click to expand_):

<details>
<summary>Unix like systems (macOS, Linux)</summary>

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
$ pip install -r website/requirements.txt
```

Finally build the website locally using:

```sh
$ cd website && make html
```

The website will be located at `build` diretory.

You can view it in your browser by serving it locally with:

```sh
$ python -m http.server --directory build/html
```

Then opening the link: [http://localhost:8000](http://localhost:8000)

</details>
