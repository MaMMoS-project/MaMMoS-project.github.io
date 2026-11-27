# MaMMoS project

Preliminary website repository for pages hosted at https://mammos-project.github.io/

The `main` branch here will be automotically published.

## Materials pages

The pages under `source/materials/` are generated from
[uppsala-data](https://github.com/MaMMoS-project/uppsala-data) when the
website is built in CI. To build them locally, clone that repository and run:

    pixi run python tools/generate_materials.py PATH/TO/uppsala-data
    pixi run make html
