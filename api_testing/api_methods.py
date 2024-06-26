from api_testing.base_request import BaseRequest
from allure import step


class GeneralPublicAPIMethods:

    def __init__(self, base_url, header=None):
        self.base_request = BaseRequest(base_url, header)

    @step("Getting information about the task by its id")
    def task_by_id(self, task_id, expected_error_code=False,
                   expected_error_message=None):
        return self.base_request.get(
            'tasks',
            task_id,
            expected_error_code=expected_error_code,
            expected_error_message=expected_error_message
        )

    @step("Creating a virtual machine")
    def create_vm(self, location_id, image_id, cpu, ram_mb,
                  volumes=None, networks=None, name=None,
                  ssh_key_ids=None, application_ids=None,
                  tags=None, affinity_group_id=None, server_init_script=None,
                  expected_error_code=False, expected_error_message=None):
        data = {
            "location_id": location_id,
            "image_id": image_id,
            "cpu": cpu,
            "ram_mb": ram_mb,
            "volumes": volumes,
            "networks": networks,
            "name": name,
            "ssh_key_ids": ssh_key_ids,
            "application_ids": application_ids,
            "tags": tags,
            "affinity_group_id": affinity_group_id,
            "server_init_script": server_init_script
        }
        return self.base_request.post(
            'servers',
            '',
            data=data,
            expected_error_code=expected_error_code,
            expected_error_message=expected_error_message
        )

    @step("Getting information about a virtual machine by its id")
    def get_vm_by_id(self, vm_id, expected_error_code=False,
                     expected_error_message=None):
        return self.base_request.get(
            'servers',
            vm_id,
            expected_error_code=expected_error_code,
            expected_error_message=expected_error_message
        )

    @step("PUT request to change virtual machine configuration (CPU & RAM)")
    def change_all_vm_configuration(self, cpu, ram_mb, vm_id,
                                    expected_error_code=False,
                                    expected_error_message=None):
        data = {
            "cpu": cpu,
            "ram_mb": ram_mb
        }
        response = self.base_request.put(
            'servers',
            vm_id,
            data=data,
            expected_error_code=expected_error_code,
            expected_error_message=expected_error_message
        )
        return response

    @step("Deleting a virtual machine")
    def delete_vm(self, vm_id, expected_error_code=False,
                  expected_error_message=None):
        return self.base_request.delete(
            'servers',
            vm_id,
            expected_error_code=expected_error_code,
            expected_error_message=expected_error_message
        )

    @step("Powering off the virtual machine using OS tools")
    def shut_down_vm_via_os(self, vm_id, expected_error_code=False,
                            expected_error_message=None):
        return self.base_request.post(
            'servers',
            vm_id + '/power/off',
            '',
            expected_error_code=expected_error_code,
            expected_error_message=expected_error_message
        )

    @step("Powering on the virtual machine")
    def power_on_vm(self, vm_id, expected_error_code=False,
                    expected_error_message=None):
        return self.base_request.post(
            'servers',
            vm_id + '/power/on',
            '',
            expected_error_code=expected_error_code,
            expected_error_message=expected_error_message
        )

    @step("Powering down the virtual machine")
    def shut_down_vm_via_power_off(self, vm_id, expected_error_code=False,
                                   expected_error_message=None):
        return self.base_request.post(
            'servers',
            vm_id + '/power/shutdown',
            '',
            expected_error_code=expected_error_code,
            expected_error_message=expected_error_message
        )

    @step("Rebooting the virtual machine with OS tools")
    def soft_reboot_vm(self, vm_id, expected_error_code=False,
                       expected_error_message=None):
        return self.base_request.post(
            'servers',
            vm_id + '/power/reboot',
            '',
            expected_error_code=expected_error_code,
            expected_error_message=expected_error_message
        )

    @step("Power rebooting the virtual machine")
    def hard_reboot_vm(self, vm_id, expected_error_code=False,
                       expected_error_message=None):
        return self.base_request.post(
            'servers',
            vm_id + '/power/reset',
            '',
            expected_error_code=expected_error_code,
            expected_error_message=expected_error_message
        )

    @step("Getting a list of available locations")
    def get_locations_list(self, expected_error_code=False,
                           expected_error_message=None):
        return self.base_request.get(
            'locations',
            '',
            expected_error_code=expected_error_code,
            expected_error_message=expected_error_message
        )

    @step("Getting a list of available images")
    def get_images_list(self, expected_error_code=False,
                        expected_error_message=None):
        return self.base_request.get(
            'images',
            '',
            expected_error_code=expected_error_code,
            expected_error_message=expected_error_message
        )

    @step("Adding a new volume")
    def add_volume(self, vm_id, name, size_mb, expected_error_code=False,
                   expected_error_message=None):
        data = {
            "name": name,
            "size_mb": size_mb
        }
        response = self.base_request.post(
            'servers',
            vm_id + '/volumes',
            data=data,
            expected_error_code=expected_error_code,
            expected_error_message=expected_error_message
        )
        return response
