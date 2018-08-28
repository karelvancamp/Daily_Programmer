## Definitions

Given two different strings of equal length, the spacing between them is the number of other strings you would need to connect them on a word ladder. Alternately, this is 1 less than the number of letters that differ between the two strings. Examples:

    spacing("shift", "shirt") => 0
    spacing("shift", "whist") => 1
    spacing("shift", "wrist") => 2
    spacing("shift", "taffy") => 3
    spacing("shift", "hints") => 4

The total spacing of a word list is the sum of the spacing between each consecutive pair of words on the word list, i.e. the number of (not necessarily distinct) strings you'd need to insert to make it into a word ladder. For example, the list:

    daily
    doily
    golly
    guilt

has a total spacing of 0 + 1 + 2 = 3

## Challenge

Given an input list of unique words and a maximum total spacing, output a list of distinct words taken from the input list. The output list's total spacing must not exceed the given maximum. The output list should be as long as possible.

You are allowed to use existing libraries and research in forming your solution. (I'm guessing there's some graph theory algorithm that solves this instantly, but I don't know it.)

#### Example input

    abuzz
    carts
    curbs
    degas
    fruit
    ghost
    jupes
    sooth
    weirs
    zebra

Maximum total spacing: 10

#### Example output

The longest possible output given this input has length of 6:

    zebra
    weirs
    degas
    jupes
    curbs
    carts

#### Challenge input

This list of 1000 4-letter words randomly chosen from enable1.

Maximum total spacing of 100.

My best solution has a length of 602. How much higher can you get?

#### Best solution I found:

Length 822

#### Method

- Calculate spacing distances
- Remove isolated nodes (no 0 cost edges)
- Remove cliques size 2 which have a node in upper average distance.
 Use binary search to find optimal cutoff value these
 - Run TSP-solver on leftover nodes
 - Find lowest cost subsection (lowest moving sum)

#### Found solution

'used uses oses ones obes obis ywis iwis imps amps asps nips lips libs gibs gies gaes gabs jabs sabs says sals salp salt malt mall mull mule mole sole soli shri sari sadi sago dago dado dude duke dyke dike dime mime time tome tame lame lane sane safe gaff caff waff luff puff tuff tuft tufa tuna luna luny lune tune tung hung sung sunn sunk gunk punk puck yuck tuck tick lick lice fice fico piso miso mist wist wisp hiss kiss kifs kids kirs kits kite kine kino kink oink hind rind rand wand vend vent cent rent sent sene gene gone gane mane mano many mony moly molt mott mote dote doge dope nope mope more kore nori nodi nods yods yobs yows yowe poke pole pele hebe heme heck keck kept wept weft left loft coft soft sift gift girt airt airn aura jura jury fury fumy mumm mumu muni mini minx miff biff tiff teff toff tofu doff dons dong gong bong song sang bang bung bund buns buys buss bugs buts butt bute byte ante ants ands anas anal anil deil heil hail harl farl furl burl purl purs pugs pugh push tush hush hash hasp harp tarp tare tyre tyro tiro tirl wiry wary warm barm farm fard fare fere cere cero cete cute cuts cuss fuss foss coss coos coys joys jots jota iota bota bots both beth bath lath late gate gave gyve neve nevi nest pest psst post wost wort sort sorn sown mown moan moat doat goat goal load road roar rear pear peag neap heap heat beat beam seam snap snag slag slay spay spaz soak sook soot boot boor boob bomb bogy dogy doxy foxy fozy oozy dozy cozy cory coly cold cola mola kola kolo mozo mojo lobo lobe love lose hose nosy rosy posy pony tony tory torr tort toit trim grim gram pram prao prat plat play pray fray tray trad trod trop wrap crap clap clop plop plod plus plum slum scum scud yaud yaup jaup jauk wauk waur gaur gaun lawn lain kain rain cain vain vail kail fail tail tael twee tree bree gree free flee flog frog snog snug smug emus ecus ekes okes okeh oxen omen omer eyer dyer deer weer jeer leer peer peel keel reel reek geek geed deed teed toed toes voes vies dies diet duet duel dull doll boll bill bilk bulk hulk murk mark marc maya raya rays lays ways days kays kafs oafs oaks daks dals dale bale gale gala gulp gull gill yill yell cell celt gelt felt feat pert part pare para vara java fava nada nana nona none zone zonk zing ting tint lint liny viny vina viga mica pica pina puna pupa plea olea olla ally alls albs alba alma alme aloe sloe syce sice site sith sits sims sins yins ains rins bins bine bize bike bile rile rill rial sial sibb jibb jimp limp lamp gamp gapy gaby goby gobo gogo gout pout phut phat what cham chay chaw craw braw bros bras eras urbs arbs arfs aria arid acid amid aped abed abet leet deet debt deny dewy dews dees zees yeas yens tens hens huns nuns nans nabs nabe wake ware yare rare rase vase lase lyse eyne syne sync wyns wins wigs bigs zigs zags zaps maps macs maes mads muds suds sums sumo such ouch orcs orca orra okra lira lire life lite wite nite nixe nide vide ride ripe rite ritz ditz dits pits pics pigs rigs gigs migs mils oils olds elds elks ilks ills ells eels mels mems mess moss mocs rocs rock yock mock jock jack lack lacs lace tace tape taps tads pads pals paly pily pili pill will wall wawl waws waps baps bams baas boas koas kbar kyar kyak dyad dead dean hwan swan scan scab slub snub spun stun stey stew slew skew skeg skip slip flip flit flat flak flam film fila file fine five hive hire sire cire cure curt hurt yurt just rust oust oast east wast vast bast bait brin brig drib drub daub caul call calk talk talc tali raki rami ragi magi mage maze mazy hazy haze hade jade lade made mode code rode rote roti loti lots tots cots cats pats mats qats vats kats kata kaka kaph koph qoph gosh posh pash dash bash bask mask yank dank dark sark bark barn darn durn curn curb carb card bard lard lari lars gars gats guts gets vets jets jess cess ceps peps feds fets lets legs begs beys deys devs revs rees rues dues duos dubs dups sups sops oops lops wops wogs jogs jigs jugs lugs mugs vugs vugg nogg hogg hogs hods hows bows pows pois paid said sain shin whin when wren prez prep peep weep weed weld wild gild sild silt jilt riot'

