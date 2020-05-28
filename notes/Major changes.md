# Major changes

I've done 2020, 2019, 2018

2018: c64c6c9dd
2017: f835378be
2016: e67749426
2015: 1ee70e9d8
2014: ba9ec669b
2013: a83e74b37
2012: bd23a3719
2011-06-01: f49f384fe
2011: 5e25f3171
2009: 2f3095014 ruby: Import ruby and slicc from GEMS Mon May 11 10:38:43 2009

- Gabe Black <gabeblack@google.com>
  - Updates for guest<->simulator communication
    - ABI changes
    - m5 utility
  - SystemC
    - Implemented simulator
    - TLM
  - Fastmodel support
  - More general code updates than can be listed
    - Port improvements
    - Unify SE and FS

- Daniel Carvalho <odanrc@yahoo.com.br>
  - Replacement policies
  - Cache compressions

- Nilay Vaish <nilay@cs.wisc.edu>
  - Ruby improvements
    - MESI 3 level
    - O3 compatibility
  - x86 improvements

- Jason Lowe-Power <jason@lowepower.com>
  - Learning gem5
  - Website
  - Governance

- Nils Asmussen <nils.asmussen@barkhauseninstitut.org>
  - RISC-V baremetal FS

- Tushar Krishna <tushar@ece.gatech.edu>
  - Garnet 2.0

- Javier Bueno Hedo <javier.bueno@metempsy.com>
  - predictor and prefetcher improvements
- Pau Cabre <pau.cabre@metempsy.com>
  - LTAGE improvements

- Christian Menard <christian.menard@tu-dresden.de>
  - gem5 <-> SystemC-TLM

- Tony Gutierrez <anthony.gutierrez@amd.com>
  - GPU model
- Brandon Potter <brandon.potter@amd.com>
  - SE mode improvements
    - Virtual file system
    - Many more syscalls
    - Full support for ROCM

- Sean Wilson <spwilson2@wisc.edu>
  - testlib

- Bobby R. Bruce <bbruce@ucdavis.edu>
  - Testing

- Alec Roelke <alec.roelke@gmail.com>
  - RISC-V

- Andreas Hansson <andreas.hanson@arm.com>
  - Classic cache: More simple protocols (mostly exclusive, etc.)
  - DRAM model
  - memory tracing / traffic generator
- Andreas Sandberg <Andreas.Sandberg@arm.com>
  - KVM CPU (virtualized fast forwarding)
    - Forking
    - CPU switching improvements
  - HDF5
  - python3
- Giacomo Travaglini <giacomo.travaglini@arm.com>
  - General arm improvements
  - Jason didn't track this in a detailed fashion. Feel free to fill in any specifics!
- Nikos Nikoleris <nikos.nikoleris@arm.com>
  - General classic cache improvements
  - Jason didn't track this in a detailed fashion. Feel free to fill in any specifics!
- Curtis Dunham <Curtis.Dunham@arm.com>
  - gem5+SST
- Gabor Dozsa <gabor.dozsa@arm.com>
  - dist-gem5
- Tiago Mück <tiago.muck@arm.com>
  - ARM+Ruby
- Andrew Bardsley <Andrew.Bardsley@arm.com>
  - MinorCPU
- Stephan Diestelhorst <stephan.diestelhorst@arm.com>
  - power model + DVFS
- Radhika Jagtap <radhika.jagtap@arm.com>
  - Elastic traces
- Anouk Van Laer <anouk.vanlaer@arm.com>
  - Power model
- Wendy Elsasser <wendy.elsasser@arm.com>
  - DRAM model
    - low power
    - multi cycle commands LPDDR5
- David Guillen-Fandos <david.guillen@arm.com>
  - Power model
- Akash Bagdia <akash.bagdia@ARM.com>
  - Power model
- Matteo Andreozzi <matteo.andreozzi@arm.com>
  - QoS aware memory controller
