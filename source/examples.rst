.. .. list-table::
..    :header-rows: 1
..    :widths: 22 43 35

..    * - User goal
..      - Typical question
..      - Main tools/workflows

..    * - Explore a magnetic material
..      - "I know the composition/crystal structure. What magnetic properties can I obtain?"
..      - `mammos-dft <https://mammos-project.github.io/mammos/examples/mammos-dft/index.html>`_
..        →
..        `mammos-spindynamics <https://mammos-project.github.io/mammos/examples/mammos-spindynamics/index.html>`_
..        →
..        `mammos-analysis <https://mammos-project.github.io/mammos/examples/mammos-analysis/index.html>`_

..    * - Evaluate a permanent magnet
..      - "What Hc, Mr or (BH)max can this material/microstructure achieve?"
..      - `mammos-mumag <https://mammos-project.github.io/mammos/examples/mammos-mumag/index.html>`_
..        →
..        `mammos-analysis <https://mammos-project.github.io/mammos/examples/mammos-analysis/index.html>`_;
..        optionally
..        `mammos-ai <https://mammos-project.github.io/mammos/examples/mammos-ai/index.html>`_

..    * - Optimise a magnetic sensor
..      - "How does geometry affect sensor response/linearity?"
..      - `Sensor demonstrator <https://mammos-project.github.io/mammos/demonstrator/sensor.html>`_
..        →
..        `mammos-mumag <https://mammos-project.github.io/mammos/examples/mammos-mumag/index.html>`_
..        →
..        `optimisation workflow <https://github.com/MaMMoS-project/dakota-sensor-optimization>`_

..    * - Analyse experimental data
..      - "I have VSM/SEM/HDF5 data. How do I extract magnetic/material parameters?"
..      - `magmeas <https://github.com/MaMMoS-project/magmeas>`_,
..        `sem_io <https://github.com/MaMMoS-project/sem_io>`_,
..        `Read_HDF5 <https://github.com/MaMMoS-project/Advanced_Data_Visualization>`_,
..        `DaHU <https://github.com/MaMMoS-project/DaHU>`_,
..        `mammos-analysis <https://mammos-project.github.io/mammos/examples/mammos-analysis/index.html>`_

..    * - Connect data and models
..      - "How do I make my data interoperable between methods/scales?"
..      - `mammos-entity <https://mammos-project.github.io/mammos/examples/mammos-entity/index.html>`_,
..        `mammos-units <https://mammos-project.github.io/mammos/examples/mammos-units/index.html>`_,
..        `MagMO <https://github.com/MaMMoS-project/MagneticMaterialsOntology>`_,
..        `mochada_kit <https://github.com/MaMMoS-project/mochada_kit>`_,
..        `NOMAD tools <https://github.com/MaMMoS-project/nomad>`_

..    * - Run a complete MaMMoS workflow
..      - "Show me an end-to-end example."
..      - `MaMMoS Demonstrator <https://mammos-project.github.io/mammos/demonstrator/index.html>`_
..        /
..        `Jupyter notebooks <https://github.com/MaMMoS-project/mammos>`_


Examples and Workflows
======================

Find the MaMMoS tools and workflows that best match what you want to do.

.. grid:: 1 2 3 3
   :gutter: 4

   .. grid-item-card:: Explore a magnetic material
      :img-top: /_static/magnetic_material.png
      :img-alt: Explore a magnetic material
      :text-align: center
      :class-card: mammos-usecase-card

      *"I know the composition/crystal structure. What magnetic properties can I obtain?"*

      +++

      `mammos-dft <https://mammos-project.github.io/mammos/examples/mammos-dft/index.html>`_
      →
      `mammos-spindynamics <https://mammos-project.github.io/mammos/examples/mammos-spindynamics/index.html>`_
      →
      `mammos-analysis <https://mammos-project.github.io/mammos/examples/mammos-analysis/index.html>`_


   .. grid-item-card:: Evaluate a permanent magnet
      :img-top: /_static/permanent_magnet.png
      :img-alt: Evaluate a permanent magnet
      :text-align: center
      :class-card: mammos-usecase-card

      *"What Hc, Mr or (BH)max can this material/microstructure achieve?"*

      +++

      `mammos-mumag <https://mammos-project.github.io/mammos/examples/mammos-mumag/index.html>`_
      →
      `mammos-analysis <https://mammos-project.github.io/mammos/examples/mammos-analysis/index.html>`_

      optionally
      `mammos-ai <https://mammos-project.github.io/mammos/examples/mammos-ai/index.html>`_


   .. grid-item-card:: Optimise a magnetic sensor
      :img-top: /_static/sensor.png
      :img-alt: Optimise a magnetic sensor
      :text-align: center
      :class-card: mammos-usecase-card

      *"How does geometry affect sensor response/linearity?"*

      +++

      `Sensor demonstrator <https://mammos-project.github.io/mammos/demonstrator/sensor.html>`_
      →
      `mammos-mumag <https://mammos-project.github.io/mammos/examples/mammos-mumag/index.html>`_
      →
      `optimisation workflow <https://github.com/MaMMoS-project/dakota-sensor-optimization>`_


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