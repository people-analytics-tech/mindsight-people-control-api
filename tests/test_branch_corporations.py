from mindsight_people_control_api.scripts.branch_corporations import BranchCorporations
from mindsight_people_control_api.scripts.corporations import Corporations

new_branch_corporation = {}
corporation_global = {}
class TestBranchCorporationRequests:
    
    branch_corporations_client = BranchCorporations()
    corporations_client = Corporations()

    def test_post_create_branch_corporation(self):
        global new_branch_corporation 
        global corporation_global 

        corporation = self.corporations_client.get_list_corporations().results

        if not corporation:
            corporation = self.corporations_client.post_create_corporation(
                code="23", name="StoneTest"
            )
        else:
            corporation = corporation[0]

        corporation_global = corporation

        post_branch_corporation = (
            self.branch_corporations_client.post_create_branch_corporation(
                code="post", name="StoneFilialTeste", corporation_id=corporation_global["code"]
            )
        )
        new_branch_corporation = post_branch_corporation
        assert isinstance(post_branch_corporation , dict)

    def test_get_list_corporations(self):
        list_branch_corporation = self.branch_corporations_client.get_list_branch_corporations().get_all().results
        print()
        assert isinstance(list_branch_corporation , list)

    def test_get_retrieve_branch_corporation(self):
        global new_branch_corporation 

        get__branch_corporation = (
            self.branch_corporations_client.get_retrieve_branch_corporation(
                new_branch_corporation["id"]
            )
        )
        new_branch_corporation = get__branch_corporation
        assert isinstance(get__branch_corporation , dict)

    def test_patch_update_branch_corporation(self):
        global new_branch_corporation 
        global corporation_global

        patch_branch_corporation = (
            self.branch_corporations_client.patch_update_branch_corporation(
                _id=new_branch_corporation["id"],
                name="StoneFilialPatchTest",
                code="patch",
                corporation_id=corporation_global["code"]
            )
        )
        new_branch_corporation = patch_branch_corporation 
        assert isinstance(patch_branch_corporation , dict)

    def test_put_edit_branch_corporation(self):
        global new_branch_corporation 
        global corporation_global

        put_branch_corporation = (
            self.branch_corporations_client.put_edit_branch_corporation(
                _id=new_branch_corporation["id"],
                name="StoneFilialPutTest",
                code="put",
                corporation_id=corporation_global["code"]
            )
        )
        new_branch_corporation = put_branch_corporation 
        assert isinstance(put_branch_corporation , dict)

    def test_delete_branch_corporation(self):
        global new_branch_corporation 
        
        delete_branch_corporation = (
            self.branch_corporations_client.delete_branch_corporation(new_branch_corporation["id"])
        )
        assert delete_branch_corporation.status_code == 204
