# michar

## usage

### TODO generate pydocs 

[docs](./docs/)

```shell
michar --help
```

### configuration

[config.toml](./src/michar/config.toml)

## development

- [vscode](https://code.visualstudio.com/)
  - [install recommended extensions when opening this project workspace](.vscode/extensions.json)
- [homebrew](https://brew.sh/)
- [iterm2 + theme of choice](https://medium.com/airfrance-klm/beautify-your-iterm2-and-prompt-40f148761a49)
- [oh-my-zsh](https://ohmyz.sh/)
  - [powerlevel100k](https://github.com/romkatv/powerlevel10k)
  - [zsh-autosuggestion](https://github.com/zsh-users/zsh-autosuggestions)

### environment setup

#### pyenv

```shell
brew install pyenv
pyenv install 3.9
pyenv local 3.9
```

#### poetry

```shell
brew install poetry
poetry config virtualenvs.prefer-active-python true
poetry env use `pyenv which python`
poetry install
```

## test

### tox

```shell
tox -e pytest
```

## build

### TODO tox targets
