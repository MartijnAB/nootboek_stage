
class _Swagger_Toxcast:

    def __init__(self):
        self._offset = "c"
        self._limit = None
        self._query = None

        self._urel = "https://toxcast-api.cloud.douglasconnect.com/beta/"

    def set_offset(self, x): self._offset = x

    def set_limit(self, x): self._limit = x

    def set_query(self, x): self._query = x


    def get_offset(self): return  self._offset

    def get_limit(self): return self._limit

    def get_query(self): return self._query

    def _meke_url_(self, x):
        text = ""
        for i in x:
            if i():
                text += "?" + i.__name__[4:] + "=" + str(i())
            else:
                pass
        return text

    def get_url(self):
        return self._meke_url_([self.get_offset, self.get_limit, self.get_query])

class _Assays_results(_Swagger_Toxcast):

    def __init__(self):
        super().__init__()
        self._aid_filter = "b"
        self._aeid_filter = None
        self._asid_filter = None
        self._cell_formt_filter = None
        self._detection_technology_type_filter = None
        self._intended_target_family_filter = None
        self._intended_target_type_filter = None
        self._organism_filter = None
        self._technological_target_type_filter = None
        self._timepoint_hr_filter = None
        self._tissue_filter = None


    def set_aid_filter(self, x): self._aid_filter = x

    def set_aeid_filter(self, x): self._aeid_filter = x

    def set_asid_filter(self, x): self._asid_filter = x

    def set_cell_formt_filter(self, x): self._cell_formt_filter = x

    def set_detection_technology_type_filter(self, x): self._detection_technology_type_filter = x

    def set_intended_target_family_filter(self, x): self._intended_target_family_filter = x

    def set_intended_target_type_filter(self, x): self._intended_target_type_filter = x

    def set_organism_filter(self, x): self._organism_filter = x

    def set_technological_target_type_filter(self, x): self._technological_target_type_filter = x

    def set_timepoint_hr_filter(self, x): self._timepoint_hr_filter = x

    def set_tissue_filter(self, x): self._tissue_filter = x



    def get_aid_filter(self): return self._aid_filter

    def get_aeid_filter(self): return self._aeid_filter

    def get_asid_filter(self): return self._asid_filter

    def get_cell_formt_filter(self): return self._cell_formt_filter

    def get_detection_technology_type_filter(self): return self._detection_technology_type_filter

    def get_intended_target_family_filter(self): return self._intended_target_family_filter

    def get_intended_target_type_filter(self): return self._intended_target_type_filter

    def get_organism_filter(self): return self._organism_filter

    def get_technological_target_type_filter(self): return self._technological_target_type_filter

    def get_timepoint_hr_filter(self): return self._timepoint_hr_filter

    def get_tissue_filter(self): return self._tissue_filter

    def get_url(self, x=True):
        assays_results_url = self._meke_url_([self.get_aid_filter, self.get_aeid_filter, self.get_asid_filter, self.get_cell_formt_filter, self.get_detection_technology_type_filter, self.get_intended_target_family_filter, self.get_intended_target_type_filter, self.get_organism_filter, self.get_technological_target_type_filter, self.get_timepoint_hr_filter, self.get_tissue_filter])
        if x:
            return assays_results_url + _Swagger_Toxcast.get_url(self)
        else:
            return assays_results_url


class _Compounds_results(_Swagger_Toxcast):

    def __init__(self):
        super().__init__()
        self._chid_filter = "e"
        self._clib_filter = None
        self._dss_tox_q_c_level_filter = None
        self._substances_type_filter = None


    def set_chid_filter(self, x): self._chid_filter = x

    def set_clib_filter(self, x): self._clib_filter = x

    def set_dss_tox_q_c_level_filter(self, x): self._dss_tox_q_c_level_filter = x

    def set_substances_type_filter(self, x): self._substances_type_filter = x


    def get_chid_filter(self): return self._chid_filter

    def get_clib_filter(self): return self._clib_filter

    def get_dss_tox_q_c_level_filter(self): return self._dss_tox_q_c_level_filter

    def get_substances_type_filter(self): return self._substances_type_filter

    def get_url(self, x=True):
        compounds_results_url = self._meke_url_([self.get_chid_filter, self.get_clib_filter, self.get_dss_tox_q_c_level_filter, self.get_substances_type_filter])
        if x:
            return compounds_results_url + _Swagger_Toxcast.get_url(self)
        else:
            return compounds_results_url



class _Assays(_Assays_results):

    def __init__(self):
        super().__init__()


    def run_assays(self): return self._urel + "assays" + _Assays.get_url(self)

class _Compounds(_Compounds_results):

    def __init__(self):
        super().__init__()

    def run_compounds(self):
        return self._urel + "compounds" + _Compounds_results.get_url(self)

class _Results(_Assays_results, _Compounds_results):

    def __init__(self):
        super().__init__()
        self._result_id_filter = "a"
        self._hitc_filter = "bliep"


    def set_result_id_filter(self, x): self._result_id_filter = x

    def set_hitc_filter(self, x): self._hitc_filter = x


    def get_result_id_filter(self): return self._result_id_filter

    def get_hitc_filter(self): return self._hitc_filter

    def _get_url(self):
        return self._meke_url_([self.get_result_id_filter, self.get_hitc_filter])


    def run_results(self): return self._urel + "results" + _Assays_results.get_url(self, False) + self._get_url() + _Compounds_results.get_url(self)




class Toxcast(_Results, _Assays, _Compounds):

    def __init__(self):
        super().__init__()
        self.probeer = "testen"

test = Toxcast()
print(test.probeer)
# print(test._result_id_filter)
print(test.get_result_id_filter())
print(test.get_aid_filter())
print(test.get_offset())
print(test.get_chid_filter())
print(test.run_assays())

print(test.run_compounds())
# test.set_hitc_filter("grappig?")
print(test.run_results())