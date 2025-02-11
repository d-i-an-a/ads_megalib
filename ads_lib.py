import math
import requests
import json
import warnings
# https://astrothesaurus.org/
# https://github.com/astrothesaurus/UAT
# version 4.2.0
with open('UAT_list.json') as f:
    thesaurus = json.load(f)
    
uris = {}
for item in thesaurus:
    name = item['name']
    number = int(item['uri'].split('/')[-1])
    uris[number] = name

def journal_names():
    # from http://astro.dur.ac.uk/~cole/Intro_LaTeX_PG/PhDthesis/rcrain/aas_macros.sty

    short_name = {}
    long_name = {}

    short_name['\\aj'] = 'AJ'
    short_name['\\araa'] = 'ARA\&A'
    short_name['\\apj'] = 'ApJ'
    short_name['\\apjl'] = 'ApJ'
    short_name['\\apjs'] = 'ApJS'
    short_name['\\ao'] = 'Appl.~Opt.'
    short_name['\\apss'] = 'Ap\&SS'
    short_name['\\aap'] = 'A\&A'
    short_name['\\aapr'] = 'A\&A~Rev.'
    short_name['\\aaps'] = 'A\&AS'
    short_name['\\azh'] = 'AZh'
    short_name['\\baas'] = 'BAAS'
    short_name['\\jrasc'] = 'JRASC'
    short_name['\\memras'] = 'MmRAS'
    short_name['\\mnras'] = 'MNRAS'
    short_name['\\pra'] = 'Phys.~Rev.~A'
    short_name['\\prb'] = 'Phys.~Rev.~B'
    short_name['\\prc'] = 'Phys.~Rev.~C'
    short_name['\\prd'] = 'Phys.~Rev.~D'
    short_name['\\pre'] = 'Phys.~Rev.~E'
    short_name['\\prl'] = 'Phys.~Rev.~Lett.'
    short_name['\\pasp'] = 'PASP'
    short_name['\\pasj'] = 'PASJ'
    short_name['\\qjras'] = 'QJRAS'
    short_name['\\skytel'] = 'S\&T'
    short_name['\\solphys'] = 'Sol.~Phys.'
    short_name['\\sovast'] = 'Soviet~Ast.'
    short_name['\\ssr'] = 'Space~Sci.~Rev.'
    short_name['\\zap'] = 'ZAp'
    short_name['\\nat'] = 'Nature'
    short_name['\\iaucirc'] = 'IAU~Circ.'
    short_name['\\aplett'] = 'Astrophys.~Lett.'
    short_name['\\apspr'] = 'Astrophys.~Space~Phys.~Res.'
    short_name['\\bain'] = 'Bull.~Astron.~Inst.~Netherlands'
    short_name['\\fcp'] = 'Fund.~Cosmic~Phys.'
    short_name['\\gca'] = 'Geochim.~Cosmochim.~Acta'
    short_name['\\grl'] = 'Geophys.~Res.~Lett.'
    short_name['\\jcp'] = 'J.~Chem.~Phys.'
    short_name['\\jgr'] = 'J.~Geophys.~Res.'
    short_name['\\jqsrt'] = 'J.~Quant.~Spec.~Radiat.~Transf.'
    short_name['\\memsai'] = 'Mem.~Soc.~Astron.~Italiana'
    short_name['\\nphysa'] = 'Nucl.~Phys.~A'
    short_name['\\physrep'] = 'Phys.~Rep.'
    short_name['\\physscr'] = 'Phys.~Scr'
    short_name['\\planss'] = 'Planet.~Space~Sci.'
    short_name['\\procspie'] = 'Proc.~SPIE'
    # additional
    short_name['\\nar'] = 'New~Astr.~Rev.'
    short_name['\\na'] = 'New~Astr.'
    short_name['\\rmxaa'] = 'Rev.~Mexicana~de~Astron.~y~Astrof.'
    short_name['\\icarus'] = 'Icarus'
    short_name['\\pasa'] = 'PASA'
    short_name['\\jcap'] = 'JCAP'
    short_name['\\caa'] = 'ChA&A'

    long_name['\\aj'] = 'Astronomical Journal'
    long_name['\\araa'] = 'Annual Review of Astron and Astrophysics'
    long_name['\\apj'] = 'Astrophysical Journal'
    long_name['\\apjl'] = 'Astrophysical Journal, Letters'
    long_name['\\apjs'] = 'Astrophysical Journal, Supplement'
    long_name['\\ao'] = 'Applied Optics'
    long_name['\\apss'] = 'Astrophysics and Space Science'
    long_name['\\aap'] = 'Astronomy and Astrophysics'
    long_name['\\aapr'] = 'Astronomy and Astrophysics Reviews'
    long_name['\\aaps'] = 'Astronomy and Astrophysics, Supplement'
    long_name['\\azh'] = 'Astronomicheskii Zhurnal'
    long_name['\\baas'] = 'Bulletin of the AAS'
    long_name['\\jrasc'] = 'Journal of the RAS of Canada'
    long_name['\\memras'] = 'Memoirs of the RAS'
    long_name['\\mnras'] = 'Monthly Notices of the RAS'
    long_name['\\pra'] = 'Physical Review A: General Physics'
    long_name['\\prb'] = 'Physical Review B: Solid State'
    long_name['\\prc'] = 'Physical Review C'
    long_name['\\prd'] = 'Physical Review D'
    long_name['\\pre'] = 'Physical Review E'
    long_name['\\prl'] = 'Physical Review Letters'
    long_name['\\pasp'] = 'Publications of the ASP'
    long_name['\\pasj'] = 'Publications of the ASJ'
    long_name['\\qjras'] = 'Quarterly Journal of the RAS'
    long_name['\\skytel'] = 'ky and Telescope'
    long_name['\\solphys'] = 'Solar Physics'
    long_name['\\sovast'] = 'Soviet Astronomy'
    long_name['\\ssr'] = 'Space Science Reviews'
    long_name['\\zap'] = 'Zeitschrift fuer Astrophysik'
    long_name['\\nat'] = 'Nature'
    long_name['\\iaucirc'] = 'IAU Cirulars'
    long_name['\\aplett'] = 'Astrophysics Letters'
    long_name['\\apspr'] = 'Astrophysics Space Physics Research'
    long_name['\\bain'] = 'Bulletin Astronomical Institute of the Netherlands'
    long_name['\\fcp'] = 'Fundamental Cosmic Physics'
    long_name['\\gca'] = 'Geochimica Cosmochimica Acta'
    long_name['\\grl'] = 'Geophysics Research Letters'
    long_name['\\jcp'] = 'Journal of Chemical Physics'
    long_name['\\jgr'] = 'Journal of Geophysics Research'
    long_name['\\jqsrt'] = 'Journal of Quantitiative Spectroscopy and Radiative Transfer'
    long_name['\\memsai'] = 'Mem. Societa Astronomica Italiana'
    long_name['\\nphysa'] = 'Nuclear Physics A'
    long_name['\\physrep'] = 'Physics Reports'
    long_name['\\physscr'] = 'Physica Scripta'
    long_name['\\planss'] = 'Planetary Space Science'
    long_name['\\procspie'] = 'Proceedings of the SPIE'
    #
    long_name['\\nar'] = 'New Astronomy Review'
    long_name['\\na'] = 'New Astronomy'
    long_name['\\rmxaa'] = 'Revista Mexicana de Astronomia y Astrofisica'
    long_name['\\icarus'] = 'Icarus'
    long_name['\\pasa'] = 'Publications of the Astronomical Society of Australia'
    long_name['\\jcap'] = 'Journal of Cosmology and Astroparticle Physics'
    long_name['\\caa'] = 'Chinese Astronomy and Astrophysics'
    return short_name, long_name


def get_library(library_id, num_documents, config):
    # from https://github.com/adsabs/ads-examples/blob/master/library_csv/lib_2_csv.py
    """
    Get the content of a library when you know its id. As we paginate the
    requests from the private library end point for document retrieval,
    we have to repeat requests until we have all documents.
    :param library_id: identifier of the library
    :type library_id:
    :param num_documents: number of documents in the library
    :type num_documents: int
    :return: list
    """

    start = 0
    rows = 2000  # max number of list length from API
    num_paginates = int(math.ceil(num_documents / (1.0*rows)))
    documents = []
    for i in range(num_paginates):
        #print('Pagination {} out of {}'.format(i+1, num_paginates))

        r = requests.get(
            '{}/libraries/{id}?start={start}&rows={rows}'.format(
                config['url'],
                id=library_id,
                start=start,
                rows=rows
            ),
            headers=config['headers']
        )

        # Get all the documents that are inside the library
        try:
            data = r.json()['documents']
        except ValueError:
            raise ValueError(r.text)

        documents.extend(data)

        start += rows

    return documents

def adsresponse_to_dict(bib_received):
    list_bib = bib_received.split('@')[1:]
    #
    # store library into 2D dictionary
    records = {}
    for record in list_bib:
        row = [r.strip() for r in record.strip().split(',\n')]
        # Replace space in author names
        ads_key = row[0].replace(' ', '-')
        #
        if ads_key == '':
            pass
        else:
        # split values into dictionary
            temp_dict = {}
            for item in row[1:-1]:
                if 'author' in item:
                    items = item.split('author = ')
                    key = 'author'
                    value = items[1]                    
                elif 'title' in item:
                    items = item.split('title = ')
                    key = 'title'
                    value = items[1]    
                elif 'keywords = ' in item:
                    items = item.split('keywords = ')
                    key = 'keywords'
                    value = items[1]  
                else:
                    items = item.split(' =')
                    key, value = items[0], items[1]
                #
                #
                temp_dict[key.strip()]=value.strip()
                #
            records[ads_key] = temp_dict
    #
    return records

def fix_journal_abbr(bib_dict, format='short'):
    # 'short' prints abbreviated journal name; e.g. A&A, MNRAS, ApJ
    # 'long' prints full name; Astronomy & Astrophysics
    short_name, long_name = journal_names()
    #
    journal_dict = short_name
    if format == 'long':
        journal_dict = long_name
    #
    for item in bib_dict.keys():
        #
        try:
            e = bib_dict[item]['journal']
            #
            journal = e[1:-1] # remove '{', '}'
            if journal[0] == '\\':
                name = journal_dict[journal]
                new_name = '{' + name + '}'
                bib_dict[item]['journal'] = new_name
        except:
            warnings.warn(f"Warning: {item} has no 'Journal' keyword.")
    return bib_dict

def resolve_uat(code, thesaurus=uris):
    # look up the keyword code corresponding to the unified thesaurus
    # https://astrothesaurus.org/
    return thesaurus[code]
    
def add_keyword_tag(bib_dict, tag, only_ads=False):
    
    for item in bib_dict.keys():
        if only_ads:
            bib_dict[item]['keywords']= '{' + f'{tag}' + '}'
        else:
            if 'keywords' in bib_dict[item].keys():
                #
                keywords = bib_dict[item]['keywords'][1:-1] # remove '{', '}}
                key_str = keywords.split(',')
                #
                new_keys = []
                for k in key_str:
                    try:
                        code = int(k)
                        desc = resolve_uat(code)
                        new_keys.append(desc)
                    except:
                        new_keys.append(k)

                bib_dict[item]['keywords'] = '{'+f'{",".join(new_keys).lower()},{tag}'+'}'            
            else:
                bib_dict[item]['keywords']= '{' + f'{tag}' + '}'
        
    return bib_dict
    
def sanitise_multi(megalib):
    # megalib is a list of N dictionaries.
    # Find and merge multiple occurencies, keeping all tags

    Nlibs = len(megalib)   
    records = megalib[0]

    if Nlibs == 1:
        pass
    else:
        for lib in megalib[1:]:
            for lib_key, lib_value in lib.items():
                if lib_key in records.keys():
                    # merge keywords
                    # Ingore beginning and end brackets: "{},". 
                    # Don't replace them, as they can appear inside the text.
                    temp_keywords = lib[lib_key]['keywords'][1:-1].split(',')
                    old_keywords = records[lib_key]['keywords'][1:-1].split(',')
                    #
                    new_keywords = list(set(temp_keywords+old_keywords))
                    # update keywords with merged set
                    records[lib_key]['keywords'] = '{'+','.join(new_keywords)+'}'
                else:
                    records[lib_key] = lib_value
    return records

def dict_to_bib(records):
    # format for saving in .bib
    final_bib = ''
    for key1, value_dict in records.items():
        
        inner_str = ',\n'.join([f'{key2.rjust(16, " ")} = {value}' for key2, value in value_dict.items()])
        
        final_bib = final_bib + f'@{key1},\n{inner_str}'+'\n}\n\n'
    
    return final_bib
    
    
    
    
    
