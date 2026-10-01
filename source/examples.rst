.. list-table::
   :header-rows: 1
   :widths: 22 43 35

   * - User goal
     - Typical question
     - Main tools/workflows

   * - Explore a magnetic material
     - "I know the composition/crystal structure. What magnetic properties can I obtain?"
     - `mammos-dft <https://mammos-project.github.io/mammos/examples/mammos-dft/index.html>`_
       →
       `mammos-spindynamics <https://mammos-project.github.io/mammos/examples/mammos-spindynamics/index.html>`_
       →
       `mammos-analysis <https://mammos-project.github.io/mammos/examples/mammos-analysis/index.html>`_

   * - Evaluate a permanent magnet
     - "What Hc, Mr or (BH)max can this material/microstructure achieve?"
     - `mammos-mumag <https://mammos-project.github.io/mammos/examples/mammos-mumag/index.html>`_
       →
       `mammos-analysis <https://mammos-project.github.io/mammos/examples/mammos-analysis/index.html>`_;
       optionally
       `mammos-ai <https://mammos-project.github.io/mammos/examples/mammos-ai/index.html>`_

   * - Optimise a magnetic sensor
     - "How does geometry affect sensor response/linearity?"
     - `Sensor demonstrator <https://mammos-project.github.io/mammos/demonstrator/sensor.html>`_
       →
       `mammos-mumag <https://mammos-project.github.io/mammos/examples/mammos-mumag/index.html>`_
       → optimisation workflow

   * - Analyse experimental data
     - "I have VSM/SEM/HDF5 data. How do I extract magnetic/material parameters?"
     - ``magmeas``, ``sem_io``, ``Read_HDF5``, ``DaHU``,
       `mammos-analysis <https://mammos-project.github.io/mammos/examples/mammos-analysis/index.html>`_

   * - Connect data and models
     - "How do I make my data interoperable between methods/scales?"
     - `mammos-entity <https://mammos-project.github.io/mammos/examples/mammos-entity/index.html>`_,
       `mammos-units <https://mammos-project.github.io/mammos/examples/mammos-units/index.html>`_,
       MagMO, ``mochada_kit``, NOMAD tools

   * - Run a complete MaMMoS workflow
     - "Show me an end-to-end example."
     - `MaMMoS Demonstrator <https://mammos-project.github.io/mammos/demonstrator/index.html>`_
       / Jupyter notebooks