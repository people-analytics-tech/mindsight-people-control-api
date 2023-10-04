from mindsight_people_control_api.scripts.corporations import Corporations

corporation_global = {}


class TestCorporationRequests:
    corporations_client = Corporations()

    def test_post_create_branch_corporation(self):
        global corporation_global

        post_corporation = self.corporations_client.post_create_corporation(
            code="post", name="StonePostTest"
        )
        corporation_global = post_corporation
        assert isinstance(post_corporation , dict)

    def test_get_list_corporations(self):
        list_corporation = (
            self.corporations_client.get_list_corporations().get_all().results
        )
        print()
        assert isinstance(list_corporation , list)

    def test_get_retrieve_branch_corporation(self):
        global corporation_global

        get_corporation = self.corporations_client.get_retrieve_corporation(
            corporation_global["id"]
        )
        corporation_global = get_corporation
        assert isinstance(get_corporation , dict)
        print()

    def test_patch_update_branch_corporation(self):
        global corporation_global

        patch_corporation = self.corporations_client.patch_update_corporation(
            _id=corporation_global["id"],
            name="StonePatchTest",
            code="patch",
        )
        corporation_global = patch_corporation
        assert isinstance(patch_corporation , dict)

    def test_put_edit_branch_corporation(self):
        global corporation_global

        put_corporation = self.corporations_client.put_edit_corporation(
            _id=corporation_global["id"], name="StonePutTest", code="put"
        )
        corporation_global = put_corporation
        assert isinstance(put_corporation , dict)

    def test_delete_corporation(self):
        global corporation_global

        delete_corporation = (
            self.corporations_client.delete_corporation(corporation_global["id"])
        )
        assert delete_corporation.status_code == 204
