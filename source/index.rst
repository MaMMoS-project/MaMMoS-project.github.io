.. MaMMoS documentation master file, created by
   sphinx-quickstart on Mon Oct  2 09:55:58 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

**Ma**\gnetic **M**\ultiscale **Mo**\delling **S**\uite
=======================================================

.. toctree::
   :hidden:
   :maxdepth: 1

   Home <self>
   objectives
   who-we-are
   events
   units
   resources
   open-positions
   related-eu-projects


What is MaMMoS about?
---------------------

Magnetic materials are essential for many applications in energy, information, and communication technologies.
However, the complex phenomena at different length and time scales often limit the development of new magnetic
materials and devices. The goal of this project is to develop a magnetic multiscale modeling suite that will
allow the design and optimisation of magnetic materials and devices based on multiscale modelling,
characterisation, and numerical optimisation.

.. .. image:: _static/sectors.png
..     :width: 600

What can you do with MaMMoS?
------------------------------

MaMMoS connects experiments, simulations and AI across magnetic length scales.
Its Python tools make modelling, characterisation and optimisation interoperable.
**Focus:** resource-efficient permanent magnets and high-perfomance magnetic sensors.

Find the MaMMoS tools and workflows that best match what you want to do.

.. grid:: 1 2 3 3
    :gutter: 4

    .. grid-item-card:: `Explore a magnetic material <https://mammos-project.github.io/mammos/demonstrator/spindynamics-temperature-dependent-parameters.html>`_
        :text-align: center
        :class-card: mammos-usecase-card

        .. image:: /_static/magnetic_material.png
         :alt: Explore a magnetic material
         :target: https://mammos-project.github.io/mammos/demonstrator/spindynamics-temperature-dependent-parameters.html
         :class: mammos-card-image
         :width: 100%

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
        :text-align: center
        :class-card: mammos-usecase-card

        .. image:: /_static/permanent_magnet.png
         :alt: Hard magnet material exploration
         :target: https://mammos-project.github.io/mammos/demonstrator/hard-magnet-material-exploration.html
         :class: mammos-card-image
         :width: 100%

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

    .. grid-item-card:: `Analyse experimental data <https://mammos-project.github.io/magmeas/notebooks/getting_started.html>`_
        :text-align: center
        :class-card: mammos-usecase-card

        .. image:: /_static/experimental_data.png
         :alt: Analyse experimental data
         :target: https://mammos-project.github.io/magmeas/notebooks/getting_started.html
         :class: mammos-card-image
         :width: 100%

        *"I have VSM/SEM/HDF5 data. How do I extract magnetic/material parameters?"*

        +++

        `magmeas <https://github.com/MaMMoS-project/magmeas>`_,
        `sem_io <https://github.com/MaMMoS-project/sem_io>`_,
        `Read_HDF5 <https://github.com/MaMMoS-project/Advanced_Data_Visualization>`_,
        `DaHU <https://github.com/MaMMoS-project/DaHU>`_,
        `mammos-analysis <https://mammos-project.github.io/mammos/examples/mammos-analysis/index.html>`_

    .. grid-item-card:: `Sensor shape optimization workflow <https://mammos-project.github.io/mammos/demonstrator/sensor.html>`_
        :text-align: center
        :class-card: mammos-usecase-card

        .. image:: /_static/sensor.png
         :alt: Sensor shape optimization workflow
         :target: https://mammos-project.github.io/mammos/demonstrator/sensor.html
         :class: mammos-card-image
         :width: 100%

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

    .. grid-item-card:: `Connect data and models <https://mammos-project.github.io/mammos/examples/mammos-entity/quickstart.html>`_
        :text-align: center
        :class-card: mammos-usecase-card

        .. image:: /_static/interoperability.png
         :alt: Connect data and models
         :target: https://mammos-project.github.io/mammos/examples/mammos-entity/quickstart.html
         :class: mammos-card-image
         :width: 100%

        *"How do I make my data interoperable between methods/scales?"*

        +++

        `mammos-entity <https://mammos-project.github.io/mammos/examples/mammos-entity/index.html>`_,
        `mammos-units <https://mammos-project.github.io/mammos/examples/mammos-units/index.html>`_,
        `MagMO <https://github.com/MaMMoS-project/MagneticMaterialsOntology>`_,
        `mochada_kit <https://github.com/MaMMoS-project/mochada_kit>`_,
        `NOMAD tools <https://github.com/MaMMoS-project/nomad>`_


    .. grid-item-card:: `Run a complete MaMMoS workflow <https://mammos-project.github.io/mammos/demonstrator/index.html>`_
        :text-align: center
        :class-card: mammos-usecase-card

        .. image:: /_static/workflow.png
         :alt: Run a complete MaMMoS workflow
         :target: https://mammos-project.github.io/mammos/demonstrator/index.html
         :class: mammos-card-image
         :width: 100%

        *"Show me an end-to-end example."*

        +++

        `MaMMoS Demonstrator <https://mammos-project.github.io/mammos/demonstrator/index.html>`_
        /
        `Jupyter notebooks <https://github.com/MaMMoS-project/mammos>`_

MaMMoS Framework Software
-------------------------

The MaMMoS framework provides software components for magnetic multiscale
modeling.

The `MaMMoS demonstrator
<https://mammos-project.github.io/mammos/demonstrator/>`__ contains end-to-end
workflows combining functionality of multiple of the MaMMoS framework
components. Each workflow is provided as a Jupyter notebook, which can be
browsed as static HTML on the demonstrator webpages, executed in the cloud, or
downloaded for local execution with more powerful hardware. Further details can
be found on the demonstrator page.

The following table provides a short overview of the individual framework
components and contains links to the individual repositories and the
documentation:

.. list-table::
   :header-rows: 1

   * - Package repository
     - Summary
   * - `mammos <https://github.com/mammos-project/mammos>`__
       (`documentation <https://mammos-project.github.io/mammos>`__)
     - Meta package to install the full MaMMoS simulation suite.
   * - `mammos-ai <https://github.com/mammos-project/mammos-ai>`__
       (`documentation <https://mammos-project.github.io/mammos>`__)
     - Pre-trained AI models.
   * - `mammos-analysis <https://github.com/mammos-project/mammos-analysis>`__
       (`documentation <https://mammos-project.github.io/mammos>`__)
     -  Post-processing (hysteresis loop, kuzmin, ...).
   * - `mammos-dft <https://github.com/mammos-project/mammos-dft>`__
       (`documentation <https://mammos-project.github.io/mammos>`__)
     - DFT-based magnetic material properties.
   * - `mammos-entity <https://github.com/mammos-project/mammos-entity>`__
       (`documentation <https://mammos-project.github.io/mammos>`__)
     - Entity (Quantity and EMMO ontology label).
   * - `mammos-mumag <https://github.com/mammos-project/mammos-mumag>`__
       (`documentation <https://mammos-project.github.io/mammos>`__)
     - Finite-element micromagnetic simulations (hysteresis).
   * - `mammos-spindynamics <https://github.com/mammos-project/mammos-spindynamics>`__
       (`documentation <https://mammos-project.github.io/mammos>`__)
     - Spindynamics-based magnetic material properties.
   * - `mammos-units <https://github.com/mammos-project/mammos-units>`__
       (`documentation <https://mammos-project.github.io/mammos>`__)
     - Quantities (values with units).

Magnetic materials domain ontology
----------------------------------

As part of the MaMMoS project an EMMO-based
`domain ontology for magnetic materials (MagMO) <https://emmo-repo.github.io/domain-magnetic-materials/>`__
was created. The development takes place in https://github.com/emmo-repo/domain-magnetic-materials.

The `mammos-entity <https://github.com/mammos-project/mammos-entity>`__ Python package provides a convenient way of annotating raw data with metadata supplied by the ontology (EMMO and MagMO), e.g. by writing metadata-enriched files.

Additional Tools
----------------

The following tools have been created through or supported by the MaMMoS
project. For each, please follow the link for installation instructions and
documentation:

.. list-table::
   :header-rows: 1

   * - Package repository
     - Summary
   * - `mochada_kit <https://github.com/MaMMoS-project/mochada_kit>`__
       (`documentation <https://mammos-project.github.io/mochada_kit/user/index.html>`__)
     - Workflow diagram builder
   * - `sem_io <https://github.com/MaMMoS-project/sem_io>`__
       (`documentation <https://github.com/MaMMoS-project/sem_io/blob/main/README.md>`__)
     - Metadata extraction from SEM images
   * - `DaHU <https://github.com/MaMMoS-project/DaHU>`__
       (`documentation <https://github.com/MaMMoS-project/DaHU/blob/main/README.md>`__)
     - Data analysis dashboard for specific instruments at Institut Néel
   * - `Read_HDF5 <https://github.com/MaMMoS-project/Read_HDF5>`__
       (`documentation <https://github.com/MaMMoS-project/Read_HDF5/blob/main/readme.md>`__)
     - Data tools to read and write HDF5 files at Institute Néel
   * - `nomad <https://github.com/MaMMoS-project/nomad>`__
       (`documentation <https://github.com/MaMMoS-project/nomad/blob/main/README.md>`__)
     - Tools for uploading data to Nomad
   * - `magmeas <https://github.com/MaMMoS-project/magmeas>`__
       (`documentation <https://mammos-project.github.io/magmeas>`__)
     - Python package to import magnetometry data and calculate extrinsic magnetic properties


Further information
-------------------

:email:`thomas.schrefl@donau-uni.ac.at`

Project: 101135546 — MaMMoS

`HORIZON-CL4-2023-DIGITAL-EMERGING-01 <https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-details/horizon-cl4-2023-digital-emerging-01-12;callCode=null;freeTextSearchKeyword=2023-DIGITAL-EMERGING-01;matchWholeText=true;typeCodes=1>`_

Disclaimer
----------

Funded by the European Union. Views and opinions expressed are however those of the author(s) only and do not
necessarily reflect those of the European Union or European Health and Digital Executive Agency (HADEA). Neither
the European Union nor the granting authority can be held responsible for them.

Acknowledgments
---------------

.. figure:: _static/zulip-icon-128x128.png
   :align: left
   :scale: 50%
   :target: https://zulip.com/

Project MaMMoS is sponsored by `Zulip <https://zulip.com>`__. `Zulip <https://zulip.com>`__ is an organised team chat app designed for efficient communication, and used for project communication and software development within MaMMoS.
