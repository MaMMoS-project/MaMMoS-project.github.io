Examples and Workflows
======================

Find the MaMMoS tools and workflows that best match what you want to do.

.. grid:: 1 2 3 3
    :gutter: 4

    .. grid-item-card:: `Explore a magnetic material <https://mammos-project.github.io/mammos/demonstrator/spindynamics-temperature-dependent-parameters.html>`_
        :img-top: /_static/magnetic_material.png
        :img-alt: Explore a magnetic material
        :text-align: center
        :class-card: mammos-usecase-card

        *"I know the composition/crystal structure. What magnetic properties can I obtain?"*

        +++

        `mammos-dft <https://mammos-project.github.io/mammos/examples/mammos-dft/index.html>`_
        →
        `mammos-spindynamics <https://mammos-project.github.io/mammos/examples/mammos-spindynamics/index.html>`_
        /
        `UppASD <https://github.com/UppASD/UppASD>`_
        →
        `mammos-analysis <https://mammos-project.github.io/mammos/examples/mammos-analysis/index.html>`_

        **Supporting tool:**
        `mammos-entity <https://mammos-project.github.io/mammos/examples/mammos-entity/index.html>`_

    .. grid-item-card:: `Hard magnet material exploration <https://mammos-project.github.io/mammos/demonstrator/hard-magnet-material-exploration.html>`_
        :img-top: /_static/permanent_magnet.png
        :img-alt: Hard magnet material exploration
        :text-align: center
        :class-card: mammos-usecase-card

        *"How do hard-magnet properties such as coercivity change with material and temperature?"*

        +++

        `mammos-dft <https://mammos-project.github.io/mammos/examples/mammos-dft/index.html>`_
        →
        `mammos-spindynamics <https://mammos-project.github.io/mammos/examples/mammos-spindynamics/index.html>`_
        →
        `mammos-analysis <https://mammos-project.github.io/mammos/examples/mammos-analysis/index.html>`_
        →
        `mammos-mumag <https://mammos-project.github.io/mammos/examples/mammos-mumag/index.html>`_
        →
        `mammos-analysis <https://mammos-project.github.io/mammos/examples/mammos-analysis/index.html>`_

        **Prerequisites:**
        `mammos-units <https://mammos-project.github.io/mammos/examples/mammos-units/index.html>`_
        ·
        `mammos-entity <https://mammos-project.github.io/mammos/examples/mammos-entity/index.html>`_

    .. grid-item-card:: `Sensor shape optimization workflow <https://mammos-project.github.io/mammos/demonstrator/sensor.html>`_
        :img-top: /_static/sensor.png
        :img-alt: Sensor shape optimization workflow
        :text-align: center
        :class-card: mammos-usecase-card

        *"How can the shape of a magnetic sensor element be optimized to maximize its linear response range?"*

        +++

        `mammos-spindynamics <https://mammos-project.github.io/mammos/examples/mammos-spindynamics/index.html>`_
        →
        `mammos-analysis <https://mammos-project.github.io/mammos/examples/mammos-analysis/index.html>`_
        →
        `Ubermag <https://ubermag.github.io/>`_ / OOMMF
        →
        `mammos-analysis <https://mammos-project.github.io/mammos/examples/mammos-analysis/index.html>`_
        →
        `Bayesian optimization <https://github.com/bayesian-optimization/BayesianOptimization>`_

        **Prerequisites:**
        `mammos-units <https://mammos-project.github.io/mammos/examples/mammos-units/index.html>`_
        ·
        `mammos-entity <https://mammos-project.github.io/mammos/examples/mammos-entity/index.html>`_

    .. grid-item-card:: Analyse experimental data
        :img-top: /_static/experimental_data.png
        :img-alt: Analyse experimental data
        :text-align: center
        :class-card: mammos-usecase-card

        *"I have VSM/SEM/HDF5 data. How do I extract magnetic/material parameters?"*

        +++

        `magmeas <https://github.com/MaMMoS-project/magmeas>`_,
        `sem_io <https://github.com/MaMMoS-project/sem_io>`_,
        `Read_HDF5 <https://github.com/MaMMoS-project/Advanced_Data_Visualization>`_,
        `DaHU <https://github.com/MaMMoS-project/DaHU>`_,
        `mammos-analysis <https://mammos-project.github.io/mammos/examples/mammos-analysis/index.html>`_

    .. grid-item-card:: Connect data and models
        :img-top: /_static/interoperability.png
        :img-alt: Connect data and models
        :text-align: center
        :class-card: mammos-usecase-card

        *"How do I make my data interoperable between methods/scales?"*

        +++

        `mammos-entity <https://mammos-project.github.io/mammos/examples/mammos-entity/index.html>`_,
        `mammos-units <https://mammos-project.github.io/mammos/examples/mammos-units/index.html>`_,
        `MagMO <https://github.com/MaMMoS-project/MagneticMaterialsOntology>`_,
        `mochada_kit <https://github.com/MaMMoS-project/mochada_kit>`_,
        `NOMAD tools <https://github.com/MaMMoS-project/nomad>`_


    .. grid-item-card:: Run a complete MaMMoS workflow
        :img-top: /_static/workflow.png
        :img-alt: Run a complete MaMMoS workflow
        :text-align: center
        :class-card: mammos-usecase-card

        *"Show me an end-to-end example."*

        +++

        `MaMMoS Demonstrator <https://mammos-project.github.io/mammos/demonstrator/index.html>`_
        /
        `Jupyter notebooks <https://github.com/MaMMoS-project/mammos>`_