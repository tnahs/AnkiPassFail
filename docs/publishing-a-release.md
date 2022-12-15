# Publishing a Release

1. Clone this repository.
2. Add feature/patch.
3. Bump version to `[VERSION]` in:

    - `pyproject.toml`
    - `addon/manifest.json`
    - `addon/__init__.py`

4. Push changes:

    ```shell
    git add .
    git commit -m "feat: shiny new things!"
    git push origin master
    ```

5. Tag the last commit:

    ```shell
    git tag [VERSION]
    git push origin [VERSION]
    ```

    > This will trigger GitHub Actions to:
    >
    > 1. Build the add-on bundle.
    > 2. Create a draft release in GitHub.
    > 3. Upload the bundle to the draft release.

6. Add release notes and publish the draft release.

    💡 The tag and title should be `[VERSION]`.
