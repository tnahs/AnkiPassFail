# AnkiPassFail

Avoid Ease-Hell!

## Installation

Download and run the latest [`AnkiPassFail.ankiaddon`][releases] release.

## Usage

Installing the add-on is all that's required. Once installed, the `Easy` and
`Hard` buttons are disabled along with their corresponding hotkeys `2` and
`4` respectively.

```
    <15m           2d           7d           2mo
┌───────────┐ ┌╴╴╴╴╴╴╴╴╴╴┐ ┌──────────┐ ┌╴╴╴╴╴╴╴╴╴╴┐
│   Again   │ ┆   ░░░░   ┆ │   Good   │ ┆   ░░░░   ┆
└───────────┘ └╴╴╴╴╴╴╴╴╴╴┘ └──────────┘ └╴╴╴╴╴╴╴╴╴╴┘
```

## Development

1. Install the required `[python-version]`. See the [Anki development][anki-dev]
   docs for more information.

    ```shell
    pyenv install [python-version]
    ```

2. Clone this repository.

    ```shell
    git clone git@github.com:tnahs/AnkiPassFail.git
    ```

3. Set `[python-version]` as the local version:

    ```shell
    cd ./AnkiPassFail
    pyenv local [python-version]
    ```

4. Create and enter a virtual environment:

    ```shell
    python -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip
    ```

5. Install required packages:

    ```shell
    pip install -r requirements.txt
    ```

6. Set development environment variables. See
   [Anki development | Environment Variables][env-var] for more information.

    Required:

    ```shell
    export ANKI_ADDON_DEVELOPMENT=1
    ```

    Optional:

    ```shell
    export ANKIDEV=1
    export LOGTERM=1
    export DISABLE_QT5_COMPAT=1
    ```

7. Run Anki from the terminal.

    ```shell
    anki
    ```

[anki-dev]: https://github.com/ankitects/anki/blob/main/docs/development.md
[env-var]: https://github.com/ankitects/anki/blob/main/docs/development.md#environmental-variables
[releases]: https://github.com/tnahs/AnkiPassFail/releases
