#!/usr/bin/env python3

def get_authors():
    entries = {}

    with open('author-list.tex') as f:
        d = f.readlines()
        e = ''
        author = ''
        num = 0
        for line in d:
            num += 1
            if line.startswith('%'):
                # Comments at the end.
                break
            if not line.strip():
                # blank line between entries
                #print(f"On line number {num}: '{line[:-1]}'")
                assert(author != '')
                entries[author] = e
                e = ''
                author = ''
                continue
            if not author:
                # first line of the block is the author's name
                assert(line.startswith('\\author{'))
                author = line[8:-2].split(' ')[-1]
                print(f"Found {author}")
            e += line

    return entries

def sort_authors():

    entries = get_authors()

    print(f"Found {len(entries)} authors")

    with open('new-list.tex', 'w') as f:
        f.write('\n')
        f.write(entries['Lowe-Power'])
        f.write('\n')
        del entries['Lowe-Power']

        for author,entry in sorted(entries.items()):
            f.write(entry)
            f.write('\n')

def create_acks():
    all_authors = [
        'Gabe Black',
        'Andreas Hansson',
        'Andreas Sandberg',
        'Nilay Vaish',
        'Giacomo Travaglini',
        'Daniel Rodrigues Carvalho',
        'Nikos Nikoleris',
        'Ali Saidi',
        'Steve Reinhardt',
        'Brandon Potter',
        'Curtis Dunham',
        'Tony Gutierrez',
        'Jason Lowe-Power',
        'Korey Sewell',
        'Bobby R. Bruce',
        'Ciro Santilli',
        'Mitch Hayenga',
        'Adrian Herrera',
        'Alec Roelke',
        'Brad Beckmann',
        'Joel Hestness',
        'Geoffrey Blake',
        'David Hashe',
        'Gabor Dozsa',
        'Javier Bueno Hedo',
        'Tiago Mück',
        'Andrew Bardsley',
        'Sean Wilson',
        'Tuan Ta',
        'Alexandru Dutu',
        'Dam Sunwoo',
        'Sascha Bischoff',
        'Giacomo Gabrielli',
        'Nils Asmussen',
        'Stephan Diestelhorst',
        'Chun-Chen Hsu',
        'Rekai Gonzalez-Alberquilla',
        'Andrea Mondelli',
        'Matthew Poremba',
        'Radhika Jagtap',
        'Christian Menard',
        'Bjoern A. Zeeb',
        'Anouk Van Laer',
        'Pau Cabre',
        'Wendy Elsasser',
        'Dylan Johnson',
        'Michael LeBeane',
        'David Guillen-Fandos',
        'Nathanael Premillieu',
        'Pouya Fotouhi',
        'Timothy Hayes',
        'Tushar Krishna',
        'Jordi Vaquero',
        'Lena E. Olson',
        'Chander Sudanthi',
        'Jose Marinho',
        'Omar Naji',
        'Akash Bagdia',
        'Chuan Zhu',
        'Matteo Andreozzi',
        'Syed Ali Raza Jafri',
        'Jairo Balart',
        'Nathan Binkert',
        'Malek Musleh',
        'Matthias Jung',
        'Gedare Bloom',
        'Marc Orr',
        'Marco Elver',
        'Mrinmoy Ghosh',
        'Ryan Gambord',
        'Ayaz Akram',
        'Deyaun Guo',
        'Glenn Bergmans',
        'Matt Evans',
        'Peter Enns',
        'Abdul Mutaal Ahmad',
        'Chris Emmons',
        'Hanhwi Jang',
        'Ian Jiang',
        'Joe Gross',
        'Matthew Horsnell',
        'Prakash Ramrakhyani',
        'Andrew Lukefahr',
        'Ani Udipi',
        'Javier Setoain',
        'Neha Agarwal',
        'Siddhesh Poyarekar',
        'Yasuko Eckert',
        'Arthur Perais',
        'Austin Harris',
        'Boris Shingarov',
        'Earl Ou',
        'Faissal Sleiman',
        'Hoa Nguyen',
        'Ivan Pizarro',
        'Matthew D. Sinclair',
        'Paul Rosenfeld',
        'Rahul Thakur',
        'Robert Kovacsics',
        'Timothy M. Jones',
        'Uri Wiener',
        'Binh Pham',
        'Daniel Johnson',
        'Emilio Castillo',
        'Erfan Azarkhish',
        'Jayneel Gandhi',
        'Lisa Hsu',
        'Marco Balboni',
        'Michiel Van Tol',
        'Mohammad Alian',
        'Palle Lyckegaard',
        'Rico Amslinger',
        'Ruslan Bukin',
        'Srikant Bharadwaj',
        'Sudhanshu Jha',
        'Swapnil Haria',
        'Tommaso Marinelli',
        'Yu-hsin Wang',
        'Adrien Pesle',
        'Amin Farmahini-Farahani',
        'Bradley Wang',
        'Brian Grayson',
        'Christopher Torng',
        'Djordje Kovacevic',
        'Eric Van Hensbergen',
        'Hsuan Hsu',
        'Isaac Sánchez Barrera',
        'Jing Qu',
        'Jiuyue Ma',
        'John Kalamatianos',
        'Koan-Sin Tan',
        'Lluís Vilanova',
        'Mahyar Samani',
        'Rene de Jong',
        'Stan Czerniawski',
        'William Wang',
        'Éder F. Zulian',
        'Adrià Armejach',
        'Bertrand Marquis',
        'Blake Hechtman',
        'Cagdas Dirik',
        'Dibakar Gope',
        'Edmund Grimley-Evans',
        'Jan-Peter Larsson',
        'Javier Cano-Cano',
        'Jieming Yin',
        'John Alsop',
        'Jui-min Lee',
        'Kanishk Sugand',
        'Karthik Sangaiah',
        'Kevin Brodsky',
        'Krishnendra Nathella',
        'Lluc Alvarez',
        'Marc Mari Barcelo',
        'Matthias Hille',
        'Maurice Becker',
        'Michael Adler',
        'Michael Levenhagen',
        'Mingyuan',
        'Moyang Wang',
        'Nuwan Jayasena',
        'Pin-Yen Lin',
        'Reiley Jeyapaul',
        'Riken Gohil',
        'Rizwana Begum',
        'Rohit Kurup',
        'Ron Dreslinski',
        'Rune Holm',
        'Sandipan Das',
        'Sherif Elhabbal',
        'Stanislaw Czerniawski',
        'Trivikram Reddy',
        'Victor Garcia',
        'Vince Weaver',
        'Wade Walker',
        'Weiping Liao',
        'Xiangyu Dong',
        'Xiaoyu Ma',
        'Yuetsu Kodama',
        'ARM gem5 Developers',
        'Anders Handler',
        'Andrea Pellegrini',
        'Andriani Mappoura',
        'Anis Peysieux',
        'Ashkan Tousi',
        'Avishai Tvila',
        'Bagus Hanindhito',
        'Chen Zou',
        'Chris Adeniyi-Jones',
        'Christoph Pfister',
        'Dongxue Zhang',
        'Doğukan Korkmaztürk',
        'Erik Tomusk',
        'Fernando Endo',
        'Gabe Loh',
        'Georg Kotheimer',
        'Hamidreza Khaleghzadeh',
        'Hongil Yoon',
        'Hussein Elnawawy',
        'Ilias Vougioukas',
        'Isaac Richter',
        'Jakub Jermar',
        'James Clarkson',
        'Khalique',
        'Marjan Fariborz',
        'Mark Hildebrand',
        'Matteo M. Fusi',
        'Maxime Martinasso',
        'Maximilian Stein',
        'Maximilien Breughe',
        'Michael Upton',
        'Min Kyu Jeong',
        'Monir Mozumder',
        'Nayan Deshmukh',
        'Nicholas Lindsay',
        'Nicolas Derumigny',
        'Ola Jeppsson',
        'Pablo Prieto',
        'Po-Hao Su',
        'Polydoros Petrakis',
        'Pritha Ghoshal',
        'Ricardo Alves',
        'Robert Scheffel',
        'Ruben Ayrapetyan',
        'Rutuja Oza',
        'Samuel Grayson',
        'Santi Galan',
        'Sean McGoogan',
        'Sergei Trofimov',
        'Severin Wischmann',
        'Shawn Rosti',
        'Sooraj Puthoor',
        'Sophiane Senni',
        'Stian Hvatum',
        'Sujay Phadke',
        'Tao Zhang',
        'Thomas Grass',
        'Tom Jablin',
        'Umesh Bhaskar',
        'Willy Wolff',
        'Xianwei Zhang',
        'Xin Ouyang',
        'Yifei Liu',
        'Yuan Yao',
        'Zhang Zheng',
        'Zicong Wang',
        'Jiajie Chen',
        'Zhengrong Wang',
        'Chris Adeniyi-Jones',
        'Mbou Eyole',
        'Thomas Grocutt',
    ]

    entries = get_authors()
    for e in entries.values():
        name = e.split('\n')[0][8:-1]
        if name in all_authors:
            del all_authors[all_authors.index(name)]
        else:
            print(f"Could not find {name}")

    print(', '.join(sorted(all_authors, key=lambda i: i.split(' ')[-1])))

def print_authors():
    entries = get_authors()
    for e in entries.values():
        name = e.split('\n')[0][8:-1]
        print(name, end=',')

if __name__=="__main__":
    pass
