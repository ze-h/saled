# `saled`, the SaLAI Editor

## Scheduling the project folder

The folder structure of the previous `SaLED` project

```
|-- app.py
|-- assets
|   |-- favicon.ico
|   `-- media
|       |-- demo-source.txt
|       `-- demo.mp3
|-- cached
|   `-- ledger.json
|-- callbacks.py
|-- layouts
|   |-- side_bar.py
|   |-- top_bar.py
|   `-- transcript_region.py
`-- utils
    |-- audio.py
    `-- fileIO.py
```

In transitioning to the `saled` project, we change the following folders from the source tree or Git commit:

-   `__pycache__` will be ignored from Git commit.
-   `assets` will be removed. The contents will be moved to another folder.
-   `cached` will be renamed as `.cached`

The folder structure of the new `saled` project is simplified to:

```
src/
|-- saled/
|   |-- app.py
|   |-- callbacks.py
|   |-- layouts/
|   |   |-- side_bar.py
|   |   |-- top_bar.py
|   |   `-- transcript_region.py
|   `-- utils/
|       |-- audio.py
|       `-- fileIO.py
test/
```

Of course, we have the needed `__init__` and `__main__` files as well.

## Cloning and configuring the project

Please follow the steps below to clone and configure the `saled` project.

-   Go to the parent folder where you want to host the `saled` project.
-   Run `git clone https://github.com/eraus-projs/saled.git`
-   Change the directory to `saled`.
-   Run `conda env create --name <saled11>`. Here, we use conda to create the base env for the project. You can change `<saled11>` to something else; `11` here stands for the default Python version is 3.11.
-   Activate the env using `conda activate <saled11>`.
-   Run `poetry install` to install the project.

After the installation, you can run the project anywhere you have MP3 files by typing `saled`.
