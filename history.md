# Excavating gem5's history

I'm going to be writing a gem5-20 paper soon.
As part of this paper writing procedure, I wanted to find out all of the big contributions (new features) that had been added since the gem5 release.
Like everything in gem5, this was harder than expected!

In this post, I'm describing my methodology for "excavating" gem5's history.
This isn't a perfect methodology, so I may miss things.
I'll be sending out a list of "major" changes to gem5 in the last 9 years based on this methdology, so please let me know if I've missed anything!

## Things I learned from this exercise

- It may seem like we're overly pedantic about our git commit messages. We're not! It was progressively harder and harder to figure out what the changes were about.
- Important changes don't come with many commits (usually).
- The biggest contributors are people who are making general improvements, not new features
- In fact, this is general. Very few "new features" are added compared to commits!
  - No overarching roadmap
- More recently, there are fewer (simple) bug fixes. We've done a good job! The code quality is improving generally!
- General changes
  - Ruby has become *much* less popular
  - SE mode has become less popular
  - arm has become much more popular
- It's really hard to reverse engineer release notes!

## The recent past

Now, I want to find out what's been changing lately.
This was pretty easy using git's `log` command.
For instance, if I wanted to see all of the commits sorted by author since the beginning of this year, I can use the following command.

```
git shortlog -ne --since=2020-01-01
```

To see what happened in 2019, we can use a combination of `--since` and `--until`:

```
git shortlog -ne --since=2019-01-01 --until=2020-01-01
```

## The further past

I quickly found a problem with this method.
For some reason, when I checked to see what was committed in 2016, there was *nothing*!

```
git shortlog -ne --since=2016-01-01 --until=2017-01-01
```

Looking closer, in 2017, the "first" commit was made in February.
This helped me remember that we transitioned from mercurial to git around that time!

Digging into it a bit more, it looks like when we migrated all of the commits from mercurial to git we only kept the *author* date, not the commit date.
So, if you look at the dates in the gem5 history you'll find that before Feb 2017 the dates are non-linear.

Therefore, for 2017 and further, I'm instead using spans of commits to track what happened that year.
I'm using the following commits.

| Year       | First commit hash |
|------------|-------------------|
| 2018       | c64c6c9dd         |
| 2017       | f835378be         |
| 2016       | e67749426         |
| 2015       | 1ee70e9d8         |
| 2014       | ba9ec669b         |
| 2013       | a83e74b37         |
| 2012       | bd23a3719         |
| 2011-06-01 | f49f384fe         |
| 2011       | 5e25f3171         |
| First Ruby | 2f3095014         |

For example, to see all commits in 2016 we can use:

```
git shortlog -ne e67749426..f835378be
```

## The "first" commit

The first step was finding when m5 officially became gem5.

There was a long transition as the [GEMS]() code was merged into the [m5 codebase]().
This started back in May of 2009 with the following commit:

```
2f3095014 ruby: Import ruby and slicc from GEMS Mon May 11 10:38:43 2009
```

However, for the sake of arguments, I'm going to pick one commit as the "official" gem5 release.
That commit is

```
f49f384fe scons: rename some things from m5 to gem5
Author: Nathan Binkert <nate@binkert.org>
Date:   Thu Jun 2 17:36:18 2011 -0700
```

This is a nice commit on a nice date because it's almost exactly 9 years ago.

### history

#### 2020 (so far)

- Gabe Black <gabeblack@google.com>
  - Update ABI for guest<->simulator communication
  - improvements to m5 (guest<->simulator) utility
- Giacomo Travaglini <giacomo.travaglini@arm.com>
- Bobby R. Bruce <bbruce@ucdavis.edu>
  - CI tests and website
- Adrian Herrera <adrian.herrera@arm.com>
- Daniel Carvalho <odanrc@yahoo.com.br>
- Nils Asmussen <nils.asmussen@barkhauseninstitut.org>
  - Baremetal FS RISC-V
- Nikos Nikoleris <nikos.nikoleris@arm.com>
- Ciro Santilli <ciro.santilli@arm.com>
- Timothy Hayes <timothy.hayes@arm.com>
- Matthew Poremba <matthew.poremba@amd.com>
- Jordi Vaquero <jordi.vaquero@metempsy.com>
- Jason Lowe-Power <jason@lowepower.com>
- Ayaz Akram <yazakram@ucdavis.edu>
- Tiago Mück <tiago.muck@arm.com>
- Yu-hsin Wang <yuhsingw@google.com>
- Anouk Van Laer <anouk.vanlaer@arm.com>
- Earl Ou <shunhsingou@google.com>
- Gabor Dozsa <gabor.dozsa@arm.com>
- Hsuan Hsu <hsuan.hsu@mediatek.com>
- Tony Gutierrez <anthony.gutierrez@amd.com>
- Boris Shingarov <shingarov@gmail.com>
- Trivikram Reddy <tvreddy@ucdavis.edu>
- Andreas Sandberg <Andreas.Sandberg@arm.com>
- Andriani Mappoura <andriani.mappoura@arm.com>
- Chun-Chen Hsu <chunchenhsu@google.com>
- Giacomo Gabrielli <giacomo.gabrielli@arm.com>
- Hussein Elnawawy <hussein.elnawawy@gmail.com>
- Joe Gross <joe.gross@amd.com>
- Mahyar Samani <msamani@ucdavis.edu>
- Matt Poremba <matthew.poremba@amd.com>
- Michiel Van Tol <michiel.vantol@arm.com>
- Wendy Elsasser <wendy.elsasser@arm.com>
- Yuan Yao <yuanyao@seas.harvard.edu>
- jiegec <noc@jiegec.ac.cn>

#### 2019

- Gabe Black <gabeblack@google.com>
  - SystemC TLM
  - Port API updates
  - fastmodel support
- Giacomo Travaglini <giacomo.travaglini@arm.com>
  - ARM improvements (GICv3&4, SMMU)
- Daniel Carvalho <odanrc@yahoo.com.br>
  - Cache compression
- Andreas Sandberg <Andreas.Sandberg@arm.com>
  - HDF5
  - python3 (beginnings)
- Ciro Santilli <ciro.santilli@arm.com>
- Nikos Nikoleris <nikos.nikoleris@arm.com>
- Javier Bueno Hedo <javier.bueno@metempsy.com>
  - predictors and prefetcher improvements
- Brandon Potter <brandon.potter@amd.com>
- Tiago Mück <tiago.muck@arm.com>
  - ARM+Ruby support
- Adrian Herrera <adrian.herrera@arm.com>
- Bobby R. Bruce <bbruce@ucdavis.edu>
  - testing improvements
- Andrea Mondelli <andrea.mondelli@ucf.edu>
- Jason Lowe-Power <jason@lowepower.com>
- Chun-Chen Hsu <chunchenhsu@google.com>
- Pouya Fotouhi <pfotouhi@ucdavis.edu>
- Tuan Ta <qtt2@cornell.edu>
- Giacomo Gabrielli <giacomo.gabrielli@arm.com>
- Gabor Dozsa <gabor.dozsa@arm.com>
- Jairo Balart <jairo.balart@metempsy.com>
- Ryan Gambord <gambordr@oregonstate.edu>
- IanJiangICT <ianjiang.ict@gmail.com>
- Jordi Vaquero <jordi.vaquero@metempsy.com>
- Javier Setoain <javier.setoain@arm.com>
- Alec Roelke <alec.roelke@gmail.com>
- Anouk Van Laer <anouk.vanlaer@arm.com>
- Hoa Nguyen <hoanguyen@ucdavis.edu>
- Ivan Pizarro <ivan.pizarro@metempsy.com>
- Ayaz Akram <yazakram@ucdavis.edu>
- Tommaso Marinelli <tommarin@ucm.es>
- Isaac Sánchez Barrera <isaac.sanchez@bsc.es>
- Jing Qu <jqu32@wisc.edu>
- Srikant Bharadwaj <srikant.bharadwaj@amd.com>
- Adrià Armejach <adria.armejach@bsc.es>
- Alexandru Dutu <alexandru.dutu@amd.com>
- Austin Harris <austinharris@utexas.edu>
- Bertrand Marquis <bertrand.marquis@arm.com>
- David Hashe <david.hashe@amd.com>
- Jan-Peter Larsson <jan-peter.larsson@arm.com>
- Joe Gross <joe.gross@amd.com>
- Jui-min Lee <fcrh@google.com>
- Mahyar Samani <msamani@ucdavis.edu>
- Marc Mari Barcelo <marc.maribarcelo@arm.com>
- Matthew Poremba <matthew.poremba@amd.com>
- Michiel Van Tol <michiel.vantol@arm.com>
- Mingyuan <xiang_my@outlook.com>
- Moyang Wang <mw828@cornell.edu>
- Sandipan Das <sandipan@linux.ibm.com>
- Tony Gutierrez <anthony.gutierrez@amd.com>
- Anis Peysieux <anis.peysieux@inria.fr>
- Avishai Tvila <avishai.tvila@gmail.com>
- Bagus Hanindhito <hanindhito@bagus.my.id>
- Curtis Dunham <Curtis.Dunham@arm.com>
- Doğukan Korkmaztürk <d.korkmazturk@gmail.com>
- Georg Kotheimer <georg.kotheimer@mailbox.tu-dresden.de>
- Isaac Richter <isaac.richter@rochester.edu>
- John Alsop <johnathan.alsop@amd.com>
- Kevin Brodsky <kevin.brodsky@arm.com>
- Marjan Fariborz <mfariborz@ucdavis.edu>
- Matt Sinclair <mattdsinclair@gmail.com>
- Matteo Andreozzi <matteo.andreozzi@arm.com>
- Nicholas Lindsay <nicholas.lindsay@arm.com>
- Pablo Prieto <pablo.prieto@unican.es>
- Pau Cabre <pau.cabre@metempsy.com>
- Po-Hao Su <supohaosu@gmail.com>
- Polydoros Petrakis <ppetrak@ics.forth.gr>
- Rahul Thakur <rjthakur@google.com>
- Rekai Gonzalez-Alberquilla <rekai.gonzalezalberquilla@arm.com>
- Ruben Ayrapetyan <ruben.ayrapetyan@arm.com>
- Rutuja Oza <roza@ucdavis.edu>
- Samuel Grayson <sam@samgrayson.me>
- Sascha Bischoff <sascha.bischoff@arm.com>
- Stanislaw Czerniawski <stacze01@arm.com>
- Steve Reinhardt <stever@gmail.com>
- Timothy Hayes <timothy.hayes@arm.com>
- Willy Wolff <willy.mh.wolff.ml@gmail.com>
- Xin Ouyang <xin.ouyang@streamcomputing.com>
- Yifei Liu <liu.ad2039@gmail.com>
- Zicong Wang <wangzicong@nudt.edu.cn>
- seanzw <seanyukigeek@gmail.com>

#### 2018

- Gabe Black <gabeblack@google.com>
  - SystemC in gem5
- Giacomo Travaglini <giacomo.travaglini@arm.com>
  - ARM improvements
- Daniel Carvalho <odanrc@yahoo.com.br>
  - Replacement policies
- Nikos Nikoleris <nikos.nikoleris@arm.com>
- Andreas Sandberg <Andreas.Sandberg@arm.com>
- Jason Lowe-Power <jason@lowepower.com>
- Ciro Santilli <ciro.santilli@arm.com>
- Brandon Potter <brandon.potter@amd.com>
- Chuan Zhu <chuan.zhu@arm.com>
- Pau Cabre <pau.cabre@metempsy.com>
  - LTAGE improvements
- Tuan Ta <qtt2@cornell.edu>
- Alec Roelke <alec.roelke@gmail.com>
- Tony Gutierrez <anthony.gutierrez@amd.com>
- Glenn Bergmans <glenn.bergmans@arm.com>
  - DT Autogeneration
- Matteo Andreozzi <matteo.andreozzi@arm.com>
  -QoS aware memory controller
- Anouk Van Laer <anouk.vanlaer@arm.com>
- Hanhwi Jang <jang.hanhwi@gmail.com>
- Rekai Gonzalez-Alberquilla <rekai.gonzalezalberquilla@arm.com>
- Siddhesh Poyarekar <siddhesh.poyarekar@gmail.com>
- Curtis Dunham <Curtis.Dunham@arm.com>
- Robert Kovacsics <rmk35@cl.cam.ac.uk>
- Sean Wilson <spwilson2@wisc.edu>
  - testlib
- Adrien Pesle <adrien.pesle@arm.com>
- Bradley Wang <radwang@ucdavis.edu>
- Chun-Chen Hsu <chunchenhsu@google.com>
- Javier Bueno Hedo <javier.bueno@metempsy.com>
- Matt Sinclair <mattdsinclair@gmail.com>
- Wendy Elsasser <wendy.elsasser@arm.com>
- Earl Ou <shunhsingou@google.com>
- Edmund Grimley Evans <Edmund.Grimley-Evans@arm.com>
- Giacomo Gabrielli <giacomo.gabrielli@arm.com>
- Matt Horsnell <matt.horsnell@arm.com>
- Maurice Becker <madnaurice@googlemail.com>
- Pin-Yen Lin <treapking@google.com>
- Rico Amslinger <rico.amslinger@informatik.uni-augsburg.de>
- Sherif Elhabbal <elhabbalsherif@gmail.com>
- Xiaoyu Ma <xiaoyuma@google.com>
- Yuetsu Kodama <yuetsu.kodama@riken.jp>
- Alexandru Dutu <alexandru.dutu@amd.com>
- Austin Harris <austinharris@utexas.edu>
- Brad Beckmann <brad.beckmann@amd.com>
- Chen Zou <chenzou@uchicago.edu>
- Christian Menard <christian.menard@tu-dresden.de>
- Gabor Dozsa <gabor.dozsa@arm.com>
- John Alsop <johnathan.alsop@amd.com>
- Kevin Brodsky <kevin.brodsky@arm.com>
- Khalique <khalique913@gmail.com>
- Matteo M. Fusi <matteo.fusi@bsc.es>
- Maximilian Stein <maximilian.stein@tu-dresden.de>
- Michael LeBeane <michael.lebeane@amd.com>
- Michiel Van Tol <michiel.vantol@arm.com>
- Nayan Deshmukh <nayan26deshmukh@gmail.com>
- Robert Scheffel <robert.scheffel1@tu-dresden.de>
- Rohit Kurup <rohit.kurup@arm.com>
- Srikant Bharadwaj <srikant.bharadwaj@amd.com>
- Stanislaw Czerniawski <stacze01@arm.com>
- Steve Reinhardt <stever@gmail.com>
- Sujay Phadke <electronicsguy123@gmail.com>
- Swapnil Haria <swapnilster@gmail.com>
- Xianwei Zhang <xianwei.zhang@amd.com>

#### 2017

- Gabe Black <gabeblack@google.com>
  - Various improvements to scons, tests, and many ISAs
- Andreas Sandberg <andreas.sandberg@arm.com>
  - Various improvements to python support and ARM ISA
- Nikos Nikoleris <nikos.nikoleris@arm.com>
  - General improvements to classic cache protocol
- Brandon Potter <brandon.potter@amd.com>
  - Improvements to SE mode
- Alec Roelke <ar4jc@virginia.edu>
  - RISC-V support added
- Giacomo Travaglini <giacomo.travaglini@arm.com>
  - Various improvements to ARM
- Sean Wilson <spwilson2@wisc.edu>
- Curtis Dunham <Curtis.Dunham@arm.com>
- Jason Lowe-Power <jason@lowepower.com>
  - Learning gem5
  - Beginning of formal project governance
- Christian Menard <Christian.Menard@tu-dresden.de>
  - gem5 <-> SystemC-TLM
- Jose Marinho <jose.marinho@arm.com>
- Bjoern A. Zeeb <baz21@cam.ac.uk>
- Peter Enns <Peter.Enns@arm.com>
- Rekai Gonzalez-Alberquilla <rekai.gonzalezalberquilla@arm.com>
- Gabor Dozsa <gabor.dozsa@arm.com>
- Gedare Bloom <gedare@rtems.org>
- Matthias Jung <jungma@eit.uni-kl.de>
- Radhika Jagtap <radhika.jagtap@arm.com>
- Andreas Hansson <andreas.hanson@arm.com>
- Anouk Van Laer <anouk.vanlaer@arm.com>
- Pau Cabre <pau.cabre@metempsy.com>
- Paul Rosenfeld <prosenfeld@micron.com>
- Rahul Thakur <rjthakur@google.com>
- Sudhanshu Jha <sudhanshu.jha@arm.com>
- Lena Olson <leolson@google.com>
- Matthew Poremba <matthew.poremba@amd.com>
- Sascha Bischoff <sascha.bischoff@arm.com>
- Éder F. Zulian <zulian@eit.uni-kl.de>
- Austin Harris <austinharris@utexas.edu>
- David Guillen-Fandos <david.guillen@arm.com>
- Javier Cano-Cano <javier.cano555@gmail.com>
- Matthias Hille <matthiashille8@gmail.com>
- Nathanael Premillieu <nathanael.premillieu@arm.com>
- Rico Amslinger <rico.amslinger@informatik.uni-augsburg.de>
- Riken Gohil <Riken.Gohil@arm.com>
- Stephan Diestelhorst <stephan.diestelhorst@arm.com>
- Swapnil Haria <swapnilster@gmail.com>
- Tiago Mück <tiago.muck@arm.com>
- Tony Gutierrez <anthony.gutierrez@amd.com>
- Weiping Liao <weipingliao@google.com>
- Wendy Elsasser <wendy.elsasser@arm.com>
- Alexandru Dutu <alexandru.dutu@amd.com>
- Ashkan Tousi <ashkan.tousimojarad@arm.com>
- Boris Shingarov <shingarov@gmail.com>
- Geoffrey Blake <geoffrey.blake@arm.com>
- Hanhwi Jang <jang.hanhwi@gmail.com>
- Matt Sinclair <mattdsinclair@gmail.com>
- Matteo Andreozzi <matteo.andreozzi@arm.com>
- Rohit Kurup <rohit.kurup@arm.com>
- Santi Galan <santi.galan@metempsy.com>
- Sean McGoogan <Sean.McGoogan@arm.com>
- Tushar Krishna <tushar@ece.gatech.edu>
- Zhang Zheng <perise@gmail.com>

#### 2016

- Andreas Sandberg <Andreas.Sandberg@arm.com>
  - Forking
  - Various fixes
- Andreas Hansson <andreas.hanson@arm.com>
  - Classic cache improvements (mostly exclusive)
- Curtis Dunham <Curtis.Dunham@arm.com>
  - General ARM
- Tony Gutierrez <anthony.gutierrez@amd.com>
  - GPU model
- Steve Reinhardt <stever@gmail.com>
  - Various changes
- Nikos Nikoleris <nikos.nikoleris@arm.com>
  - Classic caches improvements
- Brandon Potter <brandon.potter@amd.com>
  - SE mode improvements
- Michael LeBeane <michael.lebeane@amd.com>
- Dylan Johnson <Dylan.Johnson@ARM.com>
- Alexandru Dutu <alexandru.dutu@amd.com>
- Mitch Hayenga <mitch.hayenga@arm.com>
- David Guillen-Fandos <david.guillen@arm.com>
  - Power model
- Gabor Dozsa <gabor.dozsa@arm.com>
  - Distributed ethernet model
- Tushar Krishna <tushar@ece.gatech.edu>
  - Garnet 2.0 updates
- Alec Roelke <alec.roelke@gmail.com>
  - Beginning of RISC-V
- Bjoern A. Zeeb <baz21@cam.ac.uk>
  - FreeBSD support
- Jason Lowe-Power <jason@lowepower.com>
- Rekai Gonzalez-Alberquilla <rekai.gonzalezalberquilla@arm.com>
- Arthur Perais <arthur.perais@inria.fr>
- Abdul Mutaal Ahmad <abdul.mutaal@gmail.com>
- Brad Beckmann <brad.beckmann@amd.com>
- David Hashe <david.hashe@amd.com>
- Mohammad Alian <m.alian1369@gmail.com>
- Omar Naji <Omar.Naji@arm.com>
- Sascha Bischoff <sascha.bischoff@arm.com>
- Wendy Elsasser <wendy.elsasser@arm.com>
  - DRAM low-power functionality
- Akash Bagdia <akash.bagdia@ARM.com>
  - Power model
- Joel Hestness <jthestness@gmail.com>
- John Kalamatianos <john.kalamatianos@amd.com>
- Matteo Andreozzi <matteo.andreozzi@arm.com>
- Matthew Poremba <matthew.poremba@amd.com>
- Radhika Jagtap <radhika.jagtap@arm.com>
- Stephan Diestelhorst <stephan.diestelhorst@arm.com>
- Jieming Yin <jieming.yin@amd.com>
- Matthias Jung <jungma@eit.uni-kl.de>
- Reiley Jeapaul <Reiley.Jeyapaul@arm.com>
- Tuan Ta <qtt2@cornell.edu>
- Blake Hechtman <bah13@duke.edu>
- Christian Menard <christian.menard@tu-dresden.de>
- Fernando Endo <fernando.endo2@gmail.com>
- Geoffrey Blake <geoffrey.blake@arm.com>
- Ilias Vougioukas <Ilias.Vougioukas@ARM.com>
- Jakub Jermar <jakub@jermar.eu>
- Joe Gross <joe.gross@amd.com>
- Krishnendra Nathella <Krishnendra.Nathella@arm.com>
- Marco Elver <Marco.Elver@ARM.com>
- Matt Poremba <matthew.poremba@amd.com>
- Nathan Binkert <nate@binkert.org>
- Nathanael Premillieu <nathanael.premillieu@arm.com>
- Nicolas Derumigny <nderumigny@gmail.com>
- Prakash Ramrakhyani <prakash.ramrakhyani@arm.com>
- Ricardo Alves <ricardo.alves@arm.com>
- Sergei Trofimov <sergei.trofimov@arm.com>
- Shawn Rosti <shawn.rosti@gmail.com>
- Sooraj Puthoor <puthoorsooraj@gmail.com>
- Sophiane Senni <sophiane.senni@gmail.com>
- Victor Garcia <victor.garcia@arm.com>

#### 2015

- Andreas Hansson <andreas.hanson@arm.com>
  - Classic memory improvements
- Andreas Sandberg <Andreas.Sandberg@arm.com>
  - ARM improvements
- Nilay Vaish <nilay@cs.wisc.edu>
  - General Ruby improvements
- David Hashe <david.hashe@amd.com>
- Steve Reinhardt <stever@gmail.com>
- Curtis Dunham <Curtis.Dunham@arm.com>
  - SST-gem5 connector?
- Brandon Potter <brandon.potter@amd.com>
- Brad Beckmann <brad.beckmann@amd.com>
- Joel Hestness <jthestness@gmail.com>
- Ali Jafri <ali.jafri@arm.com>
- Tony Gutierrez <anthony.gutierrez@amd.com>
- Radhika Jagtap <radhika.jagtap@arm.com>
  - Elastic traces?
- Mitch Hayenga <mitch.hayenga@arm.com>
- Ali Saidi <Ali.Saidi@arm.com>
- Gabe Black <gabeblack@google.com>
- Jason Lowe-Power <jason@lowepower.com>
- Nikos Nikoleris <nikos.nikoleris@arm.com>
- Stephan Diestelhorst <stephan.diestelhorst@arm.com>
- Erfan Azarkhish <erfan.azarkhish@unibo.it>
  - HMC model
- Marco Balboni <Marco.Balboni@ARM.com>
- Nathanael Premillieu <nathanael.premillieu@arm.com>
- Ruslan Bukin <br@bsdpad.com>
- Sascha Bischoff <sascha.bischoff@arm.com>
- Wendy Elsasser <wendy.elsasser@arm.com>
- Abdul Mutaal Ahmad <abdul.mutaal@gmail.com>
- Andrew Bardsley <Andrew.Bardsley@arm.com>
- Bjoern A. Zeeb <baz21@cam.ac.uk>
- Geoffrey Blake <geoffrey.blake@arm.com>
- Giacomo Gabrielli <giacomo.gabrielli@arm.com>
- Joe Gross <joe.gross@amd.com>
- Lena Olson <leolson@google.com>
- Malek Musleh <malek.musleh@gmail.com>
- Palle Lyckegaard <palle@lyckegaard.dk>
- Andrew Lukefahr <lukefahr@umich.edu>
- Boris Shingarov <shingarov@gmail.com>
- Cagdas Dirik <cdirik@micron.com>
- David Guillen-Fandos <david.guillen@arm.com>
- Dylan Johnson <Dylan.Johnson@ARM.com>
- Emilio Castillo <castilloe@unican.es>
- Gabor Dozsa <gabor.dozsa@arm.com>
- Karthik Sangaiah <karthik.sangaiah@arm.com>
- Matt Evans <matt.evans@arm.com>
- Matthias Jung <jungma@eit.uni-kl.de>
- Rekai Gonzalez-Alberquilla <rekai.gonzalezalberquilla@arm.com>
- Rene de Jong <rene.dejong@arm.com>
- Rizwana Begum <rb639@drexel.edu>
- Rune Holm <rune.holm@arm.com>
- Timothy M. Jones <timothy.jones@arm.com>
- Alexandru Dutu <alexandru.dutu@amd.com>
- Chris Emmons <chris.emmons@arm.com>
- Christoph Pfister <pfistchr@student.ethz.ch>
- Dibakar Gope <gope@wisc.edu>
- Dongxue Zhang <elta.era@gmail.com>
- Hongil Yoon <ongal@cs.wisc.edu>
- Marco Elver <Marco.Elver@ARM.com>
- Maxime Martinasso <maxime.cscs@gmail.com>
- Mike Upton <michaelupton@gmail.com>
- Monir Mozumder <monir.mozumder@amd.com>
- Pau Cabre <pau.cabre@metempsy.com>
- Peter Enns <Peter.Enns@arm.com>
- Swapnil Haria <swapnilster@gmail.com>
- Victor Garcia <victor.garcia@arm.com>

#### 2014

- Andreas Hansson <andreas.hanson@arm.com>
- Nilay Vaish <nilay@cs.wisc.edu>
  - MESI three level
  - Ruby improvements
  - x86 improvements
- Andreas Sandberg <Andreas.Sandberg@arm.com>
  - KVM CPU
- Mitch Hayenga <mitch.hayenga@arm.com>
- Curtis Dunham <Curtis.Dunham@arm.com>
- Gabe Black <gabeblack@google.com>
- Ali Saidi <Ali.Saidi@arm.com>
- Andrew Bardsley <Andrew.Bardsley@arm.com>
  - Minor CPU
- Steve Reinhardt <stever@gmail.com>
- Stephan Diestelhorst <stephan.diestelhorst@arm.com>
  - Power model and DVFS support
- Geoffrey Blake <geoffrey.blake@arm.com>
- Tony Gutierrez <anthony.gutierrez@amd.com>
- Dam Sunwoo <dam.sunwoo@arm.com>
- Alexandru Dutu <alexandru.dutu@amd.com>
  - KVM in SE mode
- Omar Naji <Omar.Naji@arm.com>
  - DRAM Power
- Marco Elver <Marco.Elver@ARM.com>
- Binh Pham <binhpham@cs.rutgers.edu>
- Radhika Jagtap <radhika.jagtap@arm.com>
- Wendy Elsasser <wendy.elsasser@arm.com>
- Yasuko Eckert <yasuko.eckert@amd.com>
- Akash Bagdia <akash.bagdia@ARM.com>
- Andrew Lukefahr <lukefahr@umich.edu>
- Giacomo Gabrielli <giacomo.gabrielli@arm.com>
- Jiuyue Ma <majiuyue@ncic.ac.cn>
- Joel Hestness <jthestness@gmail.com>
- Sascha Bischoff <sascha.bischoff@arm.com>
- Amin Farmahini <aminfar@gmail.com>
- Eric Van Hensbergen <eric.vanhensbergen@arm.com>
- Kanishk Sugand <kanishk.sugand@arm.com>
- Marc Orr <marc.orr@gmail.com>
- Matt Horsnell <matt.horsnell@arm.com>
- Michael Adler <Michael.Adler@intel.com>
- Neha Agarwal <neha.agarwal@arm.com>
- Stan Czerniawski <stan.czerniawski@arm.com>
- Chris Adeniyi-Jones <Chris.Adeniyi-Jones@arm.com>
- Chris Emmons <chris.emmons@arm.com>
- Christopher Torng <clt67@cornell.edu>
- Emilio Castillo <castilloe@unican.es>
- Faissal Sleiman <Faissal.Sleiman@arm.com>
- Gabe Loh gabriel.loh@amd.com gloh <none@none>
- Gedare Bloom <gedare@rtems.org>
- Matt Evans <matt.evans@arm.com>
- Nikos Nikoleris <nikos.nikoleris@arm.com>
- Ola Jeppsson <ola.jeppsson@gmail.com>
- Paul Rosenfeld <prosenfeld@micron.com>
- Prakash Ramrakhyani <prakash.ramrakhyani@arm.com>
- Severin Wischmann <wiseveri@student.ethz.ch>
- Stian Hvatum <stian@dream-web.no>
- Timothy M. Jones <timothy.jones@arm.com>
- Tom Jablin <tjablin@gmail.com>
- Xiangyu Dong <rioshering@gmail.com>

#### 2013

- Andreas Hansson <andreas.hanson@arm.com>
  - DRAM model
  - Memory tracing / traffic generator support
- Andreas Sandberg <Andreas.Sandberg@arm.com>
  - CPU switching improvements
  - KVM CPU
- Nilay Vaish <nilay@cs.wisc.edu>
  - x86 improvements
  - Ruby improvements
- Ali Saidi <Ali.Saidi@arm.com>
- Steve Reinhardt <stever@gmail.com>
- Joel Hestness <jthestness@gmail.com>
- Sascha Bischoff <sascha.bischoff@arm.com>
- Tony Gutierrez <anthony.gutierrez@amd.com>
- Geoffrey Blake <geoffrey.blake@arm.com>
- Akash Bagdia <akash.bagdia@ARM.com>
- Ani Udipi <ani.udipi@arm.com>
- Dam Sunwoo <dam.sunwoo@arm.com>
- Lena Olson <leolson@google.com>
- Mitch Hayenga <mitch.hayenga@arm.com>
- Faissal Sleiman <Faissal.Sleiman@arm.com>
- Malek Musleh <malek.musleh@gmail.com>
- Neha Agarwal <neha.agarwal@arm.com>
- Chris Emmons <chris.emmons@arm.com>
- Gabe Black <gabeblack@google.com>
- Chander Sudanthi <chander.sudanthi@arm.com>
- Christian Menard <christian.menard@tu-dresden.de>
- Christopher Torng <clt67@cornell.edu>
- Deyaun Guo <guodeyuan@tsinghua.org.cn>
- Jason Lowe-Power <jason@lowepower.com>
- Lluís Vilanova <vilanova@ac.upc.edu>
- Matt Evans <matt.evans@arm.com>
- Matt Horsnell <matt.horsnell@arm.com>
- Michael Levenhagen <mjleven@sandia.gov>
- Prakash Ramrakhyani <prakash.ramrakhyani@arm.com>
- Stephan Diestelhorst <stephan.diestelhorst@arm.com>
- Timothy M. Jones <timothy.jones@arm.com>
- Uri Wiener <uri.wiener@arm.com>
- Yasuko Eckert <yasuko.eckert@amd.com>
- Amin Farmahini <aminfar@gmail.com>
- Andrea Pellegrini <andrea.pellegrini@gmail.com>
- Blake Hechtman <bah13@duke.edu>
- Brad Beckmann <brad.beckmann@amd.com>
- Dibakar Gope <gope@wisc.edu>
- Emilio Castillo <castilloe@unican.es>
- Eric Van Hensbergen <eric.vanhensbergen@arm.com>
- Gedare Bloom <gedare@rtems.org>
- Lluc Alvarez <lluc.alvarez@bsc.es>
- Marco Elver <Marco.Elver@ARM.com>
- Mrinmoy Ghosh <mrinmoy.ghosh@arm.com>
- Nathanael Premillieu <nathanael.premillieu@arm.com>
- Rene de Jong <rene.dejong@arm.com>
- Stan Czerniawski <stan.czerniawski@arm.com>
- Tao Zhang <tao.zhang.0924@gmail.com>
- Umesh Bhaskar <umesh.b2006@gmail.com>
- Xiangyu Dong <rioshering@gmail.com>

#### 2012

- Andreas Hansson <andreas.hanson@arm.com>
  - Major port improvements
  - AddrRange
  - Traffic Generator
  - Simple DRAM controller
- Nilay Vaish <nilay@cs.wisc.edu>
  - Cache state checkpointing in Ruby
  - O3+Ruby updates
- Gabe Black <gabeblack@google.com>
  - unify SE and FS
- Ali Saidi <Ali.Saidi@arm.com>
- Andreas Sandberg <Andreas.Sandberg@arm.com>
- Brad Beckmann <brad.beckmann@amd.com>
- Steve Reinhardt <stever@gmail.com>
- Tony Gutierrez <anthony.gutierrez@amd.com>
- Dam Sunwoo <dam.sunwoo@arm.com>
- Chander Sudanthi <chander.sudanthi@arm.com>
- Geoffrey Blake <geoffrey.blake@arm.com>
- Joel Hestness <jthestness@gmail.com>
- Marc Orr <marc.orr@gmail.com>
- Nathanael Premillieu <nathanael.premillieu@arm.com>
- Jason Lowe-Power <jason@lowepower.com>
- Mrinmoy Ghosh <mrinmoy.ghosh@arm.com>
- Deyaun Guo <guodeyuan@tsinghua.org.cn>
- Jayneel Gandhi <jayneel@cs.wisc.edu>
- Nathan Binkert <nate@binkert.org>
- Brian Grayson <b.grayson@samsung.com>
- Djordje Kovacevic <djordje.kovacevic@arm.com>
- Koan-Sin Tan <koansin.tan@gmail.com>
- Lena Olson <leolson@google.com>
- Malek Musleh <malek.musleh@gmail.com>
- Matt Evans <matt.evans@arm.com>
- Uri Wiener <uri.wiener@arm.com>
- William Wang <william.wang@arm.com>
- Mitch Hayenga <mitch.hayenga@arm.com>
- Nuwan Jayasena <Nuwan.Jayasena@amd.com>
- Ron Dreslinski <rdreslin@umich.edu>
- Sascha Bischoff <sascha.bischoff@arm.com>
- Tushar Krishna <tushar@ece.gatech.edu>
- Vince Weaver <vince@csl.cornell.edu>
- Anders Handler <s052838@student.dtu.dk>
- Andrew Lukefahr <lukefahr@umich.edu>
- Erik Tomusk <E.Tomusk@sms.ed.ac.uk>
- Giacomo Gabrielli <giacomo.gabrielli@arm.com>
- Hamid Reza Khaleghzadeh <khaleghzadeh@gmail.com>
- James Clarkson <james.clarkson@arm.com>
- Krishnendra Nathella <Krishnendra.Nathella@arm.com>
- Lisa Hsu <Lisa.Hsu@amd.com>
- Lluc Alvarez <lluc.alvarez@bsc.es>
- Lluís Vilanova <vilanova@ac.upc.edu>
- Marco Elver <Marco.Elver@ARM.com>
- Matt Horsnell <matt.horsnell@arm.com>
- Maximilien Breughe <maximilien.breughe@elis.ugent.be>
- Min Kyu Jeong <minkyu.jeong@arm.com>
- Palle Lyckegaard <palle@lyckegaard.dk>
- Prakash Ramrakhyani <prakash.ramrakhyani@arm.com>
- Pritha Ghoshal <pritha9987@tamu.edu>

#### 2011

- Gabe Black <gabeblack@google.com>
- Korey Sewell <ksewell@umich.edu>
- Ali Saidi <Ali.Saidi@arm.com>
- Nilay Vaish <nilay@cs.wisc.edu>
- Steve Reinhardt <stever@gmail.com>
- Brad Beckmann <brad.beckmann@amd.com>
- Nathan Binkert <nate@binkert.org>
- Daniel Johnson <daniel.johnson@arm.com>
- Chander Sudanthi <chander.sudanthi@arm.com>
- Geoffrey Blake <geoffrey.blake@arm.com>
- Lisa Hsu <Lisa.Hsu@amd.com>
- Mrinmoy Ghosh <mrinmoy.ghosh@arm.com>
- Tushar Krishna <tushar@ece.gatech.edu>
- Chris Emmons <chris.emmons@arm.com>
- Deyaun Guo <guodeyuan@tsinghua.org.cn>
- Giacomo Gabrielli <giacomo.gabrielli@arm.com>
- Prakash Ramrakhyani <prakash.ramrakhyani@arm.com>
- Wade Walker <wade.walker@arm.com>
- Andreas Hansson <andreas.hanson@arm.com>
- Gabe Loh <gabriel.loh@amd.com>
- Gedare Bloom <gedare@rtems.org>
- Joel Hestness <jthestness@gmail.com>
- Mitch Hayenga <mitch.hayenga@arm.com>
- Thomas Grass <Thomas.Grass@ARM.com>
- Tony Gutierrez <anthony.gutierrez@amd.com>
