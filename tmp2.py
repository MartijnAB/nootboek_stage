# CAS = ["88-18-6",
# "96-76-4",
# "98-54-4",
# "105-67-9",
# "106-44-5",
# "128-37-0",
# "128-39-2",
# "140-66-9",
# "576-26-1",
# "697-82-5",
# "2416-94-6",
# "4130-42-1",
# "120-80-9",
# "123-31-9",
# "700-13-0",
# "1948-33-0",
# "108-46-3",
# "108-73-6",
# "108-95-2",]
#
# pathwayQuery = '''SELECT ?CAS_nummer ?itemLabel (group_concat(?trivial_name ) as ?trivial_names )
# WHERE {
# VALUES ?CAS_nummer { '''+'"'+'" "'.join(CAS)+'"'+'''}
#   ?item wdt:P231 ?CAS_nummer  .
# OPTIONAL {?item skos:altLabel ?trivial_name  .}
# SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
# }
# group by ?CAS_nummer ?itemLabel'''
#
# print(pathwayQuery)



# code = """    def get_aid_filter(self): return self._aid_filter
#
#     def get_aeid_filter(self): return self._aeid_filter
#
#     def get_asid_filter(self): return self._asid_filter
#
#     def get_cell_formt_filter(self): return self._cell_formt_filter
#
#     def get_detection_technology_type_filter(self): return self._detection_technology_type_filter
#
#     def get_intended_target_family_filter(self): return self._intended_target_family_filter
#
#     def get_intended_target_type_filter(self): return self._intended_target_type_filter
#
#     def get_organism_filter(self): return self._organism_filter
#
#     def get_technological_target_type_filter(self): return self._technological_target_type_filter
#
#     def get_timepoint_hr_filter(self): return self._timepoint_hr_filter
#
#     def get_tissue_filter(self): return self._tissue_filter"""
#
#
# code = """    def get_chid_filter(self): return self._chid_filter
#
#     def get_clib_filter(self): return self._clib_filter
#
#     def get_dss_tox_q_c_level_filter(self): return self._dss_tox_q_c_level_filter
#
#     def get_substances_type_filter(self): return self._substances_type_filter"""
#
#
# code = """    def get_result_id_filter(self): return self._result_id_filter
#
#     def get_hitc_filter(self): return self._hitc_filter"""
# x = ""
#
# for iets in code.split("\n"):
#     # print(iets.split())
#     try:
#         # print(iets.split()[1][:-7])
#         x += "self." + iets.split()[1][:-7] + ", "
#         print(x)
#     except:
#         pass

    # self.get_aid_filter, self.get_aeid_filter, self.get_asid_filter, self.get_cell_formt_filter, self.get_detection_technology_type_filter, self.get_intended_target_family_filter, self.get_intended_target_type_filter, self.get_organism_filter, self.get_technological_target_type_filter, self.get_timepoint_hr_filter, self.get_tissue_filter,

print(__name__)
def testen():
    print(testen.__name__)
testen()

# import copy

class ChemicalCompound():
    """
    A chemical compound is a chemical substance
    composed of many identical molecules (or molecular entities) composed of atoms from more than one element
    held together by chemical bonds.

    22-01-2019
    https://en.wikipedia.org/wiki/Chemical_compound

    """

    def __init__(self):
        self._cas = None
        self._wikidata = None

        self._trivial_names = set()
        self._wikidata_own_trivial_name = None

        self._is_chemicalcompound = False

        self._one_required = [ChemicalCompound.getcas, ChemicalCompound.getwikidata]


    def _ischemicalcompound(self, because=False):
        if self._is_chemicalcompound and not because:
            return True
        because_return = []
        for required in self._one_required:
            try:
                required(self)
                self._is_chemicalcompound = True
                if because:
                    because_return += [required]
                else:
                    return True
            except LookupError:
                pass
        if not because_return:
            return False
        else:
            return because_return


    def _add(self, variable, information):
        if variable:
            print("you tried to overwrite the following information:\n" + str(variable))
            print("\nwith\n" + str(information) + "\nthe program will now terminate")
            exit(1)
        if not information:
            print("you tried to only delete " + str(information))
            exit(1)

    def _get(self, info, variable):
        if variable:
            return variable
        else:
            raise LookupError(info + "has not been add")


    def addcas(self, cas_id):
        self._add(self._cas, cas_id)
        self._cas = cas_id

    def getcas(self): return self._get("cas", self._cas)

    def addwikidata(self, wikidata_id):
        self._add(self._wikidata, wikidata_id)
        self._wikidata = wikidata_id

    def getwikidata(self): return self._get("wikidata", self._wikidata)

    def addtrivialnames(self, the_trivial_names):
        self._trivial_names.update(the_trivial_names)

    def gettrivialnames(self): return self._get("trivialnames", self._trivial_names)

    def addwikidataowntrivialname(self, the_trivial_name):
        self._add(self._wikidata_own_trivial_name, the_trivial_name)
        self._wikidata_own_trivial_name =

    def getwikidataowntrivialname(self): return self._get("trivialnames", self._trivial_names)

class StoredChemicalCompounds():

    def __init__(self):
        self._chemical_compounds = []
        self._iteration_ = 0

    def __add__(self, other):
        if other._ischemicalcompound():
            for required in other._ischemicalcompound(True):
                try:
                    self._select_by(required, required(other))
                    print("al redie added " + str(required(other)))
                    exit(1)
                except LookupError:
                    pass
            self._chemical_compounds += [other]
        else:
            print("chemical miss proper definition")
            exit(1)

    def __iter__(self):
        return self

    def __next__(self):
        if self._iteration_ >= len(self._chemical_compounds):
            self._iteration_ = 0
            raise StopIteration
        else:
            self._iteration_ += 1
            return self._chemical_compounds[self._iteration_ - 1]

    def _select_by(self, fuc, var):
        for compound in self._chemical_compounds:
            if fuc(compound) == var:
                return compound
        raise LookupError("not found " + str(var))

    def selectbycas(self, cas): return self._select_by(ChemicalCompound.getcas, cas)

    def selectbywikidata(self, wikidata): return self._select_by(ChemicalCompound.getwikidata, wikidata)



the_compounds = StoredChemicalCompounds()

#///////////////////////////////////////////////////////////////////////////////
import requests
import re
import pandas
from SPARQLWrapper import SPARQLWrapper, JSON

urla = "http://bridgedb.prod.openrisknet.org/Human/xrefs/Ca/"
urlb = "?dataSource=Wikidata"
urlc = "?dataSource=ChEBI"
tggatesconvert = 'http://open-tggates-api.cloud.douglasconnect.com/v2/'


CAS = ["103-90-2",
"88-18-6",
"96-76-4",
"98-54-4",
"105-67-9",
"106-44-5",
"128-37-0",
"128-39-2",
"140-66-9",
"576-26-1",
"697-82-5",
"2416-94-6",
"4130-42-1",
"120-80-9",
"123-31-9",
"700-13-0",
"1948-33-0",
"108-46-3",
"108-73-6",
"108-95-2",]

#///////////////////////////////////////////////////////////////////////////////

# for cas_id in CAS:
#     compound = ChemicalCompound()
#     compound.addcas(cas_id)
#     compound.addwikidata(requests.get(urla + cas_id + urlb).text.split("\t")[0])
#     # print(compound._ischemicalcompound())
#     # exit()
#     the_compounds.__add__(compound)
#     # compounds += [compound]
# print(the_compounds._chemical_compounds)
# # exit()
#
# for compound in the_compounds:
#     print(compound)
#     # exit()
#     print(compound.getcas() + "  " + compound.getwikidata())
#
# for i, compound in enumerate(the_compounds):
#     print(str(i)+" "+str(compound))

# exit()

test = ChemicalCompound()
# print(test.getcas())
# print(test.getwikidata())

# exit()
print(test._ischemicalcompound())
test.addcas(2)
print(test._ischemicalcompound())
test.addwikidata("onzin")
print(test._ischemicalcompound())
# exit()
print(test.getcas())
print(test.getwikidata())
print(test._ischemicalcompound())
the_compounds.__add__(test)
# gek = ChemicalCompound()
# gek.addcas("testen")
# the_compounds.__add__(gek)
gek2 = ChemicalCompound()
gek2.addcas("testen")
the_compounds.__add__(gek2)
print(the_compounds)
print(the_compounds._chemical_compounds)




# intersand = the_compounds.selectbycas("testen")
# # print(the_compounds.selectbycas("testdden"))
print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
# print(intersand._cas)
# print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
# print(intersand._wikidata)
# print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
# print(intersand.getcas())
# print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
# # print(intersand.getwikidata())
# # print(the_compounds.selectbywikidata("wikieatat er bij"))
# intersand.addwikidata("wikieatat er bij")
# print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
# print(intersand._cas)
# print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
# print(intersand._wikidata)
# print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
# print(intersand.getcas())
# print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
# print(intersand.getwikidata())
# print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
# print(the_compounds.selectbywikidata("wikieatat er bij").getcas())

# print(the_compounds.selectbywikidata("probeeren"))
# the_compounds.selectbycas("testen").addwikidata("probeeren")
# print(the_compounds.selectbycas("testen").getcas())
# print(the_compounds.selectbycas("testen").getwikidata())
# print(the_compounds.selectbywikidata("probeeren").getcas())
# print(the_compounds.selectbywikidata("probeeren").getwikidata())
# print(intersand.getcas())
# intersand.addwikidata("wikieatat er bij")
# print(intersand.getwikidata())
# print(the_compounds.selectby("wikieatat er bij"))


the_compounds.selectbycas("testen").addtrivialnames(["adfsdf", "sdfjklasdjklsdfjkl"])
print(the_compounds.selectbycas("testen").gettrivialnames())


