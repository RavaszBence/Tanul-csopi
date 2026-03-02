szöveg = str("A Megadeth amerikai thrash metal együttes, melynek vezetője az alapító, gitáros, frontember, dalszerző Dave Mustaine. Az együttes 1983-ban alakult, miután Mustaine távozott a Metallicából. Mint az amerikai thrash metal mozgalom egyik úttörő együttese, a Megadeth az 1980-as években szerzett nemzetközi hírnevet, de folyamatos tagcserék sújtották, részben a tagok közismert kábítószerproblémái miatt. A megtisztulást és a stabil felállást követően a Megadeth platina- és aranylemezek sorát jelentette meg, köztük a Grammy-díjra jelölt, 1992-es, dupla platina Countdown to Extinction nagylemezt. A Megadeth 2002-ben oszlott fel, miután Mustaine komoly idegkárosodást szenvedett a bal karjára, de az átfogó fizioterápiának köszönhetően 2004-ben Mustaine újjáalakította az együttest, és kiadta a The System Has Failed albumot, amely a Billboard 200-as albumlistájának 18. helyén debütált. Ezt követte a 2007-es United Abominations nagylemez, amely ugyanezen a listán a 8. helyen startolt. Legutóbbi albumuk a 2016-ban megjelent Dystopia, melynek címadó dala Grammy-díjat kapott a Best Metal Performance kategóriában az 59. díjátadón.[5] A Megadeth jellegzetes gitárstílusáról ismert, gyakran használnak komplex, bonyolult zenei átkötéseket és váltásokkal teli gitárszólókat. Mustaine szintén ismert sajátos „vicsorgó” énekstílusáról, akárcsak visszatérő dalszövegtémáiról mint a politika, háború, függőség és emberi kapcsolatok. Mint a kereskedelmileg egyik legsikeresebb heavy metal zenekar, a Megadeth több mint 50 millió albumot adott el világszerte,[6][7] és eddig összesen 12 alkalommal jelölték őket Grammy-díjra a Best Metal Performance kategóriában. Több mint három évtizedes pályafutása alatt a Megadethnek több mint húsz hivatalos tagja volt, de a zenekar motorja, fő dalszerzője és egyetlen eredeti tagja mindig Dave Mustaine maradt. A Megadethet a Metallicával, a Slayerrel és az Anthraxszel együtt mint a thrash metal „nagy négyesét” tartják számon.")

butus_jelek = [".", ",", "[", "]", "(", ")"]

for jel in butus_jelek:
    szöveg = szöveg.replace(jel, "")
    
szavak = szöveg.split() # szóköz mentén szedi szét a szöveget

for szó in szavak:
    print(szó) # egymás alá  a szavak lista bejárássasl

db = 0
if "\n" in szöveg:
    db += 1
print(db)

