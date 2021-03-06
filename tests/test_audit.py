# from tests import factories
# from tests.common import ApiBaseTest
# from webservices.common.models import AuditCase
# from webservices.resources.audit import AuditCaseView
# from webservices.schemas import AuditCaseSchema
# from webservices.rest import api
from tests import factories
from tests.common import ApiBaseTest
from webservices.resources.costs import CommunicationCostView
from webservices.schemas import CommunicationCostSchema
from webservices.rest import api

class TestAudit(ApiBaseTest):

    def test_fields(self):
        factories.CommunicationCostFactory()
        results = self._results(api.url_for(CommunicationCostView))
        assert len(results) == 1
        assert results[0].keys() == CommunicationCostSchema().fields.keys()

   # def test_filters_audit_case_id(self):
    #     filters = [
    #         ('audit_case_id', AuditCase.audit_case_id, '1'),
    #     ]
    #     for label, column, values in filters:
    #         [
    #             factories.AuditCaseFactory(**{column.key: value})
    #             for value in values
    #         ]
    #         results = self._results(api.url_for(AuditCaseView, **{label: values[0]}))
    #         print("results :::", results)
    #         assert len(results) == 1
    #         assert results[0][column.key] == values[0]

    # def test_filters_audit_case_id(self):
    #     filters = [
    #         ('audit_case_id', AuditCase.audit_case_id, '1'),
    #     ]
    #     for label, column, values in filters:
    #         [
    #             factories.AuditCaseFactory(**{column.key: value})
    #             for value in values
    #         ]
    #         results = self._results(api.url_for(AuditCaseView, **{label: values[0]}))
    #         print("results :::", results)
    #         assert len(results) == 1
    #         assert results[0][column.key] == values[0]

    # def test_fields(self):
    #     factories.AuditCaseFactory()
    #     results = self._results(api.url_for(AuditCaseView, {'primary_category_id': -1, 'sub_category_Id': -2}))
    #     print('results :::', results)
    #     assert len(results) == 1
    #     assert results[0].keys() == AuditCaseSchema().fields.keys()

    # def test_sort(self):
    #     [
    #         factories.AuditCaseFactory(audit_case_id=4),
    #         factories.AuditCaseFactory(audit_case_id=3),
    #         factories.AuditCaseFactory(audit_case_id=2),
    #         factories.AuditCaseFactory(audit_case_id=1),
    #     ]
    #     results = self._results(api.url_for(AuditCaseView, sort='audit_case_id'))
    #     self.assertTrue(
    #         [each['audit_case_id'] for each in results],
    #         [1, 2, 3, 4]
    #)
