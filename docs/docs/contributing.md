# Contributing to Fido

Fido is currently under alpha development. We are now welcoming contributors to collaborate on improving Fido.

## Get involved

There are many ways to contribute to Fido, and many of them do not involve writing any code. Here's a few ideas to get started,

- Contribute to Fido via code
- Help improve documentation on this site
- Request a feature by submitting a feature request

## Working on Fido

### Requirements

For developing code,

- Python `>=3.8`
- [Poetry](https://python-poetry.org/docs/) `>=1.0.0`
- Docker Engine `>=20.10`

For developing this site (refers to [Docusaurus Installation](https://docusaurus.io/docs/installation#requirements) for latest requirements),

- Node.js `>=12.13.0`
- Yarn `>=1.5`

### Development dependencies

Fido uses a different set of dependencies for development. To ensure all the correct dependencies are present, please run the following command when developing against Fido for the first time.

```bash
poetry install
```

Likewise, for developing against the website for the first time, install all the dependencies using Yarn,

```bash
cd docs && yarn install
```

## Development workflow

Using Poetry's virtual environment is the preferred development environment. The simplest way to start the virtualenv is to,

```bash
poetry shell
```

As for website development, you can start a local web server with hot-reloading for fast development,

```bash
yarn start
```

**Now you are ready to develop against Fido!**

## Site deployment

This site is automatically deployed using GitHub Actions. To update the site, push your changes to the `documentation` branch.
